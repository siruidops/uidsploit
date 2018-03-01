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
	print green+"[+] Please enter your hash sha224"
	print "    e.x: 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b"+end
	print
	hash = raw_input(brown+'sha224_decoding > hash >>> '+end)
	print
	print green+"[+] Please enter a password file"
	print "    e.x: pass.txt"+end
	print
	file = raw_input(brown+'sha224_decoding > file >>> '+end)
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
		h = hashlib.sha224(password).hexdigest()
		if hash == h:
			print
			print green+"[+] Founded!"+end
			print
			print brown," Hash: ",green,hash,end
			print brown," Text: ",green,password,end
			print
			break
		else:
			print red,"Try: ",brown,password,end





