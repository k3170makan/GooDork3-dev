#!/usr/bin/python
from sys import argv
from bs4 import BeautifulSoup as bsoup
import urllib
"""
	An object that handles results from a google search
	goo_results takes a raw Google HTML page and parses
	it into a Result object---or list of result objects.

	This object can then be further parsed into a full-Result
	object by call the `full-parse' method to fetch all the page details,
	or by calling the appropriate methods.

	When netlib runs a google search it returns a Result object---or 
	a list of them---with the Google related information on web page.
		*URL
		*Summary
		*Matched text
		*Summary
		*Cache link
		*etc

	netlib --[HTML]--> Result ----> Operator ----> GooDork ---> output
	
	goo_results objects can be used in 2 ways:
		1) as a way to manage results from a google search
		and/or
		2) as a way to manage/store details from a google search result
			including:
				*URL
				*Displayable Text
				*Title Text
				*Anchor href values
				*... and more!
	
k3170
"""
class goo_result:
	"""
		html --- the Google 
	"""
	def __init__(self,url,title,summary,cachedLink,citeURL):
		#get this from the supplied google HTML
		self.url=''
		self.title=''
		self.summary=''
		self.cacheLink=''
		self.keyWords=[]
		self.html=''
		#get this from the request
		self.inputTags=[]
		self.scriptTags=[]
		self.anchorTags=[]
		self.textStrings=[]
		self.titleTag=[]
		self.header=dict() #headers
	def __repr__(self):
		try:
			return u"{\n\turl:%s\n\ttitle:%r\n\tsummary:%r\n\tcacheLink:%s\nkeywords:%s\n}" % (
					urllib.unquote(self.url.encode('ascii')),
					self.title,
					self.summary,
					urllib.unquote(self.cacheLink.encode('ascii')),
					self.keyWords)
			# Some titles/summaries may contain code that the terminal is not capable of displaying (For eg; UTF in cmd). 
			# Titles/summaries have to be printed raw.
		except Exception, e:
			print "[!] problem in result repr"
			raise Exception("\n\t[goo_result] Problem printing result:\n\t\t%s" % (str(e),))
	"""
		Return the Title
	"""
	def getTitle(self):
		return self.title
	def setTitle(self,mtitle):
		self.title=mtitle
	"""
		Return the Cache link
	"""
	def getCacheLink(self):
		return self.cacheLink
	def setCacheLink(self,mcache_link):
		self.cacheLink=mcache_link

	def getCiteURL(self):
		return self.citeURL
	def setCiteURL(self,mcite_url):
		self.citeURL=mcite_url
	"""
		Return the Content Summary
	"""
	def getSummary(self):
		return self.summary
	def setSummary(self,msummary):
		self.summary=msummary
	"""
		Return the URL
	"""
	def getURL(self):
		return self.url
	def setURL(self,mURL):
		self.url=mURL
	"""
		Return the Cached Image of the Page XDDD
	"""
	def getCacheImages(self):
		return self.cacheLink
	def setCacheImage(self):
		return ''

	def getKeyWords(self):
		return self.keyWords
	def setKeyWords(self,mkeyWords):
		self.keyWords=mkeyWords
	def getHeaders(self):
		return self.headers
	def setHeaders(self,headers):
		self.headers=headers
"""
		Parse Google HTML into workable Result object attributes
	"""
def parseHTML(html):#parse a google page into result objects
	#netlib calls this before return its results
	results = [] #list of result objects
	if html==None:
		#then work with `self.gooHTML'
		return []
	else:
		#use `html'
		#okay off to the lab, gotta whip up a small script to get this going
		#need to check that the ires div is available on the page
		resDiv = bsoup(html).find('div',{'id':'ires'})
		resultTags = ""
		try:
			if resDiv.ol:
				#we know that the ol tag is available
				resultTags = resDiv.ol.findAll('li',{'class':'g'})
			if len(resultTags) > 0:
				for result in resultTags:
					resultObj = goo_result(None,None,None,None,None)
					#a couple of things could be in each result tag
					#just realized GooDork would make an awesome browser extension!
					if result.blockquote: #sometimes results are grouped together using this tag
						result=result.blockquote
					if result.h3: #the link to the actual page sits in this tag, with the title of the page
						h3=result.h3
						if h3.a:
							href=h3.a.get('href')
							href=str(href[7:].split("&sa=")[0])
							title=''.join([string for string in h3.a.strings])
							resultObj.setURL(href)
							resultObj.setTitle(title)
					if result.div: #some extra's, possibly containing the cache link, image or summary	
							summary=''.join([string for string in result.div.strings])
							resultObj.setSummary(summary)
							if result.div.div: #contains the cache link
								cached=result.div.div
								if cached.cite:
									citeURL=''.join([ string for string in cached.cite.strings ])
									resultObj.setCiteURL(citeURL)
								if cached.span:
									if cached.span.a:
										#here lies the cached link
										cacheLink=cached.span.a.get('href')
										resultObj.setCacheLink(cacheLink[2:])
					results.append(resultObj)
				return results
			else:
				return [] #no results could be found
		except Exception, e:
				raise Exception("\n\t\t[goo_result] Problem parsing Google Search page:\n\t\t%s" % (e))
	return
#this next section was used during testing
if __name__ =="__main__":
	f = open(argv[1],"r").read()
	results=parseHTML(f)
	for result in results:
		try:
			print result	
		except Exception,e:
			print e
