import requests
from lxml import html

page = requests.get('https://www.rottentomatoes.com/m/fantastic_beasts_and_where_to_find_them/reviews')
tree = html.fromstring(page.content.decode('utf-8','ignore'))
review=tree.xpath('//div[@class="the_review"]/text()')
for i in review:
	print(i)


for page_number in range (2, 14):
	import time
	time.sleep(2)
	page = requests.get('https://www.rottentomatoes.com/m/fantastic_beasts_and_where_to_find_them/reviews/?page={}&sort='.format(page_number))
	tree = html.fromstring(page.content.decode('utf-8','ignore'))
	review=tree.xpath('//div[@class="the_review"]/text()')
	for i in review:
		print(i)
