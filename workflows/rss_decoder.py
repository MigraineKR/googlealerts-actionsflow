import feedparser
import html
import sys

def escape_quotes(text):
    # 문자열 내의 큰따옴표와 작은따옴표를 이스케이프합니다.
    return text.replace('"', '\\"').replace("'", "\\'")

def decode_rss_feed(url):
    feed = feedparser.parse(url)
    if feed.entries:
        entry = feed.entries[0]
        title = escape_quotes(html.unescape(entry.title))
        content = escape_quotes(html.unescape(entry.summary))
        print(f"::set-output name=title::{title}")
        print(f"::set-output name=content::{content}")

if __name__ == "__main__":
    rss_url = sys.argv[1]
    decode_rss_feed(rss_url)
