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
	print green+"[+] Please enter your hash sha1"
	print "    e.x: 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"+end
	print
	hash = raw_input(brown+'sha1_decoding > hash >>> '+end)
	print
	print green+"[+] Please enter a password file"
	print "    e.x: pass.txt"+end
	print
	file = raw_input(brown+'sha1_decoding > file >>> '+end)
	try:
		fileO = open(file, 'r')
		word = fileO.readlines()
		fileO.close()
	except IOError:
		print
		print red+"[-] Not cant open password file: ",file,end
		print
		sys.exit()
	for password in word:
		password = password.strip()
		h = hashlib.sha1(password).hexdigest()
		if hash == h:
			print
			print green+"[+] Founded!"+end
			print
			print brown+" Hash: ",brown,hash,end
			print brown+" Text: ",brown,password,end
			print
			break
		else:
			print red,"Try: ",brown,password,end





