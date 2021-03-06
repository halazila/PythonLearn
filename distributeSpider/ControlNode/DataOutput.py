# encoding:utf-8
import codecs
import time
class DataOutput(object):
	"""数据存储器 DataOutput"""
	def __init__(self):
		self.filepath = 'baike_%s.html' % (time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime()))
		self.output_head(self.filepath)
		self.datas = []

	def store_data(self,data):
		if data is None:
			return
		self.datas = append(data)
		if len(self.datas)>10:
			self.output_html(self.filepath)

	def output_head(self,path):
		'''
		写HTML头
		:return:
		'''
		fout = codecs.open(path,'w',encoding='utf-8')
		fout.write('<html>')
		fout.write('<body>')
		fout.write('<table>')
		fout.close()

	def output_html(self,path):
		'''
		将数据写入HTML文件
		:param path:文件路径
		:return:
		'''
		fout = codecs.open(path,'a',encoding='utf-8')
		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>' % data['url'])
			fout.write('<td>%s</td>' % data['title'])
			fout.write('<td>%s</td>' % data['summary'])
			fout.write('</tr>')
			self.datas.remove(data)
		fout.close()

	def output_alldata(self):
		'''
		将所有的数据输出到文件
		'''
		if self.datas is not None and len(self.datas) > 0:
			output_html(self.path)

	def output_end(self,path):
		'''
		写HTML尾部
		:param path:文件路径
		:return:
		'''
		fout = codecs.open(path,'a',encoding='utf-8')
		fout.write('</table>')
		fout.write('</body>')
		fout.write('</html>')
		fout.close()
