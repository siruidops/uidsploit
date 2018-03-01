import sys, hashlib

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
	query = raw_input(brown+'sha256_encoding > text >>> '+end)
	
	hash = hashlib.sha256(query).hexdigest()
	
	print
	print brown+" Text: "+green+query+end
	print brown+" SHA256: "+green+hash+end
	print




