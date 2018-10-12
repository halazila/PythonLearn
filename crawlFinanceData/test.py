import re
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import requests
import pandas as pd
import config
import json


url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery38657&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOIATC&js=({data:[(x)],recordsFiltered:(tot)})&cmd=C.2&st=(ChangePercent)&sr=-1&p=1&ps=10000&_=1539169823495'
url = config.EM_MDNow_Url + ('&cmd=%s' % config.EM_MDNow_Cmd['xg'])
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
headers = {'User-Agent':user_agent}
# r = requests.get(url, headers=headers)

# pattern = re.compile(r'jQuery38657\((.*)\)', re.DOTALL)
# json_data = re.findall(pattern, r.text)[0]
# json_data = json_data.replace('data', '"data"').replace('recordsFiltered', '"recordsFiltered"')
# print(json_data)

# 获取股票最新行情
# url = 'http://mdfm.eastmoney.com/EM_UBG_MinuteApi/Js/Get?dtype=25&check=st&dtformat=HH:mm:ss&cb=jQuery&id=0000012&num=10&_=1539236482252'
# r = requests.get(url, headers=headers)
# print(r.text)

import pytesseract
from PIL import Image
pic = 'C:\\WorkStation\\gitwork\\pythonLearn\\seleniumLearn\\authcode\\image\\train\\2a2a6.jpg'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
image = Image.open(pic)
image = image.convert('L')
image.show()
# code = pytesseract.image_to_string(image, config=tessdata_dir_config)
# print(code)