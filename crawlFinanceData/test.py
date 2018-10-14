import re
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import requests
import pandas as pd
import config
import json
import pandas as pd
import astock

pd.set_option('display.max_columns', None)

url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery38657&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOIATC&js=({data:[(x)],recordsFiltered:(tot)})&cmd=C.2&st=(ChangePercent)&sr=-1&p=1&ps=10000&_=1539169823495'
url = config.EM_MDNow_Url + ('&cmd=%s' % config.EM_MDNow_Cmd['xg'])
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
headers = {'User-Agent':user_agent}
# r = requests.get(url, headers=headers)

# pattern = re.compile(r'jQuery38657\((.*)\)', re.DOTALL)
# json_data = re.findall(pattern, r.text)[0]
# json_data = json_data.replace('data', '"data"').replace('recordsFiltered', '"recordsFiltered"')
# print(json_data)

# 获取股票最新交易行情
# url = 'http://mdfm.eastmoney.com/EM_UBG_MinuteApi/Js/Get?dtype=25&style=tail&check=st&dtformat=HH:mm:ss&cb=jQuery38657&id=0000012&num=10&_=1539236482252'
# r = requests.get(url, headers=headers)
# print(r.text)

# 获取股票业绩报表
# url = "http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?type=YJBB20_YJBB&token=70f12f2f4f091e459a279469fe49eca5&filter=(scode=600519)&st=reportdata&sr=desc&p=1&ps=1000"
# r = requests.get(url, headers=headers)
# data = r.text
# # print(data)
# data = json.loads(data)
# df = pd.DataFrame(data)
# print(df.columns.values)
# print(list(config.EM_YJBB_Dict.keys()))
# df = df[list(config.EM_YJBB_Dict.keys())]
# print(df.columns.values)


# K线图绘制
import matplotlib
import mpl_finance as mpf
import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import date2num

k_data = astock._get_kline('000725', 'sz', 'k')
k_data = k_data['data']
k_df = pd.DataFrame(k_data, columns=['date', 'open', 'close', 'high', 'low', 'tradeVol', 'tradeSum', 'priceAmp'])
k_df = k_df[['date', 'open', 'close', 'high', 'low', 'tradeVol', 'tradeSum']]
k_df[['open', 'close', 'high', 'low', 'tradeVol', 'tradeSum']] = k_df[['open', 'close', 'high', 'low', 'tradeVol', 'tradeSum']].astype(float) #str 格式转换为float格式
k_df.sort_values(by='date', ascending=True, inplace=True)
k_df['date'] = pd.to_datetime(k_df['date']) #date列转换为时间格式
k_df['date'] = k_df['date'].apply(lambda x:date2num(x))
k_df.replace('-',0,inplace=True)
data_mat = k_df.as_matrix()
print(k_df)
fig,ax = plt.subplots()
mpf.candlestick_ochl(ax,data_mat,colordown='#53c156', colorup='#ff1717',width=0.3,alpha=1)
ax.grid(True)
ax.xaxis_date()
plt.show()