# -*- coding: utf-8 -*-

import StringIO, gzip, alfred, urllib, urllib2, datetime, re,sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

reload(sys) 
sys.setdefaultencoding('UTF-8')
#originQuery = '{query}'
originQuery = '合利屋'
#print theQuery
#theQuery = u'%E5%90%88%E5%88%A9%E5%B1%8B'
theQuery = urllib.quote_plus(originQuery)
#url = 'http://dict-co.iciba.com/api/dictionary.php?key=F8B564ADA8E6D4FCB81ACFF2B0BC5478&w=%s' % theQuery
url = 'http://www.meituan.com/s/?w=%s&mtt=1.index%%2Fchangecity.0.0.i9xsufr8' % theQuery
#print url
request = urllib2.Request(url)
request.add_header('Accept-encoding', 'gzip')
req_open = urllib2.build_opener()
conn = req_open.open(request)
req_data = conn.read()

data_stream = StringIO.StringIO(req_data)
gzip_stream = gzip.GzipFile(fileobj=data_stream)
actual_data = gzip_stream.read()

#p = re.compile(r'.*?\[(?P<source>.*?)\] to \[(?P<dst>.*?)\] .*')
p = re.compile(r'\<h3 class=\"deal-tile__title\"\>.*?\<\/h3\>.*?\<p class=\"deal-tile__detail\"\>.*?\<\/p\>',re.S)
title_re = re.compile(r'.*?\<a href=\"(?P<url>.*?)\".*?title=\"(?P<title>.*?)\".*',re.S)
#dict = ET.fromstring(actual_data)
#poses = dict.findall('pos')
#acceptations = dict.findall('acceptation')
items = p.findall(actual_data)
#print items
results = []

if len(items) > 0 :
	index = 0
	for item in items:
		m = title_re.match(item)
                title = m.group('title')
		url = m.group('url')
                subtitle = 'test'
		aitem = alfred.Item({'uid': index, 'arg' : url}, title, subtitle)
		results.append(aitem)
		index += 1
else :
    aitem = alfred.Item({'uid': 1, 'arg' : 'http://www.meituan.com/'}, 'Not Found', '')
    results.append(aitem)

xml = alfred.xml(results)
alfred.write(xml)
