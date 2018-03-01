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
	print green+"[+] Please enter IPServer Victim"
	print "    e.x: 0.0.0.0"+end
	print
	IP = raw_input(brown+'host > IP >>> '+end)
	try:
		IP = gethostbyname(IP)
	except:
		print
		print red+"[-] Not found IP address: ",IP,end
		print
		sys.exit()
	HOST = gethostbyaddr(IP)
	print
	for i in HOST:
		if type(i) == str:
			print green+" ",i,end
		else:
			for j in i:
				print green+" ",j,end
	print




