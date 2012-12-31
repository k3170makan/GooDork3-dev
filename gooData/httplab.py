#!/usr/bin/python
#import urllib2 fuck urllib!
import urllib
import httplib
from sys import argv
from bs4 import BeautifulSoup as bsoup
if __name__=="__main__":
	#out = open(argv[1],'w')
	try:
		conn=httplib.HTTPConnection('127.0.1.1') #instantiate object
	except Exception,e:
		print "HTTPConnection call:\n",e
	conn.putrequest('GET',argv[1]) #the search request
	conn.putheader('Accept','text/html') #making sure we get text responses, how about gzip responses?
	conn.putheader('Referer','www.python.org') #randomize referers
	conn.putheader('User-agent','Internet Explorer 6.0')
	print conn.endheaders()
	try:
		resp=conn.getresponse()
	except Exception, e:
		print "getrepsonse():\n",e

	print resp.status,resp.reason
	#swtich statement in python?
	#handle the response status here
	if resp.status == 200:
		#proceed normally
		html = resp.read()
		headers = resp.getheaders()

		for key,value in headers:
			print key,value
		print
		print html
	elif str(resp.status)[0] == "4":
		print "Client error:"
		headers = resp.getheaders()
		for key,value in headers:
			print key,value
		print
	elif str(resp.status)[0] == "5":
		print "Server Error:"
		headers = resp.getheaders()
		for key,value in headers():
			print key,value
		print
