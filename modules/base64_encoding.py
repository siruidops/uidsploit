import sys, base64

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m"

def __start__():
	print
	print green+"[+] Please enter your text"
	print "    e.x: example"+end
	print
	try:
		query = raw_input(brown+'base64_encoding > text >>> '+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	
	hash = base64.b64encode(query)
	
	print
	print brown+"  Text: "+green+query+end
	print brown+"  Base64: "+green+hash+end
	print




