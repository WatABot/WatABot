import requests
from newspaper import Article
import nltk
def scrape_article(url):
  news= Article(url)

  news.download()
  news.parse()
  nltk.download('punkt')
  news.nlp()
  return news.text