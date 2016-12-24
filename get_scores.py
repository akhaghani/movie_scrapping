import requests
from lxml import html

page = requests.get('https://www.rottentomatoes.com/m/fantastic_beasts_and_where_to_find_them/reviews')  #Movie or TV show URL on Rotten Tomatoes
tree = html.fromstring(page.content.decode('utf-8','ignore'))
scores=tree.xpath('//div[@class="small subtle"]/text()')
for i in scores:
	print(i)

for page_number in range (2, 14): #Number of review pages starting at page two
	import time
	time.sleep(2)
	page = requests.get('https://www.rottentomatoes.com/m/fantastic_beasts_and_where_to_find_them/reviews/?page={}&sort='.format(page_number))  # Movie or TV show URL
	tree = html.fromstring(page.content.decode('utf-8','ignore'))
	scores=tree.xpath('//div[@class="small subtle"]/text()')
	for i in scores:
		print(i)
