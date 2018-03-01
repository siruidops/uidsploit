import sys,subprocess

red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 
tur="\033[0;36m"
yellow="\033[1;33m"
end="\033[1;37m"

def __start__():
	print
	print green+"[+] Please enter url webserver"
	print "    e.x: [http, https]://example.com"+end
	print
	url = raw_input(brown+'waf-scan > url >>> '+end)
	print
	res = subprocess.call(('wafw00f',url))
	print