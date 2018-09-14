import DataOutput
import HtmlParser
import HtmlDownloader
import UrlManager

class SpiderMan(object):
	"""爬虫调度器"""
	def __init__(self):
		self.urlManager = UrlManager()
		self.htmlDownloader = HtmlDownloader()
		self.htmlParser = HtmlParser()
		self.htmlOutput = DataOutput()

	def crawl(self, root_url):
		# 添加入口URL
		self.urlManager.add_new_url(root_url)
		