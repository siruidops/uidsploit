import sys
from socket import *

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m"

def __start__():
	print
	print green+"[+] Please enter domain"
	print "    e.x: example.com"+end
	print
	domain = raw_input(brown+'ip > domain >>> '+end)
	try:
		ip = gethostbyname(domain)
	except:
		print
		print red+"[-] Not found domain: "+domain+end
		print
		sys.exit()
	print
	print green+'   '+ip+end
	print




