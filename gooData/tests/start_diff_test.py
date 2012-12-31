#!/usr/bin/python
import httplib
import re
from sys import argv
from bs4 import BeautifulSoup as bsoup
def get(host):
	conn=httplib.HTTPConnection(host)
	conn.putrequest('GET','/search?q=define:k3170&start=10')
	conn.putheader('Accept','text/html,application/xhtml+xml')
	conn.putheader('DNT','1')
	conn.putheader('User-agent','Internet Explorer 6.0')
	conn.putheader('Referer',host)
	conn.endheaders()
	resp=conn.getresponse()
	return resp.read(),resp.getheaders(),resp.status,resp.reason
def results(html):
	res_wrap = None
	res_wrap = bsoup(html).find('div',{'id':'ires'})
	if not (res_wrap):
		raise Exception('Could not parse file')
	if len(res_wrap)==1:
		if res_wrap.ol:
			oltag = res_wrap.ol
			gresults=oltag.findAll('li',{'class':'g'})
			#print type(gresults) #ResultSet
			if len(gresults)>=1:
				return gresults
		else:
			raise Exception('No results found!')
	else:
		raise Exception('No results found!')
	return
def getPage(host,page):
	conn=httplib.HTTPConnection(host)
	conn.putrequest('GET',page)
	conn.putheader('Referer','www.python.org')
	conn.putheader('Accept','text/html')
	conn.endheaders()
	resp=conn.getresponse()
	return resp.read()
def getCaptcha(URL,ref):
	#print "\tcaptcha@{%s}" % (URL)
	path = re.split("^http://(?:[\w\-_0-9].*?)\.(?:[\w\-_0-9].*?)\.(?:[\w\-_0-9]+)",URL)[1]
	#''.join(re.split('^/sorry/image\?id=',path)).rstrip('&amp;hl=en')
	image_id=1
	host = URL[:len(URL)-len(path)]
	#print "[%s][%s]" % (host,path)
	#print host.lstrip('http://')
	conn=httplib.HTTPConnection(ref)
	conn.putrequest('GET',path)
	conn.putheader('Referer',ref)
	conn.putheader('Accept','text/html')
	conn.putheader('User-agent','Internet Explorer 6.0')
	conn.endheaders()
	resp=conn.getresponse()
	html=resp.read()
	#print html
	#strip image files
	soup=bsoup(html)
	#form=soup.find('form',{'method':'get'})
	#print "---------------"
	#print form
	#print "---------------"
	imgs=soup.find('img')
	#print "---------------"
	print imgs
	#print "---------------"
	return
if __name__=="__main__":
	#html = open(argv[1],'r').read()
	servers = open(argv[1],'r')
	servers = servers.readlines()
	servers = [i.rstrip('search\n').lstrip('http://') for i in servers]
	for index,host in enumerate(servers):
		host = host.rstrip('/')
		#print "..%s" % (host)
		#f = open(host+'.res',"w")
		html,headers,status,reason = get(host)
		try:
			#print "\t",status,reason
			if status==302:
				#for key,value in headers:
				#	print "\t>",key,':',value
				getCaptcha(headers[2][1],host)
			res = results(html)
		except Exception, e:
			#print e
			continue
		print "\t%d: <%s> #[%s]" % (index+1,host,len(res))
