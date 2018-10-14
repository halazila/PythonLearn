# eastmoney data API

# K线图数据URL，full_url = KLine_Url+'&id=%s'+'&type=%s' % (id, type)
# id: 6 digits stock code + market code(1 represents sh, 2 represents sz), like '0000012' 
# type: type of kLine, k--day line, wk--week line, mk--month line, m5k--5 minutes line, m30k--30 minutes line, m60k--60 minutes line
EM_KLine_Url = 'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?token=4f1862fc3b5e77c150a2b985b12db0fd&rtntype=6&authorityType=fa&cb=jsonp1539101454906'
# eastmoney market center address
EM_MCenter_Url = 'http://quote.eastmoney.com/center/'
# eastmoney market center home domain
EM_MHome_Url = 'http://quote.eastmoney.com/'

# 个股最新行情URL
# EM_MToday_Url + ('&cmd=%s' % cmd)
EM_MDNow_Url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery38657&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOIATC&js=({data:[(x)],recordsFiltered:(tot)})&st=(ChangePercent)&sr=-1&p=1&ps=10000&_=1539169823495'
# sh-上证A股，sz-深证A股，hs-沪深A股，xg-新股，zxb-中小板，cyb-创业板，hgt-沪股通，sgt-深股通
EM_MDNow_Cmd = {'sh':'C.2', 'sz':'C._SZAME', 'hs':'C._A', 'xg':'C.BK05011', 'zxb':'C.13', 'cyb':'C.80', 'hgt':'C.BK07071', 'sgt':'C.BK08041'}

# 沪深市场对应编码
EM_Market_Cons = {'sh':'1', 'sz':'2'}

# 个股最新价格URL
# EM_MDStock_Url + ('&id=%s' % '0000012')
EM_MDStock_Url = 'http://mdfm.eastmoney.com/EM_UBG_MinuteApi/Js/Get?dtype=25&style=tail&check=st&dtformat=HH:mm:ss&cb=jQuery38657&num=10&_=1539236482252'

# 个股业绩报表URL
# EM_YJBBStock_Url + &filter=(scode=600519)，600519代表个股代码，url中p代表page，ps代表pagesize，为了获取全部数据，这里将ps设为一个较大值1000
EM_YJBBStock_Url = 'http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?type=YJBB20_YJBB&token=70f12f2f4f091e459a279469fe49eca5&st=reportdata&sr=desc&p=1&ps=1000'

# 业绩报表名称对照
EM_YJBB_Dict = {
	'scode':'股票代码'
	, 'sname':'股票名称'
	, 'securitytype':'股票类别'
	, 'trademarket':'交易市场'
	, 'publishname':'行业'
	, 'reportdate':'报告期'
	, 'basiceps':'每股收益(元)'
	, 'cutbasiceps':'每股收益(扣除)(元)'
	, 'totaloperatereve':'营业收入(元)'
	, 'ystz':'营业收入同比增长(%)'
	, 'yshz':'营业收入季度环比增长(%)'
	, 'parentnetprofit':'净利润(元)'
	, 'sjltz':'净利润同比增长(%)'
	, 'sjlhz':'净利润季度环比增长(%)'
	, 'bps':'每股净资产(元)'
	, 'roeweighted':'净资产收益率(%)'
	, 'mgjyxjje':'每股经营现金流量(元)'
	, 'xsmll':'销售毛利率(%)'
	, 'assigndscrpt':'利润分配'
	, 'gxl':'股息率(%)'
	, 'firstnoticedate':'首次公告日期'
	, 'latestnoticedate':'最新公告日期'
	# , 'securitytypecode':''
	# , 'trademarketcode':''	
}
# 业绩报表保存为CSV格式对应列名称
EM_YJBB_CSV_Columns = [
	'股票代码'
	, '股票名称'
	, '股票类别'
	, '交易市场'
	, '行业'
	, '报告期'
	, '每股收益(元)'
	, '每股收益(扣除)(元)'
	, '营业收入(元)'
	, '营业收入同比增长(%)'
	, '营业收入季度环比增长(%)'
	, '净利润(元)'
	, '净利润同比增长(%)'
	, '净利润季度环比增长(%)'
	, '每股净资产(元)'
	, '净资产收益率(%)'
	, '每股经营现金流量(元)'
	, '销售毛利率(%)'
	, '利润分配'
	, '股息率(%)'
	, '首次公告日期'
	, '最新公告日期'
	# , 'securitytypecode':''
	# , 'trademarketcode':''
]