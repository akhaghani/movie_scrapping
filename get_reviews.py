import requests
from lxml import html

page = requests.get('https://www.rottentomatoes.com/m/fantastic_beasts_and_where_to_find_them/reviews') #Movie or TV show review's URL from Rotten Tomatoes
tree = html.fromstring(page.content.decode('utf-8','ignore'))
review=tree.xpath('//div[@class="the_review"]/text()')
for i in review:
	print(i)


for page_number in range (2, 14): #number of review pages
	import time
	time.sleep(2)
	page = requests.get('https://www.rottentomatoes.com/m/fantastic_beasts_and_where_to_find_them/reviews/?page={}&sort='.format(page_number)) #Movie or TV show review's URL
	tree = html.fromstring(page.content.decode('utf-8','ignore'))
	review=tree.xpath('//div[@class="the_review"]/text()')
	for i in review:
		print(i)
