#!/usr/bin/python
"""
	An object that handles search results from a google search
k3170
"""
class goo_results:
	def __init__(self):
		self.url='';
		self.title='';
		self.summary='';
		self.cacheLink='';
		self.keyWords=[];
	def getTitle(self):
		return self.title;
	def setTitle(self,mtitle):
		self.title=mtitle

	def getCacheLink(self):
		return self.cacheLink
	def setCacheLink(self,mcache_link):
		self.cacheLink=mcache_link

	def getSummary(self):
		return self.summary
	def setSummary(self,msummary):
		self.summary=msummary

	def getURL(self):
		return self.url
	def setURL(self,mURL):
		self.url=mURL

	def getCacheImages(self):
		return self.cacheLink
	def setCacheImage(self):
		return '';

	def getKeyWords(self):
		return self.keyWords
	def setKeyWords(self,mkeyWords):
		self.keyWords=mkeyWords
