from multiprocessing import Queue
from HtmlParser import HtmlParser
from HtmlDownloader import HtmlDownloader
from multiprocessing.managers import BaseManager
import sys
sys.setrecursionlimit(10000)

class SpiderWork(object):
	"""爬虫调度器 SpiderWork"""
	def __init__(self):
		BaseManager.register('get_task_queue')
		BaseManager.register('get_result_queue')
		server_addr = '127.0.0.1'
		print('Connect to server %s...' % server_addr)
		self.m = BaseManager(address=(server_addr,8001), authkey=b'hashci')
		self.m.connect()
		self.task = self.m.get_task_queue()
		self.result = self.m.get_result_queue()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		print('init finish')

	def crawl(self):
		while True:
			try:
				if not self.task.empty():
					url = self.task.get(True)
				if url == 'end':
					print('爬虫节点接收到停止通知')
					self.result.put({'new_urls':'end','data':'end'})
					return
				print('爬虫节点正在解析： %s' % url.encode('utf-8'))
				content = self.downloader.download(url)
				new_urls,data = self.parser.parser(url,content)
				print(new_urls)
				self.result.put({'new_urls':new_urls,'data':data})
			except EOFError as e:
				print('连接工作节点失败')
				return
			except Exception as e:
				print(e)
				print('Crawl fail')

if __name__ == '__main__':
	spider = SpiderWork()
	spider.crawl()