#!/usr/bin/python
import httplib
from sys import argv
from bs4 import BeautifulSoup as bsoup
def get(host):
	conn=httplib.HTTPConnection(host)
	conn.putrequest('GET','/search?q=define:k3170&start=30')
	conn.putheader('Accept','text/html')
	conn.putheader('User-agent','Internet Explorer 6.0')
	conn.putheader('Referer','www.python.org')
	conn.endheaders()
	resp=conn.getresponse()
	return resp.read()
def results(html):
	res_wrap = None
	res_wrap = bsoup(html).find('div',{'id':'ires'})
	if not (res_wrap):
		raise Exception('Could not parse file')
	if len(res_wrap)==1:
		if res_wrap.ol:
			oltag = res_wrap.ol
			gresults=oltag.findAll('li',{'class':'g'})
			print type(gresults) #ResultSet
			if len(gresults)>=1:
				return gresults
		else:
			raise Exception('No results found!')
	else:
		raise Exception('No results found!')
	return
if __name__=="__main__":
	#html = open(argv[1],'r').read()
	servers = open(argv[1],'r')
	servers = servers.readlines()
	servers = [i.rstrip('search\n').lstrip('http://') for i in servers]
	for host in servers:
		host = host.rstrip('/')
		print "running search for :",host
		f = open(host+'.res',"w")
		print "openend file:",host+'.res'
		html = get(host)
		res = results(html)
		for result in res:
			f.write("%s\n" % (result))
		f.flush()
