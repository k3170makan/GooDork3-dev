"""
	Handle parsing goo_result object lists into HTML
"""

import urllib

#if a output file was supplied you may dump the results into to, if not please print them out to the screen
#for instructions on how to handle config objects see goo_config
class goo_html:
	def __init__(self,config):
		self.config=config
	def goo2HTML(self,result):  #this one call must see that all parsing is done
		self.result = result
		self.html = open(str(self.config.getOutFile())+str('.html'),'wb')
		self.html.write('<html><body><h1>%s</h1>' % (self.config.getOutFile(),))
		self.html.write('<table border = 1><tr><td><p>Link</p></td> \
			<td><p>Title</p></td> \
			<td><p>Summary</p></td> \
			<td><p>Cache Link</p></td></tr>')
		for item in self.result:
			self.html.write('<tr> \
					<td><a href="%s">%s</a></td>' % (urllib.unquote(item.url).encode("utf-8"), \
						urllib.unquote(item.url).encode("utf-8")) + \
					'<td><p>'+item.title.encode("utf-8")+'</p></td> \
					<td><p>'+item.summary.encode("utf-8")+'</p></td> \
					<td><a href="%s">%s</a></td></tr>' \
					% (urllib.unquote(item.cacheLink).encode("utf-8"),urllib.unquote(item.cacheLink).encode("utf-8")))
		self.html.write('</table></body></html>')
		self.html.close()
		#please cater for a list of results or a single result
		
