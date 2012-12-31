#!/usr/bin/python
#AUTHOR=Keith (k3170) Makan
#DATE=
import re
import sys
#Later on we could try different file formats for rc.goo
"""
This object handles parsing GooRC files, and parses them into goo_config objects

[!] At the time of writing this doc string the goo_rcfile script was working so if you wish to contribute please make sure that all you commits include a working version of this file.
*the following symbols are used to inidicate extra information about the file format
*none of them are to be used as in the specification
{} means optional, everything described in the brackets is an optional requirement
[] means required, everything described int the braces is a required input
|  means OR

The gooDork .rc file format

filename: .goorc <--- the file you want goodork to use as an rc file must have this name!
-------------------------------
#GooDork //marker 
{#gdork [search terms]}
{#regex
	{@Body: [regex]}
	{@Anchors: [regex]}
	{@Text: [regex]}
	{@Url: [regex]}
	{@Script: [regex]}
	{@InputTag: [regex]}     
}
{#confg
	{@inputfile: [path to file]} 
	{@outputfile: [path to file]}
	{@outputformat: [goo|xml|csv|json|...]}
	{@operationalMode: [passive|active]}		
}
-------------------------------
*All white space chars are optional except for '\n' chars which are a must for terminating directives arguments!
*a directive tag anme always with a @
*a directive tag name always ends with a :, this marks the start of the corresponding argument

Directive Tags:
	[@name:]{whitespace}[argument\n]
Section Tags:
	[.name]{whitespace}\n
"""
class goo_rcfile:
	#Okay I think thats all of the them lols
	def __init__(self,path):
		self.section_TagQualifier="#" #marks the following word as the name of a section
		self.directive_TagQualifier="@" #marks the following word as the name of a directive
		#file section tags
		self.regex_SectionTag="regex"
		self.config_SectionTag="confg"
		self.dork_SectionTag="gdork"
		self.match_SectionTag="match" #making provision for a new functionality I'm thinking of ;)
	#directive tags
		self.body_DirectiveTag="Body"
		self.anchor_DirectiveTag="Anchor"
		self.title_DirectiveTag="Title"
		self.URL_DirectiveTag="URL"
		self.script_DirectiveTag="Script"
		self.input_DirectiveTag="Input"
		self.limit_DirecctiveTag="Limit"
		self.useragent_DirectiveTag="UserAgent"
		self.inFile_DirectiveTag="InFile"
		self.outFile_DirectiveTag="OutFile"
		self.outFormat_DirectiveTag="OutFormat"
		self.opMode_DirectiveTag="OpMode"
		self.configdict = None 
		self.transdict={self.body_DirectiveTag:'b',self.anchor_DirectiveTag:'a',self.title_DirectiveTag:'t',self.input_DirectiveTag:'i',self.script_DirectiveTag:'s',self.URL_DirectiveTag:'u',self.inFile_DirectiveTag:'infile',self.outFile_DirectiveTag:'outfile',self.outFormat_DirectiveTag:'format',self.useragent_DirectiveTag:'U',self.useragent_DirectiveTag:'useragent',self.opMode_DirectiveTag:'opmode'}
		try:
			self.fileObj=open(path,"r")
		except IOError, filebooboo:
			raise Exception('\n[goo_rcfile] gooDork had a file booboo, cannot find '+path)
			return
		self.fileString=self.fileObj.read()
	def tokenize(self): #tokenize into sections and return
		
		if self.fileString and len(self.fileString.split("#"))-1 > 0: #make sure there is atleast one section
			return self.fileString.strip("\n\t").split("#") #i could use a genexp but its not worth it here
		else:
			return None
	"""
		This builds a dictionary to be used by the goo_config class, much the same dictionary thats
		build when commandline options are supplied
	"""
	def parsefile(self): #lets try to keep everything naaaice and clean
		#was watching 'Strange Wilderness' while coding this :)
		sections = self.tokenize()
		if sections:
			section_dict_list = []
			for section in sections: #the first element in the list is usually a blank string
				tempdict = self.parseOptionsForSection(section)
				section_dict_list.append(tempdict) #tempdict = ('section_name',{options dictionary})
			#print "Done building section dictonaries"
			#for section in section_dict_list:
			#	print "...>",section
			final_options=self.buildOptionsDict(section_dict_list)
			self.configdict = final_options
			return self.configdict
		else:	
			raise Exception('\n[goo_rcfile] Parse File error: .rc file has no sections!')
	def parseOptionsForSection(self,section_string): #parse the options for a each section, this builds a dictionary for each one
			tokens=section_string.split('@')
			#print 'tokens,',tokens
			sec_name=tokens[0].lstrip('\n\t') #get the section name
			#print "section name:",sec_name 
			if self.isRegexSection(sec_name): #i should actually check that the regex in the section are valid
					sec_name='regex'
			elif self.isConfigSection(sec_name):
					sec_name='config'
			elif self.isDorkSection(sec_name):
					sec_name='dork'
					#print "DORK SEC TEST:",tokens[0].split(' ')
					return ('dork',tokens[0].split(' ')[1].rstrip('\n\t').lstrip('\n\t'))
			else:
				return None
			_dict = dict()
			tokens = tokens[1:]
			if len(tokens) >= 1:
				for option in tokens:
					opt,arg=option.split(':')
					#print 'opt,arg:',opt,arg
					_dict[opt]=arg.lstrip(' ').rstrip('\n\t')
					if sec_name=='regex':
						try:
							re.compile(_dict[opt])
						except Exception, e:
							raise Exception("\n[goo_rcfile] problem with regex `%s': %s" % (_dict[opt],e.message))
				section_tuple=(sec_name,_dict)
				return section_tuple
			else:
				raise Exception(sec_name+' section has no directives')
				return None
			raise Exception('\n[goo_rcfile] problem parsing '+sec_name+' section')
	def buildOptionsDict(self,dict_list): #build the build the dictionary that goo_config is to use
			final_dict = dict()
			#print "dict_list:",dict_list
			for section_name,opts in dict_list[1:]:
				#print opts
				if type(opts)==type(dict()):
					for key in opts:
						try:
							self.transdict[key]
						except KeyError:
							raise Exception('\n[goo_rcfile] unknown keyword in rcfile: `'+key+'\'')
						final_dict[self.transdict[key]]=opts[key]
				else:
						final_dict['dork']=opts
			return final_dict
	def isRegexSection(self,token):
		stripped=token.rstrip('\n\t')
		#print "stripped:",stripped
		return stripped=='regex'
	def isConfigSection(self,token):
		stripped=token.rstrip('\n\t')
		#print "stripped:",stripped
		return stripped=='config'
	def isDorkSection(self,token):
		stripped=token.split(' ')
		#print "stripped:",stripped
		return stripped[0]=='dork'
