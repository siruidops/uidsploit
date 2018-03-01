import md5, sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Please enter your hash MD5"
	print "    e.x: 5eb63bbbe01eeed093cb22bb8f5acdc3"+end
	print
	hash = raw_input(brown+'md5_decoding > hash >>> '+end)
	print
	print green+"[+] Please enter a password list"
	print "    e.x: pass.txt"+end
	print
	file = raw_input(brown+'md5_decoding > file >>> '+end)
	try:
		fileOpen = open(file, 'r')
		word = fileOpen.readlines()
		fileOpen.close()
	except IOError:
		print
		print red+"[-] Not cant open password file: ",file,end
		print
		sys.exit()
	for password in word:
		password = password.strip()
		h = md5.md5(password).hexdigest()
		if hash == str(h):
			print
			print green+"[+] Founded!"+end
			print
			print brown+" Hash: ",green,hash,end
			print brown+" Text: ",green,password,end
			print
			sys.exit()
		else:
			print red+"Try: ",password,end






