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
		import builtwith
	except ImportError:
		print
		print red+"[-] Not found 'builtwith' library"
		print green+"    pip install builtwith"+end
		print
		sys.exit()
	
	print
	print green+"[+] Please enter url webserver"
	print "    e.x: [([http, https]://example.com/), ([http, https]://0.0.0.0/)]"+end
	print
	url = raw_input(brown+'detect_technology > url >>> '+end)
	try:
		b = builtwith.parse(url)
	except:
		print
		print red+"[-] Not found url: "+url+end
		print
		sys.exit()
	print
	for i,j in b.iteritems():
		k = ', '.join(j)
		print brown+'    ',i,': '+green,k,end
	print




