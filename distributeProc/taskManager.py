# coding:utf-8
# taskManager.py for windows
import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
# 任务个数
task_number = 10
# 定义收发队列
task_queue = Queue.Queue(task_number)
result_queue = Queue.Queue(task_number)

def get_task():
	return task_queue

def get_result():
	return result_queue

class QueueManager(BaseManager):
	"""创建QueueManager"""
	pass

def win_run():
	# 绑定调用接口
	QueueManager.register('get_task_queue', callable=get_task)
	QueueManager.register('get_result_queue', callable=get_result)
	# 绑定端口并设置验证口令，Windows下需要填写IP地址，Linux下不填写默认为本地
	manager = QueueManager(address=('127.0.0.1',8001), authkey='hashci')
	# 启动
	manager.start()
	try:
		pass
	except Exception as e:
		raise e
	finally:
		pass
		