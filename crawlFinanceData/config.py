# eastmoney data API

# url for KLine data, data from www.eastmoney.com, full_url = KLine_Url+'&id=%s'+'&type=%s' % (id, type)
# id: 6 digits stock code + market code(1 represents sh, 2 represents sz), like '0000012' 
# type: type of kLine, k--day line, wk--week line, mk--month line, m5k--5 minutes line, m30k--30 minutes line, m60k--60 minutes line
EM_KLine_Url = 'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?token=4f1862fc3b5e77c150a2b985b12db0fd&rtntype=6&authorityType=fa&cb=jsonp1539101454906'
# eastmoney market center address
EM_MCenter_Url = 'http://quote.eastmoney.com/center/'
# eastmoney market center home domain
EM_MHome_Url = 'http://quote.eastmoney.com/'

# eastmoney stock today market data
# EM_MToday_Url + ('&cmd=%s' % cmd)
EM_MDNow_Url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery38657&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOIATC&js=({data:[(x)],recordsFiltered:(tot)})&st=(ChangePercent)&sr=-1&p=1&ps=10000&_=1539169823495'
# sh-上证A股，sz-深证A股，hs-沪深A股，xg-新股，zxb-中小板，cyb-创业板，hgt-沪股通，sgt-深股通
EM_MDNow_Cmd = {'sh':'C.2', 'sz':'C._SZAME', 'hs':'C._A', 'xg':'C.BK05011', 'zxb':'C.13', 'cyb':'C.80', 'hgt':'C.BK07071', 'sgt':'C.BK08041'}

EM_Market_Cons = {'sh':'1', 'sz':'2'}