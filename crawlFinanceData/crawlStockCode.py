import re
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import requests
import pandas as pd

url = 'http://quote.eastmoney.com/stocklist.html'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get(url, headers=headers)
if r.status_code == 200:
	r.encoding = 'GBK'
# print(r.text)
bsoup = BeautifulSoup (r.text, 'html.parser')
stockuls = bsoup.find('div', class_='quotebody').find_all('ul')
list_stock_name, list_stock_code, list_stock_uri = [], [], []
for ul in stockuls:
	stocklis = ul.find_all('li')
	for li in stocklis:
		string = li.string
		string_gourp = re.search(r'(.*)\((\d+)\)', string)
		stock_name = string_gourp.group(1)
		stock_code = string_gourp.group(2)
		href = li.find('a')['href']
		# href format like 'http://quote.eastmoney.com/sh201000.html', we just need sh201000
		stock_uri = href.split('/')[-1].split('.')[0] 
		list_stock_name.append(stock_name)
		list_stock_code.append(stock_code)
		list_stock_uri.append(stock_uri)

stock_dict = {'stock_name':list_stock_name, 'stock_code':list_stock_code, 'stock_uri':list_stock_uri}
stock_df = pd.DataFrame(data=stock_dict)
stock_df.to_csv('stocks.csv', encoding='GBK')