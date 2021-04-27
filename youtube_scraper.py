import requests
from bs4 import BeautifulSoup

def youtubeViews(input):
	videos = input
	views = []
	for video in videos:
		url = video
		soup = BeautifulSoup(requests.get(url).text, 'lxml')
		views.append(soup.select_one('meta[itemprop = "interactionCount"][content]')['content'])

	##put links/views into CSV 