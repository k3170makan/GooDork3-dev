#!/usr/bin/python
"""
	Handles parsing result object lists into xml files
"""
from sys import *
from string import *
from gooLib.goo_result import *
"""
	parse a goo_result object into an xml file
results look like this:
 43     self.url=''
 44     self.title=''
 45     self.summary=''
 46     self.cacheLink=''
 47     self.keyWords=[]
 48     self.html=''
 49     #get this from the request
 50     self.inputTags=[]
 51     self.scriptTags=[]
 52     self.anchorTags=[]
 53     self.textStrings=[]
 54     self.titleTag=[]
 55     self.header=dict() #headers
--from rc.goo
"""
#tag definitions
result_tagname="result"
resultURL_tagname="url"
resultTitle_tagname="title"
resultSummary_tagname="summary"
resultCacheLink_tagname="cachelink"
resultkeyWords_tagname="keywords"
resultkeyword_tagname="keyword"
resultheaders_tagname="headers"
resultheader_tagname="header"
resultscript_tagname="script"
class goo_xml:
	def __init__(self,config):
		self.config=config	
	def goo2XML(resultObj): #the call that handles it all
		#stub
		return
	def declare_resultFields():
		#stub
		return
	def result_tag(value):
		return "<%s>%s</%s>"  % (result_tagname,value,result_tagname)
	def URL_tag(value):
		return "<%s>%s</%s>" % (resultURL_tagname,value,resultURL_tagname)	
	def title_tag(value):
		return "<%s>%s</%s>" % (resultTitle_tagname,value,resultTitle_tagname)
	def CDATA(value):
		return "<![CDATA[%s]]>" % (value)
	#finish this later
