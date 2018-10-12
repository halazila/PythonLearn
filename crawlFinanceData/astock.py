import requests
import config
import json
import demjson
import re
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
headers = {'User-Agent':user_agent}

def _get_kline(s_id, m_id, k_type):
	"""Summary
	获取K线图数据
	Args:
	    s_id (str): 6位股票代码
	    m_id (str): 市场代码, 'sh'--上证所， 'sz'--深证所
	    k_type (str): k线数据类型，k--日K, wk--周K, mk--月K, m5k--5分钟K线, m30k--30分钟K线, m60k--60分钟K线
	Returns:
		dict: {name, market, code, data}
	"""
	market_id = config.EM_Market_Cons[m_id]
	sm_id = s_id + market_id
	full_url = config.EM_KLine_Url + ('&id=%s&type=%s' % (sm_id, k_type))
	r = requests.get(full_url, headers=headers)
	if r.status_code != 200:
		return None
	pattern = re.compile(r'jsonp\d+\((.*)\)', re.DOTALL)
	json_data = re.findall(pattern, r.text)[0]
	data = json.loads(json_data)
	res = {'name':data['name'], 'market':m_id, 'code':data['code'], 'data':data['data']}
	return res

def _get_all_boards(board_type = 'industry'): 
    """Summary
    获取所有板块信息，包括板块名称，板块代码，对应板块的链接
    Args:
        board_type (str): 板块类型：概念板块(concept)，行业板块(industry)，地域板块(region)
    Returns:
    	list: 板块列表, [{key, title, href},{}...], encoding = 'utf-8
    """
    # http://quote.eastmoney.com/center/sidemenu.json
    if board_type not in ['concept', 'industry', 'region']:
    	raise ValueError('incorrect args, arg board_type should be in [concept, industry, region]')
    r = requests.get(config.EM_MCenter_Url + 'sidemenu.json', headers=headers)
    if r.status_code != 200:
    	return None
    # get response json
    json_data = json.loads(r.text)
    for jdata in json_data:
    	# pick sh & sz market board
    	if jdata['key'] == 'hsbroad':
    		# pick the secondary board
    		hs_next = jdata['next']
    		for b_next in hs_next:
    		 	if b_next['key'] == (board_type + '_board'):
    		 		# pick detail board
    		 		board_list = b_next['next']
    		 		res_list = []
    		 		for board in board_list:
    		 			b_dict = {'key':board['key'].split('-')[-1], 'title':board['title'], 'href':(config.EM_MHome_Url + board['href'])}
    		 			res_list.append(b_dict)
    		 		return res_list
	
def _get_now_data_by_market(market_id):
	"""Summary
	通过市场编号获取该市场所有的股票最新交易信息
	# sh-上证A股，sz-深证A股，hs-沪深A股，xg-新股，zxb-中小板，cyb-创业板，hgt-沪股通，sgt-深股通
	Args:
	    market_id (str): 市场代码
	
	Returns:
	    list: 返回元素为dict的list，
	    {沪深市场代码(1--sh,2--sz)，股票代码，股票名称，最新价，涨跌额，涨跌幅，成交量（手），成交额，振幅，最高，最低，今开，昨收，量比，换手率，市盈率（动态），市净率，总市值，流通市值，60日涨跌幅，年初至今涨跌幅，时间}
	"""
	cmd_str = config.EM_MDNow_Cmd[market_id]
	url = config.EM_MDNow_Url + ('&cmd=%s' % cmd_str)
	r = requests.get(url, headers=headers)
	if r.status_code != 200:
		return None
	pattern = re.compile(r'jQuery38657\((.*)\)', re.DOTALL)
	json_data = re.findall(pattern, r.text)[0]
	json_data = json_data.replace('data', '"data"').replace('recordsFiltered', '"recordsFiltered"')
	res_str = json.loads(json_data)
	stock_data = res_str['data']
	res_list = []
	stock_dict = {}
	for  stk_d in stock_data:
		fields = stk_d.split(',')
		stock_dict = {'marketId':fields[0], 'stkCode':fields[1], 'stkName':fields[2], 'newestPrice':fields[3], 'updownSum':fields[4], 'updownAmp':(fields[5] + ('%' if fields[5] is not '-' else '')), \
			'tradeVol':fields[6], 'tradeSum':fields[7], 'priceAmp':(fields[8] + ('%' if fields[8] is not '-' else '')), 'maxPrice':fields[9], 'minPrice':fields[10], 'todayOpen':fields[11], \
			'lastClose':fields[12], 'quantRatio':fields[14], 'turnoverRate':(fields[15] + ('%' if fields[15] is not '-' else '')), 'PE':fields[16], 'PB':fields[17], 'totMarketVal':fields[18], \
			'circulateVal':fields[19], '60dayUpdownAmp':fields[20], 'YTDUpdownAmp':fields[21], 'dataTime':fields[-2]}
		res_list.append(stock_dict)
	return res_list

def _get_now_data_by_stock(stock_id, market_id):
	"""Summary
	获取个股的最新行情
	
	Args:
	    stock_id (str): 股票代码
	    market_id (str): 市场代码
	
	Returns:
	    dict: 个股行情信息
	"""

	return res
	
if __name__ == '__main__':
	print(_get_kline('600029', 'sh', 'k'))
	# print(_get_all_boards('industry'))
	# stock = _get_now_data_by_market('xg')
	# print(len(stock))
	# print(stock)
