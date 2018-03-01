import sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	try:
		import whois
	except ImportError:
		print
		print red+"[-] Not found 'python-whois' library"
		print green+"    pip install python-whois"+end
		print
		sys.exit()
	
	print
	print green+"[+] Please enter domain"
	print "    e.x: example.com"+end
	print
	domain = raw_input(brown+'whois > Doamin >>> '+end)
	try:
		res = whois.whois(domain)
	except:
		print
		print red+"[-] Not found domain: "+domain+end
		print
		sys.exit()
	print
	for i,j in res.iteritems():
		print brown+'     ',i,end,':',green,j,end
	print







		