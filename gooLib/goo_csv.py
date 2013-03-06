"""
	Handle parsing goo_result object lists into a csv
"""
import csv
import urllib

class goo_csv:
	def __init__(self,config):
		self.config = config
	def goo2CSV(self,result):
		self.result = result
		self.gooCSV = csv.writer(open(str(self.config.getOutFile())+str('.csv'),'wb'))
		for item in self.result:
			self.gooCSV.writerow([urllib.unquote(item.url),item.title.encode('utf-8'),item.summary.encode('utf-8'), \
			urllib.unquote(item.cacheLink), item.keyWords])
		#please cater for either a list of results or a single one	