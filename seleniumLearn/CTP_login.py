from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

from PIL import Image
import requests
from io import BytesIO

import clf_model

ctp_root_url = 'http://xxxxxxxx/xxxx/xxxx'


class CTPLogin(object):

	def createDriver(self, url):
		driver = webdriver.Firefox()
		driver.set_page_load_timeout(50)
		driver.get(url)
		return driver


	def login(self, driver, broker, user, passwd):
		# 获取表单输入element
		ele_broker = driver.find_element_by_id('broker_')
		ele_user = driver.find_element_by_id('username_show_')
		ele_passwd = driver.find_element_by_id('password_')
		ele_authcode = driver.find_element_by_id('captcha_')
		# 获取验证码element
		ele_img = driver.find_element_by_id('capImg')
		img_url = ele_img.get_attribute('src')
		# 获取验证码
		authcode = self.getAuthcode(driver, img_url)
		# 表单输入
		ele_broker.send_keys(broker)
		ele_user.send_keys(user)
		ele_passwd.send_keys(passwd)
		ele_authcode.send_keys(authcode)
		# 
		ele_submit = driver.find_element_by_id('a_login')
		ele_submit.click()


	def getAuthcode(self, driver, img_url):
		"""Summary
		
		Args:
		    driver (TYPE): Description
		    img_url (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		# 获取webdriver的cookie，供使用脚本request验证码图片时传入使用
		cookies = driver.get_cookies()
		req_cookie = {'JSESSIONID':cookies[0]['value']}
		r = requests.get(img_url, cookies=req_cookie)
		content = r.content
		img_bytes = BytesIO(content)
		img = Image.open(img_bytes)
		code = clf_model.clf_authcode(img)
		return code
		

if __name__ == '__main__':
	ctpLogin = CTPLogin()
	ctpLogin.login(ctpLogin.createDriver(ctp_root_url), 'xxxx', 'xxxx', 'xxxx')