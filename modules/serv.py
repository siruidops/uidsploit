import sys,socket

end='\033[0m'
yellow='\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
tur="\033[0;36m"
pur="\033[0;35m"

def __start__():
	print
	print green+'[+] Please enter your port or service'
	print '    e.x: [80, www]'+end
	print
	serv = raw_input(brown+'serv > serv >>> '+end)
	print
	try:
		port = int(serv)
		try:
			s = socket.getservbyport(port, 'tcp')
		except:
			s = 'Unknow'
		print brown+' Port: '+green+str(port)+end
		print brown+' Service: '+green+s+end
		print
	except:
		service = str(serv)
		try:
			s = socket.getservbyname(service, 'tcp')
		except:
			s = 'Unknow'
		print brown+' Port: '+green+str(s)+end
		print brown+' Service: '+green+str(service)+end
		print



