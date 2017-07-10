from lxml import html
import requests
import os

def scan_template():
	urls = []
	headers = []
	tags = []
	
	template = open('template.txt', 'r')
	
	for line in template.readlines():
		if line[0] == '/#':
			pass
		
		else:
			if line[0] == 'l':
				urls.append(line.split('l:', 1)[1])
			elif line[0] == 'h':
				headers.append(line.split('h:', 1)[1])
			if line[0] == 'l':
				urls.append(line.split('l:', 1)[1])
			if line[0] == 'l':
				urls.append(line.split('l:', 1)[1])
			
				

class scraper:
	def __init__(self, url, header=None):
		
		self.url = url
		self.header = header

	def getauthinfo():
		pass
	
	def getheaders():
		pass
		
	def writetofile():
		pass
	
	def download_img(self, url=self.url):
	
	def makerequest(self):
		page = requests.get(self.url, self.header=params)
		self.content = html.fromstring(page.content)
		
		
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print('Buyers: ', buyers)
print('Prices: ', prices)











