#!/usr/bin/python
#AUTHOR=Keith (k3170) Makan
#DATE=
import re
import sys
"""
*the following symbols are used to inidicate extra information about the file format
*none of them are to be used as in the specification
{} means optional, everything described in the brackets is an optional requirement
[] means required, everything described int the braces is a required input
|  means OR

The gooDork .rc file format

filename: .goorc <--- the file you want goodork to use as an rc file must have this name!
-------------------------------
#GooDork //marker 
{.dork: [search terms]}
{.regex
	{@Body: [regex]}
	{@Anchors: [regex]}
	{@Text: [regex]}
	{@Url: [regex]}
	{@Script: [regex]}
	{@InputTag: [regex]}     
}
{.config
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
	section_TagQualifier="." #marks the following word as the name of a section
	directive_TagQualifier="@" #marks the following word as the name of a directive
	#file section tags
	regex_SectionTag="regex"
	config_SectionTag="config"
	dork_SectionTag="dork"
	match_SectionTag="match" #making provision for a new functionality I'm thinking of ;)
	#directive tags
	body_DirectiveTag="Body"
	anchor_DirectiveTag="Anchor"
	text_DirectiveTag="Text"
	URL_DirectiveTag="URL"
	inFile_DirectiveTag="InputFile"
	outFile_DirectiveTag="OutputFile"
	outFormat_DirectiveTag="OutputFormat"
	opMode_DirectiveTag="OperationalMode"
	#Okay I think thats all of the them lols
	def __init__(self):
		return
	"""
		this method strips the whitespace chars from the file---except \n---then breaks the file into chunks per
		section, and then returns  a generator of directives to be used by the parsefile method
	"""
	def tokenize(self):
		return
	"""
		This builds a dictionary to be used by the goo_config class, much the same dictionary thats
		build when commandline options are supplied
	"""
	def parsefile(self,path):
		#the existance of the file should have been established
		try:
			with open(path,"r") as rcfile:
				tokens = tokenize(rcfile.read()) #create a list of tuples
				#now we build a goo_config object and send it back
		except IOError,e:
			print e
			sys.exit(1)
		return
	def isRegexSection(self,token):
		return
	def isConfigSection(self,token):
		return
	def isComment(self,token):
		return
	def isDorkSection(self,token):
		return
