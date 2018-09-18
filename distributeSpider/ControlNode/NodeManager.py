# encoding:utf-8
# taskManager.py for windows
from multiprocessing import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from multiprocessing import Process
from UrlManager import UrlManager
from HtmlParser import HtmlParser
from HtmlDownloader import HtmlDownloader
from DataOutput import DataOutput
import time
import sys
sys.setrecursionlimit(10000)


class NodeManager(BaseManager):
	"""控制调度器 NodeManager"""
	pass

	def start_Manager(self,url_q,result_q):
		'''
		创建一个分布式管理器
		:param url_q：url队列
		:param result_q：结果队列
		:return:
		'''
		BaseManager.register('get_task_queue',callable=lambda:url_q)
		BaseManager.register('get_result_queue',callable=lambda:result_q)
		manager = BaseManager(address=('127.0.0.1',8001),authkey=b'hashci')
		return manager

	def url_manager_proc(self,url_q,conn_q,root_url):
		url_manager = UrlManager()
		url_manager.add_new_url(root_url)
		while True:
			while url_manager.has_new_url():
				new_url = url_manager.get_new_url()
				url_q.put(new_url)
				print('old_url=',url_manager.old_url_size())
				if url_manager.old_url_size()>2000:
					# 通知爬行节点工作结束
					url_q.put('end')
					print('控制节点发起结束通知！')
					# 关闭管理节点，同时存储set状态
					url_manager.save_progress('new_urls.txt',url_manager.new_urls)
					url_manager.save_progress('old_urls.txt',url_manager.old_urls)
			# 将从result_solve_proc获取到的URL添加到URL管理器
			try:
				if not conn_q.empty():
					urls = conn_q.get(True)
					url_manager.add_new_urls(urls)
			except Exception as e:
				time.sleep(0.1)

	def result_solve_proc(self,result_q,conn_q,store_q):
		while True:
			try:
				if not result_q.empty():
					content = result_q.get(True)
					if content['new_urls']=='end':
						# 结果分析进程接收通知然后结束
						print('结果分析进程接收通知然后结束！')
						store_q.put('end')
					conn_q.put(content['new_urls']) # url为set类型
					conn_q.put(content['data']) #解析出的数据位dict类型
				else:
					time.sleep(0.1)
			except Exception as e:
				time.sleep(0.1)

	def store_proc(self,store_q):
		output = DataOutput()
		while True:
			if not store_q.empty():
				data = store_q.get(True)
				if data == 'end':
					print('存储进程接收通知然后结束')
					output.output_end(output.filepath)
					return
				output.store_data(data)
			else:
				time.sleep(0.1)

if __name__ == '__main__':
	# 初始化4个队列
	url_q = Queue()
	result_q = Queue()
	conn_q = Queue()
	store_q = Queue()
	# 创建分布式管理器
	node = NodeManager()
	manager = node.start_Manager(url_q,result_q)
	url_manager_proc = Process(target=node.url_manager_proc, args=(url_q,conn_q,'http://baike.baidu.com/view/284853.htm'))
	result_solve_proc = Process(target=node.result_solve_proc, args=(result_q,conn_q,store_q))
	store_proc = Process(target=node.store_proc, args=(store_q,))
	url_manager_proc.start()
	result_solve_proc.start()
	store_proc.start()
	manager.get_server().serve_forever()



		