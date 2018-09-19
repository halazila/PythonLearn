import requests
import re
import time
import json

def download(url):
	if url is None:
		return None
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
	headers = {'User-Agent':user_agent}
	r = requests.get(url,headers=headers)
	if r.status_code==200:
		r.encoding='utf-8'
		return r.text
	return None

def parse_url(response,pattern):
	urls = pattern.findall(response)
	if urls is not None:
		return list(set(urls)) # 将urls进行去重
	else:
		return None

def parse_json(response):
	# 将 '=' 和 ';' 之间的内容提取出来
	pattern = re.compile(r'=(.*?);')
	result = pattern.findall(response)[0]
	if result is not None:
		value = json.loads(result)
		return value
	return None

def crawl(root_url):
	content = download(root_url)
	pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
	urls = parse_url(content,pattern)
	for url in urls:
		try:
			t = time.strftime('%Y%m%d%H%M%S8998', time.localtime())
			rank_url = 'http://service.library.mtime.com/Movie.api'\
				'?Ajax_CallBack=true'\
				'&Ajax_CallBackType=Mtime.Library.Services'\
				'&Ajax_CallBackMethod=GetMovieOverviewRating'\
				'&Ajax_CrossDomain=1'\
				'&Ajax_RequestUrl=%s'\
				'&t=%s'\
				'&Ajax_CallBackArgument0=%s' % (url[0],t,url[1])
			rank_content = download(rank_url)
			data = parse_json(rank_content)
			print(data)
		except Exception as e:
			print('crawl failed:',e)
	print('crawl finished')

if __name__ == '__main__':
	crawl('http://theater.mtime.com/China_Shanghai/')