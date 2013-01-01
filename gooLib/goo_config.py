#!/usr/bin/python
from sys import argv
from sys import exit
import goo_rcfile
from getopt import gnu_getopt,getopt,GetoptError
#try:
#	from getopt import gnu_getopt,getopt,GetoptError
#except ImportError,e:
#	print "Problem Importing getopt: %s" % (e)
#	sys.exit(1)
"""
	The Config object

	An object is used to communicate the configuration properties supplied when GooDork was invoked
	The reason this is a dedicated class, is so that gooDork can omit and add options when the supplied
	configuration is wacky 0_o
	
	Add options that benefit the detection of mixed scripting and mixed display
*So far this object is up and running so if you make changes and wish to commit please keep it in this condition!
"""
class config:
	def __init__(self):
		#print "1"
		self.options=dict() #this dictionary will tell us whether options were set and the values they were given
		#print "2"
		#self.given_options = options
		self.regexOptionsList = 'b:a:t:u:s:i:c:l'
		self.configShortOptionsList = 'L:U:'
		self.configLongOptionsList = ['v','in=','out=','format=','opmode','useragent']
		self.bulkModeList = ['site','anchor','link','related']
		#why do it this way? because I want to encourage people to build there own switches later,
		#once the GooDork scripting engine is complete you will be able to add custom switches
		self.longOptionsList = self.configLongOptionsList + self.bulkModeList
		self.shortOptionsList = self.regexOptionsList + self.configShortOptionsList
		#self.optionsParsed = self.parseConfig(self.given_options)
		#print "3"
		self.rcfile = None
	#validity of the config depends soley on this method (*_*)
	def parseConfig(self,args): #this method takes a list of the switches supplied by the commandline and builds a dictionary
		#if type(args) != type(list): #check that a list was supplied, if not then a .rc file is being read :)
		#	return
		long_opIndex = 1
		if ''.join(args).split('-')[0] == '':
			long_opIndex = 0 #no dork was supplied
			self.options['hasDork'] = False 
		else:
			self.options['hasDork'] = True 
		try:
			args,opts = gnu_getopt(args,self.shortOptionsList,self.longOptionsList)
		except GetoptError, e:
			raise Exception('[goo_config] unknown option(s) were supplied: '+str(e))
			return False #problem with the options supplied
		#okay now I need to parse this to a dictionary
		for index,arg in enumerate(args):	
			if arg[1] != '': #if the thingy has a non-empty string arg, then we are working with a short option
				self.options[arg[0].replace('-','')]=arg[1]
				#print arg[0],':<',self.options[arg[0].replace('-','')],'>'
			else: #I'm assuming that the latter case is a long option
				self.options[arg[0].replace('-','')]=opts[long_opIndex]
				long_opIndex+=1
				#print arg[0],':<',self.options[arg[0].replace('-','')],'>'
		return True
	#see the goo_rgfile module
	def parseRcFile(self,file_handle):
		#method that handles the .rc file parsing
		self.rcfile=goo_rcfile.goo_rcfile(file_handle)
		self.options=self.rcfile.parsefile()
		return self.options
	#the next few methods are purely there to be semantic, friendly and to help push the GooDork as an API culture :)

	def setOption(self,keyword,value): #a method to augment the options
		if not (None==keyword or None==key):
			self.options[keyword] = value
		return

	def hasDork(self):
		return self.options.has_key('dork')
	def getDork(self):
		if self.hasDork():
			return self.options['dork']
		else:
			raise Exception('\n[goo_config] No dork was supplied')

	def hasInBody(self):
		return self.options.has_key('b')
	def getInBody(self):
		if self.hasInBody():
			return self.options['b']
		else:
			raise Exception('\n[goo_config] No regex was supplied for "inbody"')
	
	def hasInTitle(self):
		return self.options.has_key('t')
	def getInTitle(self):
		if self.hasInTitle():
			return self.options['t']
		else:
			raise Exception('\n[goo_config] no regex was supplied for "inTitle"')
	def hasInURL(self):
		return self.options.has_key('u')
	def getInURL(self):
		if self.hasInURL():
			return self.options['u']
		else:
			raise Exception('\n[goo_config] no regex was supplied for "inURL"')
	def hasInAnchor(self):
		return self.options.has_key('a')
	def getInAnchor(self):
		if self.hasInAnchor():
				return self.options['a']	
		else:
			raise Exception('\n[goo_config] no regex was supplied for "inAnchor"')
	def hasInScript(self):
		return self.options.has_key('s')
	def getInScript(self):
		if self.hasInScript():
			return self.options['s']
		else:
			raise Exception('\n[goo_config] no regex was supplied for "inScript"')
	def hasInInput(self):
		return self.options.has_key('i')
	def getInInput(self):
		if self.hasInInput():
			return self.options['i']
		else:
			raise Exception('\n[goo_config] no regex was supplied for "inInput"')
	#def hasInStyle(self):
	#def getInStyle(self):
	#def hasInLink(self):
	#def getInLink(self):
	def isPassive(self): #tell the caller if passive mode is on
		return self.options.has_key('passive')

	def hasInFile(self): #tell the caller whether an infile was specified
		return self.options.has_key('in')
	def getInFile(self):
		return self.options['in']

	def hasOutFile(self): #tell the caller whether an outfile was specified
		return self.options.has_key('out')
	def getOutFile(self):
		return self.options['out']

	def outFormat(self): #tell the caller the output format
		if self.hasOutFile():
			return self.options.has_key('format')
	def getOutFormat(self):
			return self.options['format']

	def isVerbose(self): #report the verbosity level
		return self.options.has_key('v')
	def getVerbosity(self):
		return self.options['v']

	def hasLimitedResult(self):
		return self.options.has_key('L')
	def getResultLimit(self):
		return self.options['L']

	def hasBulkMode(self,mode_name): #check whether bulk mode is enabled
		return self.options.has_key(mode_name)
	def getBulkMode(self):
		"""
			['site','anchor','link','related']
		"""
		bulkmodes = []
		if self.hasBulkMode('site'):
				bulkmodes.append('site')
		if self.hasBulkMode('anchor'):
				bulkmodes.append('anchor')
		if self.hasBulkMode('link'):
				bulkmodes.append('link')
		if self.hasBulkMode('related'):
				bulkmodes.append('related')
		return bulkmodes
	def hasUserAgent(self):
		return self.options.has_key('useragent')
	def getUserAgent(self):
		return self.options['useragent']
	def report(self): #a method I used to help test everything
		for keys in self.options:
			print "%s => %s" % (keys,self.options[keys])
	def checkConfig(self,path):
		rcfiledict = goo_rcfile.goo_rcfile(path)
		return rcfiledict.parsefile()
	def __repr__(self):
		outstring= "\n"
		for key,value in enumerate(self.options):
			outstring+= "[%s]: %s\n" % (value,self.options[value])
		return outstring
if __name__ == "__main__":
	conf = config()	
	config = conf.checkConfig(argv[1])

