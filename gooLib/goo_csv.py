"""
	Handle parsing goo_result object lists into a csv
"""
class goo_csv:
	def __init__(self,config):
		self.config = config	
	def goo2CSV(self,result):
		#please cater for either a list of results or a single one	
