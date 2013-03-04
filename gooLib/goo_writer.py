"""
	Handles writing to specific outfile
"""
import goo_csv
import goo_xml
import goo_JSON
import goo_html
from sys import exit
class goo_writer:
	def __init__(self,config):
		self.config = config	
		self.format_funcs = {'csv':goo_csv,'xml':goo_xml,'json':goo_JSON,'html':goo_html} #a little hack to sort out checking, I could write an if statement instead, but thats no fun! >D
		#check that the file doesn't already exists
		try:
				self.outfile = open(self.config.getOutFile(),"w")
		except:	
			print 'and they all fall down...'
			exit(0)	
	def write(self,results):
		if self.config.hasOutFormat():
			#the following is some code that details how the format writing will work, I've commented it out until the depencies have all been coded
			#check the output format
			#for result in results:
				#self.outfile.write("%s\n" % (self.format_funcs[self.config.getOutFormat()].toFormat(result)))
			pass #STUB
		else:
			pass
			#use generic goo_dork format	
		# Writes to specified outfile.
