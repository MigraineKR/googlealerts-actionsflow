import feedparser
import html
import sys

def decode_rss_feed(url):
    feed = feedparser.parse(url)
    if feed.entries:
        entry = feed.entries[0]
        title = html.unescape(entry.title)
        content = html.unescape(entry.summary)
        print(f"::set-output name=title::{title}")
        print(f"::set-output name=content::{content}")

if __name__ == "__main__":
    rss_url = sys.argv[1]
    decode_rss_feed(rss_url)
