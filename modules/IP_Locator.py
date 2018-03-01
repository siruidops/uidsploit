import sys, urllib

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Please enter domain or ip"
	print "    e.x: [example.com, 0.0.0.0]"+end
	print
	victim = raw_input(brown+'ip_locator > victim >>> '+end)
	url = "http://ip-api.com/json/"+victim
	try:
		u = urllib.urlopen(url).read()
	except:
		print
		print red+"[-] Please enable network"+end
		print
		sys.exit()
	print
	print green+'   '+u+end
	print





	