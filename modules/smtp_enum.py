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
	print green+"[+] Please enter IP Server"
	print "    e.x: 0.0.0.0"+end
	print
	IP = raw_input(brown+'Smtp_Enum > Server >>> '+end)
	print
	print green+"[+] Please enter PORT Server"
	print "    e.x: 25"+end
	print
	PORT = raw_input(brown+'Smtp_Enum > PORT >>> '+end)
	print
	print green+"[+] Please enter USER for test"
	print "    e.x: admin"+end
	print
	USER = raw_input(brown+'Smtp_Enum > USER >>> '+end)
	s = socket(AF_INET, SOCK_STREAM)
	try:
		s.connect((IP, PORT))
	except:
		print
		print red+"[-] Not cant connect to ip: {} , port: {} {}".format(IP, PORT, end)
		print
		sys.exit()
	print
	print brown,s.recv(1024)
	print
	s.send('VRFY ',USER)
	print
	print green,s.recv(1024)
	print




