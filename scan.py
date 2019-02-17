import argparse
import json

from html_parser import HTMLParser
from processing import text_to_word_count
from www import fetch_html_page

parser = argparse.ArgumentParser(description='HTML scrapper')
parser.add_argument(dest='url', help='web-page address')
args = parser.parse_args()

url = args.url

html = fetch_html_page(url)

html_parser = HTMLParser(html)

title = html_parser.title()

text = html_parser.div_contents()
result = text_to_word_count(text)

print(title)
print(json.dumps(result, indent=4))

# Note: this code is written with `clarity` in mind, not `performance` (if a need arises we can make it run much faster).
