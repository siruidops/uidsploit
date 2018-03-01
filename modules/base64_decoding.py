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
	print green+"[+] Please enter your base64 encoded"
	print "    e.x: aGVsbG8gd29ybGQ="+end
	print
	try:
		hash = raw_input(brown+'base64_decoding > base64 >>> '+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	try:
		text = base64.b64decode(hash)
	except:
		print
		print red+"[-] Not cant decoding your hash: ",hash,red
		print
		sys.exit()
	print
	print brown,"  Hash: ",green,hash,end
	print brown,"  Text: ",green,text,end
	print




