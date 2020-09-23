import requests, os, string, argparse
from bs4 import BeautifulSoup

url = ["http://www.hindustantimes.com/rss/topnews/rssfeed.xml",
       "https://feeds.feedburner.com/TheHackersNews",
       "http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/health/rss.xml",
       "http://feeds.bbci.co.uk/news/world/rss.xml",
       "http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml",
       "https://feeds.feedburner.com/ndtvnews-top-stories",
       "https://feeds.feedburner.com/ndtvnews-latest",
       "https://www.indiatoday.in/rss/home",
       "https://zeenews.india.com/rss/india-national-news.xml",
       "https://zeenews.india.com/rss/world-news.xml",
       "https://www.eff.org/rss/updates.xml",
       "https://timesofindia.indiatimes.com/rssfeedstopstories.cms?x=1",
       "http://feeds.feedburner.com/NDTV-LatestNews",
       "https://www.indiatoday.in/rss/1206578",
       "https://indianexpress.com/feed/",
       "https://www.feedspot.com/infiniterss.php?_src=feed_title&followfeedid=410006&q=site:https%3A%2F%2Fwww.thehindu.com%2Fnews%2Fnational%2F%3Fservice%3Drss",
       "http://www.news18.com/rss/india.xml",
       "https://www.reddit.com/r/worldnews/.rss",
       "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml"]
parser = argparse.ArgumentParser(description='NEWS')       
parser.add_argument("-n", default='ANY RANDOM NEWS')
args = parser.parse_args()
out = ''

def run(msg):
    print(msg)
    if msg == '':
        return 'empty content is sent'
        exit(0)
    elif len(msg) <= 5: 
        return 'Given news content is low'
        exit(0)
    
    i = 0
    n = 0
    webs = len(url)
    for i in range(webs):   
        resp = requests.get(url[i])
        soup = BeautifulSoup(resp.content, features="xml")
        items = soup.findAll('item')
        news_items = []
        for item in items:
            news_item = {}
            news_item['title'] = item.title.text
            news_item['description'] = item.description.text  
            finaltitle = item.title.text.lower()
            finaldis = item.description.text.lower()
            if msg in finaltitle:
                n += 1
            elif msg in finaldis:
                n += 1
    if n != 0:
        print(n)
        return "The News is True"
    if n == 0: 
        return  "The News is Fake"

