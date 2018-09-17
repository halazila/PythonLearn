from DataOutput import DataOutput
from HtmlParser import HtmlParser
from HtmlDownloader import HtmlDownloader
from UrlManager import UrlManager
import traceback

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
        # 判断url管理器中是否有新的url，同时判断抓取了多少个url
		while (self.urlManager.has_new_url() and self.urlManager.old_url_size()<100):
			try:
				# 从URL管理器获取新的url
				new_url = self.urlManager.get_new_url()
				# HTML下载器下载网页
				html = self.htmlDownloader.download(new_url)
				# HTML解析器抽取网页数据
				new_urls,data = self.htmlParser.parser(new_url,html)
				# 将抽取的url添加到URL管理器中
				self.urlManager.add_new_urls(new_urls)
				# 数据存储器存储数据
				self.htmlOutput.store_data(data)
			except Exception as e:
				print(traceback.format_exc())
		# 数据存储器将文件输出成指定格式
		self.htmlOutput.output_html()

if __name__ == '__main__':
	spider_man = SpiderMan()
	spider_man.crawl("http://baike.baidu.com/view/284853.htm")