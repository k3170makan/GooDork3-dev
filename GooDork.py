#!/usr/bin/python
#AUTHOR=Keith (k3170makan) Makan
#Main controller for GooDork
try:
	from bs4 import BeautifulSoup as soup
except ImportError:
	import gooLib.getbs4 as getbs4
	print """
* bs4 was not found. Commencing Download and install.
* You may need to re-run GooDork as admin/root if this fails.
"""
	getbs4.download()
	
import sys
from gooLib.goo_config import config as goo_config
from gooLib.goo_operator import Operator 
class gooDork:
	def __init__(self,args):
		#check to see if arguments are being supplied
		if len(args):
			self.conf=goo_config()
			self.conf.parseConfig(args)
		else:
			sys.stderr.write("\n[*] No commandline options supplied, looking for config file...")	
			self.conf=goo_config()
			try:
				with open("rc.goo") as f:
					f.close()
			except IOError,e:
				sys.stderr.write("\n[!] Please supply either a rc.goo file or some commandline arguments for GooDork to work with!")
				usage()
			self.conf.parseRcFile("rc.goo")
		#for key in self.conf.options:
		#	l = len(key)
		#	print key,' '*(7-len(key))+'=>',self.conf.options[key] #print the options neatly, this was used during testing
		self.operator = Operator(self.conf)
def usage():
	print """
./GooDork  -[habtusiLU] | --out=[outputfile] | --v verbosity | --format=output_format | --opmode=operationalmode | --useragent=useragent_string | --site | --anchor | --link | --related | --header
SWITCHES
	REGEX
	-a : anchor regex, apply regex to anchor values
	-b : body regex, apply regex to displayable text
	-t : title regex, apply regex to title tag text
	-u :  url regex, apply regex to url strings
	-s : script regex, apply regex to the contents of script tags 
	-i : input regex, apply regex to the contents of input tags attribute values
	--header : header regex, apply regex to response headers returned e.g --header "Set-Cookie: auth=admin, password=1234; httpOnly"

	BULK MODES:
		these options requrie a list of URLs as input, supplied via the '--in' switch
		--site   : run the site dork on each value in the URL list
		--anchor : run the 'anchor:' dork on a list of urls
		--link   : run the 'link:' dork on a list of urls
		--related: run the 'related:' dork on a list of urls
	CONFIG
		-L : limit the amount of resuls processed
		-U : add a custom user-agent
		--useragent use a predefined user agent
	INPUT-OUTPUT
		--in : supply an input file of urls to run gooDork on 
		--out: supply a path to an output file, to dump results to 
		--format: supply a format for the output file, default is goodork's
			own output, options include: (XML/CSV/HTML/JSON)
				if there are any other format's you'd like give me a shout ;)	
	MISC
		-v : specify the verbosity level
		-h : display help
	EXAMPLE:
		./GooDork site:*.gov+(~Login|~Admin) -u:(admin|login|config)* -t:(Login|Administration)* --out=government_logins --L 100 --format=CSV

AUTHOR: Keith (k3170) Makan, https://twitter.com/k3170makan
CONTRIBUTORS: 
	Luis (connection) Santana, https://twitter.com/hacktalkblog
	Toufeeq (Ace) Ockards, https://twitter.com/teh_klone
	0xerror, https://twitter.com/0xerror
"""
	
if __name__ == "__main__":
	dork = gooDork(sys.argv[1:])
