import urllib, sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Please enter url webserver"
	print "    e.x: [http, https]://example.com/"+end
	print
	try:
		url = raw_input(brown+'banner-grabbing > url >>> '+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	print
	print blue+"[+] Banner-Grabbing for webserver '{}':{}".format(url, end)
	print
	u = urllib.urlopen(url).headers
	for i, j in u.items():
		print brown+" ",i,' : ',green,j,end
	print