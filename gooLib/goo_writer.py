"""
	Handles writing to specific outfile
"""
from goo_csv import goo_csv
import goo_xml
import goo_JSON
import goo_html
from sys import exit
class goo_writer:
	def __init__(self,config):
		self.config = config	
		self.format_class = {'csv':goo_csv,'xml':goo_xml,'json':goo_JSON,'html':goo_html}
		#a little hack to sort out checking, I could write an if statement instead, but thats no fun! >D
		# ^ hack doesn't work. It'll open it even if it exists (no exception thrown).

		# Former hack:
		# try:
		# 		self.outfile = open(self.config.getOutFile()+'.'+self.config.getOutFormat().lower(),"w")
		# except:	
		# 	print 'and they all fall down...'
		# 	exit(0)

	def write(self,results):
		if self.config.outFormat():
			format = self.config.getOutFormat().lower()
			if format == 'csv':
				self.csv = goo_csv(self.config)
				self.csv.goo2CSV(results)
			# Cover for the rest of the formats..

		else:
			pass
			#use generic goo_dork format	
		# Writes to specified outfile.
