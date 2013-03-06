#!/usr/bin/python
#Author: Keith (k3170makan) Makan
#LASTMOD: 

import httplib #needed for making requests
import urllib2
import urllib
import gooLib.goo_config #needed to handle config data
from goo_result import parseHTML 
from goo_result import goo_result 
#import gooData.goo_spoofs as spoofString
#import gooData.goo_servers #needed to bounce between servers
#import gooData.goo_User-Agents #need to randomize user agents
from  sys import stderr #needed to write the verbose content
from sys import argv #needed to test the netlib
"""
	This lil module handles all the HTTP related work
"""
class goo_netlib:
	def __init__(self,config):
		self.config=config #config object
		#self.spoofy=spoofString() #lib that I whipped up to generate random header data
	def gooSearch(self,dork): #run a google search for something
		try:
			httpconn = httplib.HTTPConnection('www.google.co.in')
			#check if the user prefers verbatim mode here
			#print "making connection to google.com"
			start="0"
			query_string = '/search?q='+urllib2.quote(dork)+'&start='+start+'&num=100'
			#print query_string
			httpconn.putrequest('GET',query_string)
			#httpconn.putheader('Referer',self.spoofy.getReferer())
			if self.config.hasUserAgent():
				httpconn.putheader('User-agent',self.config.getUserAgent())
			else:
				httpconn.putheader('User-agent','Internet Explorer 6.0')
			httpconn.putheader('Accept','text/html')
			httpconn.putheader('Connection','close')
			httpconn.endheaders()
		except Exception,e:
			raise Exception("\n[goo_netlib] Problem running dork '%s': %s" % (dork,e))	
		
		resp = httpconn.getresponse()
		status,reason = resp.status,resp.reason
		headers = resp.getheaders()
		print status
		print headers
		if True: #self.config.isVerbose() or True:
			#verbs = int(self.config.getVerbosity())
			verbs = 3
			if verbs >= 2:
				if status != 302:
					stderr.write("[*] Results recived...\n")
				else:
					stderr.write("[!] GooDork is being denied results")
			if verbs == 3:
				stderr.write("%s %s\n" % (status,reason))
				stderr.write("%s" % (headers))
		if status==302:
			return None #no results
		else:
			#build a result object and return it
			html = resp.read()	
			stderr.write("%s" % (html)) # Needed?
			result = parseHTML(html) #returns a list of results
			return result 
	def duckSearch(self,dork):
		return
	def bounceServer(self): #bounce to another google server
		return
	def getPage(self,URL): #do simple get request to the server
		#*need to check that passivity
		if not (self.config.isPassive()):
			url = urlparse.urlsplit(URL)
			try:
				httpconn = httplib.HTTPConnection(url.netloc)
			except Exception, e:
				raise Exception("\n[goo_netlib] Problem creating httplib.HTTPConnection object: "+e)		
				httpconn.putrequest('GET',url.path+"?"+query+"#"+fragment)
				if self.config.hasUserAgent():
						httpconn.putheader("User-agent",self.config.getUserAgent());
				else:
						httpconn.putheader("User-agent","Internet Explorer 6.0");
				"""
				elif self.config.hasUserAgentPreset():
				"""	
				httpconn.putheader("Connection","close")
				httpconn.putheader("Accept","text/html")
			try:
				httpconn.endheaders()
			except Exception, e:
				raise Exception("[goo_netlib] Problem ending http headers" % (e))
			response = httpconn.getresponse()
			status,reason = response.status,response.reason
			if status > 400:
				sys.stderr.write("[*] Page was unavailable...")
				return None
			else:
				headers = response.headers	
				html = response.read()
				if self.config.isVerbose():
					verbs = int(self.config.getVerbosity())
					if verbs >= 2:
						sys.stderr.write("[+] Got response ...")
						sys.stderr.write("%s %s" % (status,reason))
					if verbs == 3:	
						sys.stderr.write("%s" % (headers))
				#build result object
				result = goo_result.parseHTML(result.read())
				result.setHeaders(headers)
				return result
		else:
			#consult the cache:
			result = getCacheResult(URL)	#make sure this returns a result object
			return result
	def getCacheResult(self,URL):
			return 	"" #handle querying the result object
if __name__=="__main__":
	gnet = goo_netlib()
	gnet.getPage("define:k3170makan");
