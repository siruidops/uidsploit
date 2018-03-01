import sys, urllib

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	url = "https://api.ipify.org/"
	try:
		u = urllib.urlopen(url).read()
	except:
		print
		print red+"[-] Error!"+end
		print
		sys.exit()
	print
	print brown+"[+] Your IP publick is {} {} {}".format(green, u, end)
	print




