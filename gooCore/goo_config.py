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
"""
class config:
	def __init__(self,options):
		print "1"
		self.options=dict() #this dictionary will tell us whether options were set and the values they were given
		print "2"
		self.given_options = options
		self.regexOptionsList = 'b:a:t:u:s:i:'
		self.configShortOptionsList = 'L:U:'
		self.configLongOptionsList = ['v','in=','out=','format=','passive','active']
		self.bulkModeList = ['site','anchor','link','related']
		#why do it this way? because I want to encourage people to build there own switches later,
		#once the GooDork scripting engine is complete you will be able to add custom switches
		self.longOptionsList = self.configLongOptionsList + self.bulkModeList
		self.shortOptionsList = self.regexOptionsList + self.configShortOptionsList
		self.optionsParsed = self.parseConfig(self.given_options)
		print "3"
		self.hasDork = False
	#validity of the config depends soley on this method (*_*)
	def parseConfig(self,args): #this method takes a list of the switches supplied by the commandline and builds a dictionary
		#if type(args) != type(list): #check that a list was supplied, if not then a .rc file is being read :)
		#	return
		long_opIndex = 1
		if ''.join(args).split('-')[0] == '':
			long_opIndex = 0 #no dork was supplied
			self.hasDork = False
			self.options['hasDork'] = self.hasDork
		else:
			self.hasDork = True
			self.options['hasDork'] = self.hasDork
		try:
			args,opts = gnu_getopt(args,self.shortOptionsList,self.longOptionsList)
		except GetoptError, e:
			print '[goo_config] unknown option(s) were supplied:',e
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
		#check whether this file actually exists
		try:
				with open(file_name) as rcfile:
					rcfile.parse			
		except IOError, e:
			print e
			sys.exit(1)	
		return
	#the next few methods are purely there to be semantic, friendly and to help push the GooDork as an API culture :)
	def setOption(self,keyword,value): #a method to augment the options
		if not (None==keyword or None==key):
			self.options[keyword] = value
		return
	def isPassive(self): #tell the caller if passive mode is on
		try:
			return self.options['passive'] != None
		except KeyError:
			return False
	def hasInFile(self): #tell the caller whether an infile was specified
		try:
			return self.options['in'] != None
		except KeyError:
			return False
	def hasOutFile(self): #tell the caller whether an outfile was specified
		try:
			return self.options['out'] != None
		except KeyError:
			return False
	def outFormat(self): #tell the caller the output format
		try:
			if self.hasOutFile():
				return self.options['format']
			else:
				return False
		except KeyError:
			return False
	def isVerbose(self): #report the verbosity level
		try:
			return self.options['v'] != None
		except KeyError:
			return False
	def hasLimitedResult(self):
		try:
			if self.options['L'] != None:
				return self.options['L']
		except KeyError:
			return False
	def hasBulkMode(self,mode_name): #check whether bulk mode is enabled
		try:
			return self.options[mode_name] != None
		except KeyError:
			return False
	def report(self): #a method I used to help test everything
		for keys in self.options:
			print "%s => %s" % (keys,self.options[keys])
	def checkConfig():
		return True #I'll finish this later, its supposed to audit the config you requested
if __name__ == "__main__":
	conf = config(argv[1:])	
	conf.report()
