# -------pickle 序列化操作
# try:
# 	import cPickle as pickle
# except ImportError:
# 	import pickle

# d = dict(url='index.html',title='Index',content='Welcome')
# pdumpsd = pickle.dumps(d)
# print(pdumpsd)
# print(pickle.loads(pdumpsd))

# f = open(r'dump.txt','wb')
# pickle.dump(d,f)
# f.close()
# f = open(r'dump.txt','rb')
# dumpf = pickle.load(f)
# f.close()
# print(dumpf)

# ------多进程
# import os
# from multiprocessing import Process

# def run_proc(name):
# 	print('Child process %s (%s) Running...' % (name,os.getpid()))

# if __name__ == '__main__':
# 	print('Parent process %s.' % os.getpid())
# 	for i in range(5):
# 		p = Process(target=run_proc, args=(str(i),))
# 		print('Process will start')
# 		p.start()
# 		p.join()
# 	print('Process end.')

# ------进程池
# from multiprocessing import Pool
# import os, time, random

# def run_task(name):
# 	print('Task %s (pid = %s) is running...' % (name, os.getpid()))
# 	time.sleep(random.random()*3)
# 	print('Task %s end.' % name)

# if __name__ == '__main__':
# 	print('Current process  %s.' % os.getpid())
# 	p = Pool(processes=5)
# 	for i in range(15):
# 		p.apply_async(run_task, args=(i,))
# 	print('Waiting for all subprocesses done')
# 	p.close()
# 	p.join()
# 	print('All subprocesses done.')

# ------进程间通信
# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码
# def proc_write(q,urls):
# 	print('Process(%s) is writing...' % os.getpid())
# 	for url in urls:
# 		q.put(url)
# 		print('Put %s to queue...' % url)
# 		time.sleep(random.random())
# # 读数据进程执行的代码
# def proc_read(q):
# 	print('Process(%s) is reading...' % os.getpid())
# 	while True:
# 		try:
# 			url = q.get(True)
# 			print('Get %s from queue.' % url)
# 		except Exception as e:
# 			print('***Error***')
		

# if __name__ == '__main__':
# 	# 父进程创建Queue，并传递给子进程
# 	q = Queue()
# 	proc_write1 = Process(target=proc_write,args=(q,['url_1','url_2','url_3']))
# 	proc_write2 = Process(target=proc_write,args=(q,['url_4','url_5','url_6']))
# 	proc_reader = Process(target=proc_read,args=(q,))
# 	# 启动子进程proc_write
# 	proc_write1.start()
# 	proc_write2.start()
# 	# 启动子进程proc_read
# 	proc_reader.start()
# 	# 等待proc_write结束
# 	proc_write1.join()
# 	proc_write2.join()
# 	# proc_read进程是死循环，无法等待其结束，只能强行终止
# 	# while q.empty()==False:
# 	# 	pass
# 	# proc_reader.terminate()

# ------多线程
# print('*************///多线程1：实现threading.Thread类///****************')
# import random
# import time,threading
# # 新线程执行的代码
# def thread_run(urls):
# 	print('Current %s is running...' % threading.current_thread().name)
# 	for url in urls:
# 		print('%s ---->>> %s' % (threading.current_thread().name, url))
# 		time.sleep(random.random())
# 	print('%s ended.' % threading.current_thread().name)

# print('Current %s is running...' % threading.current_thread().name)
# t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1','url_2','url_3'],))
# t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url_4','url_5','url_6'],))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('%s ended.' % threading.current_thread().name)

# print('*************///多线程2：继承thrading.Thread类///****************')

# class myThread(threading.Thread):
# 	"""docstring for myThread"""
# 	def __init__(self, name, urls):
# 		threading.Thread.__init__(self, name=name)
# 		self.urls = urls

# 	def run(self):
# 		print('Current %s is running...' % threading.current_thread().name)
# 		for url in self.urls:
# 			print('%s ---->>> %s' % (threading.current_thread().name, url))
# 			time.sleep(random.random())
# 		print('%s ended.' % threading.current_thread().name)
# print('Current %s is running...' % threading.current_thread().name)
# t1 = myThread(name='Thread_1', urls=['url_1','url_2','url_3'])
# t2 = myThread(name='Thread_2', urls=['url_4','url_5','url_6'])
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('%s ended.' % threading.current_thread().name)

# print('*************///线程同步：不可重入锁Lock和可重入锁RLock///****************')
# import threading
# mylock = threading.RLock()
# num = 0
# class myThread2(threading.Thread):
# 	"""docstring for myThread2"""
# 	def __init__(self, name):
# 		threading.Thread.__init__(self, name=name)

# 	def run(self):
# 		global num
# 		while True:
# 			mylock.acquire()
# 			print('%s locked, Number:%d' % (threading.current_thread().name, num))
# 			if num>=4:
# 				mylock.release()
# 				print('%s released, Number:%d' % (threading.current_thread().name, num))
# 				break
# 			num+=1;
# 			print('%s released, Number:%d' % (threading.current_thread().name, num))
# 			mylock.release()

# thread1 = myThread2('myThread2_1')
# thread2 = myThread2('myThread2_2')
# thread1.start()
# thread2.start()

# http请求
# print('*************///http请求(urllib)///****************')
# import urllib.request as request
# import urllib.parse as urlparse
# response = request.urlopen('http://www.zhihu.com')
# html = response.read()
# print(html.decode('utf-8'))
# url = 'https://www.zhihu.com/signup?next=%2F'
# postdata = {'username':'*******',
# 			'password':'********'}
# data = urlparse.urlencode(postdata).encode('utf-8')
# header = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)','Reffer':'https://www.zhihu.com'}
# req = request.Request(url, data, header)
# response = request.urlopen(req)
# html = response.read()
# print(html.decode('utf-8'))

# print('*************///http请求(requests模块)///****************')
# import requests
# postdata = {'username':'********',
# 			'password':'********'}
# r = requests.post('https://www.zhihu.com/signup?next=%2F', data=postdata)
# print(r.content.decode('utf-8'))


# print('*************///数据存储（无数据库）///****************')
# print('///使用BeautifulSoup解析html////')
# import requests
# from bs4 import BeautifulSoup
# import json
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
# headers = {'User-Agent':user_agent}
# r = requests.get('http://seputu.com/', headers=headers)
# # print(r.content.decode('utf-8'))
# soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
# # print(r.text)
# content = []
# for mulu in soup.find_all(class_='mulu'):
# 	h2 = mulu.find('h2')
# 	if h2!=None:
# 		h2_title = h2.string # 获取标题
# 		# print(h2_title)
# 		li = []
# 		for a in mulu.find(class_='box').find_all('a'):
# 			href = a.get('href')
# 			box_title = a.get('title')
# 			# print(href, box_title)
# 			li.append({'href':href, 'box_title':box_title})
# 		content.append({'title':h2_title, 'content':li})
# with open('daomu.json', 'w') as fp:
# 	json.dump(content, fp=fp, indent=4)

# print('///使用lxml解析html////')
# from lxml import etree
# import requests
# import csv
# import re
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
# headers = {'User-Agent':user_agent}
# r = requests.get('http://seputu.com/', headers=headers)
# html = etree.HTML(r.content)
# div_mulus = html.xpath('.//*[@class="mulu"]')
# pattern = re.compile(r'\s*\[(.*)\]\s*(.*)')
# raws = []
# for div_mulu in div_mulus:
# 	div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
# 	if len(div_h2) > 0:
# 		h2_title = div_h2[0]
# 		a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
# 		for a in a_s:
# 			# href 属性
# 			href = a.xpath('./@href')[0].encode('utf-8').decode('utf-8')
# 			# title 属性
# 			box_title = a.xpath('./@title')[0].encode('utf-8').decode('utf-8')
# 			match = pattern.search(box_title)
# 			if match != None:
# 				date = match.group(1)
# 				real_title = match.group(2)
# 				content = (h2_title, real_title, href, date)
# 				# print(content)
# 				raws.append(content)
# headers = ['title','real_title','href','date']
# with open('daomu.csv','w',newline='') as f:
# 	f_csv = csv.writer(f)
# 	f_csv.writerow(headers)
# 	f_csv.writerows(raws)


# print('///使用urlretrieve抽取多媒体文件////')
# import urllib
# from lxml import etree
# import requests

# def Schedule(blocknum, blocksize, totalsize):
# 	'''
# 	blocknum：已经下载的数据块
# 	blocksize：数据块的大小
# 	totalsize：远程文件的大小
# 	'''
# 	per = 100.0*blocknum*blocksize/totalsize
# 	if per>100:
# 		per = 100
# 	print('当前下载进度：%d' %per)

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
# headers = {'User-Agent':user_agent}
# r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
# html = etree.HTML(r.text)
# img_urls = html.xpath('.//img/@src')
# i = 0
# for img_url in img_urls:
# 	urllib.request.urlretrieve(img_url,'img'+str(i)+'.jpg',Schedule)
# 	i+=1

print('///使用email发送邮件////') # 已验证，可行
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '********' # 此处输入网易邮箱账号
password = '*******' # 网易邮箱开启客户端授权，这里用客户端验证码来代替密码登录
to_addr = '*******' # 收件人邮箱地址
smtp_server = 'smtp.126.com'
msg = MIMEText('爬虫信息http 403', 'plain', 'utf-8')
msg['From'] = _format_addr('一号爬虫<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('一号爬虫运行状态', 'utf-8').encode()

# 发送邮件
server = smtplib.SMTP(smtp_server) # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
server.set_debuglevel(1)
server.ehlo(smtp_server)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()