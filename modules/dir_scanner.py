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
	print green+"[+] Please enter webserver"
	print "    e.x: [http, https]://example.com/"+end
	print
	URL = raw_input(brown+'dir_scanner > URL >>> '+end)
	print
	print green+"[+] Please enter file dir"
	print "    e.x: dir.txt"+end
	print
	DIR = raw_input(brown+'dir_scanner > dir_file >>> '+end)
	
	try:
		FILE = open(DIR, 'r')
		FILEword = FILE.readlines()
		FILE.close()
	except:
		print
		print red+"[-] Not found file: {} {}".format(DIR, end)
		print
		sys.exit()
	
	try:
		tr = urllib.urlopen(URL)
	except:
		print
		print red,"[-] Not found url: {} {}".format(URL, end)
		print
		sys.exit()
	
	print
	for i in FILEword:
		i = i.strip()
		url = URL+'/'+word
		u = urllib.urlopen(url)
		if u.code == 200:
			print green+" [*]Sucess!, ",url,end
		else:
			print red+" [-]Incorect!, ",url,end




