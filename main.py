import urllib2
from bs4 import BeautifulSoup

print("load function")

SCRAPING_URL = "https://news.google.com/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"


def lambda_handler(event, context):
    request = urllib2.Request(SCRAPING_URL)
    request.add_header('User-agent', USER_AGENT)

    html = urllib2.urlopen(request).read()
    bs = BeautifulSoup(html)

    print("finish function")
    return [x.text for x in bs.find_all(class_="titletext")]
