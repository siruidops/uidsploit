import sys, os, urllib
from socket import *

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	try:
		import netifaces
	except ImportError:
		print
		print red+"[-] Not found 'netifaces' library"+end
		print green+"    pip install netifaces"+end
		print
		sys.exit()
	
	url = "https://api.ipify.org/"

	try:
		response = urllib.urlopen(url)
		IpPublick = response.read()
	except:
		IpPublick = "unknow"
	
	path = os.getcwd()
	defaultEncoding = sys.getdefaultencoding()
	encoding = sys.getfilesystemencoding()
	teorder = sys.byteorder
	versionPy = sys.version
	hexVersion = sys.hexversion
	root = os.geteuid()

	if root == 0:
		rootDB = "root"
	else:
		rootDB = "No root"
	
	name = getfqdn()
	server = gethostbyname("localhost")
	platform = sys.platform
		
	interface = netifaces.interfaces()
		
	macLo = netifaces.ifaddresses("lo")
	try:
		macWlan = netifaces.ifaddresses("wlan0")
	except:
		macWlan = "unknow"
	try:
		macEth = netifaces.ifaddresses("eth0")
	except:
		macEth = "unknow"
	try:
		login = os.getlogin()
	except OSError:
		login = "unknow"
	print
	print brown+"\tName Network: "+green+name
	print brown+"\tYour Ip lo: "+green+server
	print brown+"\tPlatform: "+green+platform
	print brown+"\tYour IP Publick: "+green+IpPublick
	print brown+"\tLogin: "+green+login
	print brown+"\tRoot: "+green+rootDB
	print brown+"\tPython Version: "+green+versionPy
	print brown+"\tHex Version: "+green+str(hexVersion)
	print brown+"\tTeorder: "+green+teorder
	print brown+"\tEncoding System: "+green+encoding
	print brown+"\tDefault Encoding: "+green+defaultEncoding
	print brown+"\tPath: "+green+path
	print brown+"\tLo: ",green,macLo
	print brown+"\tWlan0: ",green,macWlan
	print brown+"\tEth0: ",green,macEth,end
	print




