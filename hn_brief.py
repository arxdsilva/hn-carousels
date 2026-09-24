#!/usr/bin/env python3
"""
Compact Hacker News research for the carousel routine.
Replaces browsing the HN front page and comment pages with small, pre-trimmed text.

  python3 hn_brief.py top               # ranked top 10, skipping stories already in posts/
  python3 hn_brief.py story <item_id>   # article text + top comments for one story

Uses the official HN API (hacker-news.firebaseio.com). No API key needed.
Optional, for cleaner article text: pip3 install trafilatura
"""
import glob, html, json, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://hacker-news.firebaseio.com/v0"
HERE = os.path.dirname(os.path.abspath(__file__))
ARTICLE_WORD_LIMIT = 1800   # enough for the argument and key numbers
TOP_COMMENTS = 12           # top-level comments, in HN's ranked order
REPLIES_PER_COMMENT = 1     # first reply often holds the best counterpoint
COMMENT_CHAR_LIMIT = 500


def get_json(url):
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.load(r)


def get_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (hn-carousels)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "replace")


def item(i):
    return get_json(f"{API}/item/{i}.json") or {}


def clean(s):
    s = re.sub(r"<p>", "\n", s or "")
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def covered_ids():
    ids = set()
    for f in glob.glob(os.path.join(HERE, "posts", "*", "sources.md")):
        ids.update(re.findall(r"item\?id=(\d+)", open(f, encoding="utf-8").read()))
    return ids


def cmd_top():
    ids = get_json(f"{API}/topstories.json")[:10]
    with ThreadPoolExecutor(10) as ex:
        stories = list(ex.map(item, ids))
    done = covered_ids()
    for rank, s in enumerate(stories, 1):
        if not s or str(s.get("id")) in done:
            continue
        print(f"#{rank} id={s['id']} | {s.get('score', 0)} pts | {s.get('descendants', 0)} comments | "
              f"{s.get('title')} | {s.get('url', 'self post')}")


def article_text(url):
    raw = get_text(url)
    try:
        import trafilatura
        text = trafilatura.extract(raw) or ""
    except ImportError:
        raw = re.sub(r"(?is)<(script|style|nav|header|footer|aside)[^>]*>.*?</\1>", " ", raw)
        text = clean(re.sub(r"\s+", " ", raw))
    words = text.split()
    cut = " ".join(words[:ARTICLE_WORD_LIMIT])
    return cut + (" [...truncated]" if len(words) > ARTICLE_WORD_LIMIT else "")


def cmd_story(story_id):
    s = item(story_id)
    print(f"TITLE: {s.get('title')}\nURL: {s.get('url', 'self post')}\n"
          f"HN: https://news.ycombinator.com/item?id={story_id} | {s.get('score')} pts | "
          f"{s.get('descendants')} comments\n")
    if s.get("text"):
        print("POST TEXT:\n" + clean(s["text"]) + "\n")
    if s.get("url"):
        try:
            print("ARTICLE:\n" + article_text(s["url"]) + "\n")
        except Exception as e:
            print(f"ARTICLE: could not fetch ({e})\n")

    kids = s.get("kids", [])[:TOP_COMMENTS]
    with ThreadPoolExecutor(12) as ex:
        comments = list(ex.map(item, kids))
    print("TOP COMMENTS (ranked):")
    for c in comments:
        if not c or c.get("deleted") or c.get("dead"):
            continue
        print(f"- {c.get('by')}: {clean(c.get('text'))[:COMMENT_CHAR_LIMIT]}")
        for rid in c.get("kids", [])[:REPLIES_PER_COMMENT]:
            r = item(rid)
            if r and not r.get("deleted") and not r.get("dead"):
                print(f"    reply {r.get('by')}: {clean(r.get('text'))[:COMMENT_CHAR_LIMIT]}")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "top":
        cmd_top()
    elif len(sys.argv) >= 3 and sys.argv[1] == "story":
        cmd_story(sys.argv[2])
    else:
        print(__doc__)