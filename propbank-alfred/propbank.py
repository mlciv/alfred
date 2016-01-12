# -*- coding: utf-8 -*-

import StringIO, gzip, alfred, urllib, urllib2, datetime, re,sys, os
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

reload(sys) 
sys.setdefaultencoding('UTF-8')
originQuery = '{query}'
actual_data = ''
if os.path.exists("index.html"):
   f = open("index.html",'r')
   actual_data =  f.read()
   f.close()

#originQuery = 'ability'
url = 'https://verbs.colorado.edu/propbank/framesets-english/'
if originQuery == "" or actual_data == '':
    if os.path.exists('index.html') :
        os.remove("index.html")
    theQuery = urllib.quote_plus(originQuery)
    request = urllib2.Request(url)
    req_open = urllib2.build_opener()
    conn = req_open.open(request)
    req_data = conn.read()
    data_stream = StringIO.StringIO(req_data)
    actual_data = data_stream.read()
    f = open("index.html",'w')
    f.write(actual_data)
    f.close()

p = re.compile(r'\<a href=\"%s.*?\.html\"\> %s.*?\.html\<\/a\>' % (originQuery,originQuery) ,re.S)
title_re = re.compile(r'.*?\<a href=\"(?P<html>.*?.html).*',re.S)
items = p.findall(actual_data)
results = []

if len(items) > 0 :
	index = 0
	for item in items:
                #print item
		m = title_re.match(item)
		html = m.group('html')
                title = html.split('.')[0]
                subtitle = 'test'
		aitem = alfred.Item({'uid': index, 'arg' : url+html}, title, subtitle)
		results.append(aitem)
		index += 1
else :
	aitem = alfred.Item({'uid': 1, 'arg' : url}, 'Not Found', '')
	results.append(aitem)

xml = alfred.xml(results)
alfred.write(xml)
