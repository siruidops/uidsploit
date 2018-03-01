from socket import *
import sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+'[+] Please enter IP'
	print '    e.x: [127.0.0.1, localhost]'+end
	print
	IP = raw_input(brown+'PORT_Scan > IP >>> '+end)
	print
	print green+'[+] Please enter range PORT'
	print '    e.x: 5000'+end
	print
	PORT = input(brown+'PORT_Scan > PORT >>> '+end)+1
	try:
		IP = gethostbyname(IP)
	except:
		print
		print red+"[-] Not found IP: "+brown+IP+end
		print
		sys.exit()
	print
	for i in range(0, PORT):
		s = socket(AF_INET, SOCK_STREAM)
		res = s.connect_ex((IP, i))
		try:
			typer = getservbyport(i, 'tcp')
		except:
			typer = 'Unknow'
		if res == 0:
			print green+"[+] PORT {}:{} is open {}".format(i, typer, end)
		else:
			pass
	print