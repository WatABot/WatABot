import requests

url = 'http://52.175.204.249/fakebox/check'

title = ""
content = ""
link = ""




def run(title, content, link):
	newsObj = {'title': title, 'content':content, 'url':link}
	x = requests.post(url, data = newsObj)
	return x.text
