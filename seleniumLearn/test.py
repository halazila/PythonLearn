from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.firefox.webdriver.WebDriver(log_path='geckodriver.log')
# driver.get('http://www.baidu.com')
# # assert u'百度' in driver.title
# elem = driver.find_element_by_name('wd')
# elem.clear()
# elem.send_keys(u'网络爬虫')
# elem.send_keys(Keys.RETURN)
# time.sleep(3)
# # assert u'网络爬虫' not in driver.page_source
# driver.close()


# 获取cookie
# driver = webdriver.Firefox()
# driver.get('http://172.24.125.10:8080/CTPSTK201/')
# cookie = driver.get_cookies()
# print(cookie[0]['value'])
# headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
# import requests
# re_cookie = {'JSESSIONID':cookie[0]['value']}
# re = requests.get('http://172.24.125.10:8080/CTPSTK201/kaptcha.jpg', cookies=re_cookie)

# from PIL import Image
# import numpy as np
# from io import BytesIO

# content = re.content
# imgarr = BytesIO(content)
# img = Image.open(imgarr)
# img.show()
# img_arr = np.array(img)
# print(img_arr.shape)


# ele_img = driver.find_element_by_id('capImg')
# print(ele_img.get_attribute('src'))


import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
from PIL import Image

IMAGE_HEIGHT = 50
IMAGE_WIDTH = 200
VOCAB = ['a', 'b', 'c', 'd', 'e','2', '3', '4', '5', '6', '7', '8','g','f','y','n','m','p','w','x']
CAPTCHA_LENGTH = 5
VOCAB_LENGTH = len(VOCAB)

my_model = keras.models.load_model('kaptcha_model.h5')
my_model.summary()

import requests
re = requests.get('http://172.24.125.10:8080/CTPSTK201/kaptcha.jpg')

from PIL import Image
import numpy as np
from io import BytesIO

content = re.content
imgarr = BytesIO(content)
img = Image.open(imgarr)
img = img.convert('L')
img.show()
img = img.convert('L')
img_arr = np.array(img)
img_arr = img_arr / 255
img_arr = np.transpose(img_arr, (1,0))
img_arr = np.expand_dims(img_arr, 2)
img_arr = np.expand_dims(img_arr, 0)
predict = my_model.predict(img_arr)
predict = predict.reshape(CAPTCHA_LENGTH, VOCAB_LENGTH)
print('predic:', predict)
idx = np.argmax(predict, axis=1)
print('idx', idx)
text = ''
for x in idx:
	text = (text + VOCAB[x])
print(text)