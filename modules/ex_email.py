import re, urllib, sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Please enter url page"
	print "    e.x: [http, https]://example.com/ab/about.[aspx, asp, php, html]"+end
	print
	url = raw_input(brown+'email_extract > url >>> '+end)
	try:
		html = urllib.urlopen(url).read()
	except:
		print
		print red+"[-] Not found url: ",url,end
		print
		sys.exit()
	print
	i = re.findall('[.\w]+@[\w.]+', html)
	for j in i:
		print green," ",j,end
	print




