#!/usr/bin/python
from sys import argv
from bs4 import BeautifulSoup as soup
class protoRes:
	def __init__(self,url,title,anchors,disText,cacheLink):
		if html != None:
			self.html = html
		if url == None:
			self.url = ""
		if title == None:
			self.title = ""
		if anchors == None:
			self.anchors = []
		if disText == None:
			self.disText = []
		if cacheLink == None:
			self.cacheLink = ""
		self.citeURL = ""
		#thats about it for a google page
	def setURL(self,url):
			if url != None:
				self.url = url
	def setTitle(self,title):
			if title != None:
				self.title = title
	def addAnchor(self,anchor):
			if anchor != None and type(str('')) == type(anchor):
				self.anchors.append(anchor)
	def setAnchors(self,url_list):
			for anchor in url_list:
				self.addAnchor(anchor)
	def setTitle(self,title):
			if title != None:
				self.title = title
	def setCacheLink(self,link):
			if link != None:
				self.cacheLink = link
	def setSummary(self,summary):
		if summary != None:
			self.summary = summary
	def setCiteURL(self,url):
		if url != None:
			self.citeURL = url
	def display(self):
		print "{%s" % (self.title)
		if self.url:
			print "\t[%s]" % (self.url)
		if self.summary:
			print "\t[%s]" % (self.summary)
		if self.citeURL:
			print "\t[%s]" % (self.citeURL)
		if self.cacheLink:
			print "\t[%s]}\n" % (self.cacheLink)
		else:
			print "}"
def parseHTML(html):
	#parse an HTML page into a list of result objects, which is simply a neat way of organizing result data
	#psuedo:
	#1:make a blank list/generator
	#2:parse the html to soup
	#3:get the div object holding all the results
	#4:check that the ol tag is present
	#5:make a list of h3 objects
	#6:for item in the h3 object list
		#7:make a blank result object
		#8:for every tag in the object 
			#9:if this is a recognizable attribute
			#10:add it to the the blank result
		#11:add the result object to the list
	#return
	results = [] #:1
	try:
		gooSoup = soup(html)
	except Exception, e:
		print e.meesage
		return
	resultsDivider=gooSoup.find('div',{'id':'ires'}) #:2
	#print resultsDivider
	#for something in resultsDivider:
	#		print "-\n\n",something,"\n\n"
	if len(resultsDivider):
		if resultsDivider.ol: #:4
			oltag=resultsDivider.ol #all the good stuff is kept in this tag
			page_results=oltag.findAll('li',{'class':'g'}) #~:5
			for result in page_results:
				resultObj=protoRes(None,None,None,None,None)
				if result.blockquote:
					result=result.blockquote
				if result.h3:
					h3=result.h3
					anchor=h3.a
					url=anchor.get('href')
					title=anchor.strings
					title=''.join([i for i in title])
					#print ">",url
					resultObj.setURL(url)
					resultObj.setTitle(title)
				if result.div:
					smry=result.div.strings
					displayableString=''.join([string for string in smry])
					resultObj.setSummary(displayableString)
					if result.div.div:
						cached=result.div.div
						if cached.cite:
							urldisplay=cached.cite
							#print "\t%s\n" % (urldisplay)
							resultObj.setCiteURL(urldisplay)
						if cached.span:
							try:
								cacheLink=cached.span.a.get('href')
								resultObj.setCacheLink(cacheLink)
							except TypeError:
								continue
							#print "\t{%s}\n" % (cacheLink)
					#print "\t%s\n\t%s\n" % (urldisplay,cacheLink)
				results.append(resultObj)	
	for result in results:
		result.display()
if __name__=="__main__":
	#need to put on some shoes its f*cking cold!
	#this is a prototype for the results object
	html = open(argv[1],"r")
	parseHTML(html)
