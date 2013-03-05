from goo_config import config
from goo_rcfile import goo_rcfile as rcfile #too lazy to fix the name here lols
from goo_netlib import goo_netlib
from goo_result import goo_result as Result
from sys import argv
from goo_writer import goo_writer as writer
import urllib
"""
	The Operator,
		*Handles all netlib calls
		*Handles all urlstripper calls
		*Parses all output to Result objects
		*Handles all reformating of results
The idea with the operator is it runs the inital dork---or grabs the urls from the input file, if a bulk mode has been set---,
once the netlib is done doing all the neccesary networking it returns a goo_results object for the operator to handle.
So now the operator has a list of goo_result objects, it will then proceed to pruning the results in the list named goo_results.results according to the regex options suppled.
Once all the pruning is done it checks the config object for an output file
and dumps the results according to the output format supplied.
"""
#`People say I should follow a coding convention, I say coding conventions should follow me lols'

class Operator:
	def __init__(self,config):#recieves a config object and operates on it
		self.results=[] #this will hold the result objects of whatever needed to be done
		self.config = config
		self.netlib = goo_netlib(config)
		#try: #work the supplied config
		print self.config
		try:
			if self.config: #check that its not None
				if self.config.hasDork(): #check if a dork was supplied
					self.results=self.runDork()
					
					# Move to goo_writer for writing to file.
					if self.config.outFormat():
						self.writer = writer(self.config)
						self.writer.gooWriter(self.results)

					# Else just display.
					else:
						try:
							for reslt in self.results:
								print u'{\n\turl:%s\n\ttitle:%r\n\tsummary:%r\n\tcacheLink:%s\nkeywords:%s\n}' % \
								((urllib.unquote(reslt.url.encode('ascii')), reslt.title, reslt.summary, \
								urllib.unquote(reslt.cacheLink.encode('ascii')), reslt.keyWords))
						except Exception, e:
							print "[!] problem in result repr"
							raise Exception("\n\t[goo_result] Problem printing result:\n\t\t%s" % (str(e),))
					"""
					for result in self.results:
						try:
							print result
						except:
							pass
					"""
				elif self.config.hasBulkMode(): #a bulk mode is being used!
					self.runBulkMode()
				else: #no dork? then it must be a bulk mode!
					raise Exception('[goo_operator] No Bulk Mode supplied in config')
			else:
				raise Exception('[goo_operator] No Config Recieved')
		except Exception,e:
			raise Exception("[goo_operator] Problem with config "+str(e))
			
		# Check if regex switches exist first?
		print "Running Regexes"
		self.runRegex()
	"""
	"""
	def runDork(self):
		#getHTML for a dork and parse it to Result objects
		if self.config and self.config.hasDork():
			try:
				goo_search = self.netlib.gooSearch(self.config.getDork()) #this should return a list of result objects
				#print "\n[goo_search] %s" % (goo_search)
			except Exception,e:
				raise Exception('\n[goo_operator] Problem running google search:\n\t%s, %s' % (str(type(e)),str(e)))
			return goo_search #this is a results object
		else:
			raise Exception('\n[goo_operator] No dork supplied in config')
	"""
		Run the bulk mode supplied for each
	"""
	def runBulkMode(self):
		if self.config and self.config.hasBulkMode():
			try:
				infile=open(self.config.getInfile(),"r")
			except Exception, e:
				raise Exception("\n[goo_operator] Problem Opening Input file:\n\t%s" % (str(e)))
			urls=infile.readlines()
			if len(urls)==0:
				raise Exception('\n[goo_operator] Problem with Input file contents, contains nothing')
			result_list=[]
			results=[]
			bulkMode=self.config.getBulkMode()
			for url in urls:
				url=url.rstrip('\n')
				if 'site' in bulkMode:
					results+=self.siteMode()
				if 'related' in bulkMode:
					results+=self.relatedMode()
				if 'link' in bulkMode:
					results+=self.linkMode()
				if 'anchor' in bulkMode:
					results+=self.anchorMode()
				results_list+=results
			self.results=results_list
		else:
			raise Exception('\n[goo_operator] No BulkMode name supplied')
	"""
	"""
	def runRegex(self):
		#run supplied regex on the Result 
		return
	"""
	"""
	def ParseOutPut(self):#either return a results object or a list of them or write to the output file
		return
	#Just a thought:
	#{another Idea might be to have the user supply a threshold value, to specify how much of attributes in page
	#should match a given pattern, or how many hits the pattern should get on the page
	#this would make goodork regex insanely accurate and interesting to use in AI projects!
	#***GooDork could then be implemented as part of a machine learning system that builds benchmarks regexs to match
	#cetain pages as accurately as possible!} ---k3170
	"""
		Return Result objects from a given dork
	"""
	def GooSearch(self,search_term):
		#call the netlib's goodork function on a given search term
		return
	#the following all merely filter the list of result objects already returned by the initial netlib call
	"""
		Return A list of Result objects with displayable text that matches `pattern'
	"""	
	def inBody(self,pattern): #return a list of Result Objects that
		try:
			return
		except Exception,e:
			raise Exception("\n[goo_operator] Problem running inBody: %s" % (str(e)))
	"""
		Return a list of Result objects with title text that matches `pattern'
	"""
	def inTitle(self,pattern):
		try:
			return
		except Exception,e:
			raise Exception("\n[goo_operator] Problem running inTitle: %s" % (str(e)))
	"""
		Return a list of Result objects with script tag contents that matches `pattern'
		*this searches all script tags on the page, excluding cross site scripted tags
			and will return the result object if atleast one of them match the pattern
	"""
	def inScript(self,pattern):
		try:
			return
		except Exception,e:
			raise Exception("\n[goo_operator] Problem running inScript: %s" % (str(e)))
	"""
		Return a list of Result objects with Input tags that contain values AND/OR parameter names
		that match `pattern'
			i.e where <input `pattern'=`value' /> || <input parameter=`pattern'/> || <input `pattern'=`pattern'/>

			*this will search through all the input tags on a page and will return the Result Object
			if atleast one of them have values
	"""
	#I should be playing MTG right now lols
	def inInput(self,pattern):
		try:
			return
		except Exception,e:
			raise Exception("\n[goo_operator] Problem running inInput: %s" % (str(e)))
	"""
		Return a list of Result objects with Anchor tags that contain href values that match `pattern'

		*this will search through all the input tags on a page and will return the Result Object
			if atleast one of them have values
	"""
	def inAnchor(self,pattern):
		try:
			return
		except Exception,e:
			raise Exception("\n[goo_operator] Problem running inAnchor: %s" % (str(e)))
	"""
		**a hint at whats next...GooDork regex scripting
		Apply the user supplied logical operators to process regexes
	"""
	#I really need to get going with some compiler design courses!
	#I actually want to turn GooDork into a language or atleast some API
	#that allows you to programatically process results
	#quite powerfull things can be done with just these three BulkModes
	"""
		Run the `site:' directive on each URL supplied by the `in' argument
		*site returns all indexed content from a given domain{path}

		Returns a list of lists of Result objects from this operation
			[[URL 1 related URLS]
			 [URL 2 related URLS]
			...
			 [URL n reltaed URLS] ]
		
		e.g www.google.com/search?q=site:k3170makan.blogspot.com
		will return all indexed pages/resources served from my blog
	**All bulk modes can only be used if an `infile' is supplied
	"""
	def siteMode(self):
		try:
			return
		except Exception, e:
			raise Exception("\n[goo_operator] Problem running siteMode(): "+(str(e)))	
	"""
		Run the `related:' directive on each URL supplied by the `infile' argument
		Returns a list of lists of Result objects from this operation

		e.g www.google.com/search?q=related:k3170makan.blogspot.com
		will return all indexed URLS that are related in content/meta-tags to the supplied argument
	"""
	def relatedMode(self):
		try:
			return
		except Exception, e:
			raise Exception("\n[goo_operator] Problem running relatedMode(): "+(str(e)))	
	"""
		Run the `link:' directive on each URL supplied by the `infile' argument
		Returns a list of lists of Result objects from this operation
	
		e.g ww.google.com/search?q=link:k3170makan.blogspot.com
		will return all URLS that have a link to my blog
	"""
	def linkMode(self):
		try:
			return
		except Exception, e:
			raise Exception("\n[goo_operator] Problem running linkMode(): "+(str(e)))	
	"""
		Run the `anchor:' directive on each URL supplied by the `infile' argument
		Returns a list of lists of Result objects from this operation
	"""
	def anchorMode(self):
		try:
			return
		except Exception, e:
			raise Exception("\n[goo_operator] Problem running anchorMode(): "+(str(e)))	
	"""
		***
	"""
	def combinator(self): #this will later process the logical combinations of the regexes
		return
	#**exprimental
	def RevDNSMode(self): #a little surprise! This will allow you to combined reverse DNS look up with bulk mode results
		return