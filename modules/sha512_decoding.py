import sys, hashlib

def __start__():
	print
	print green+"[+] Please enter your hash sha512"
	print "    e.x: 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f"+end
	print
	hash = raw_input(brown+'sha512_decoding > hash >>> '+end)
	print
	print green+"[+] Please enter a password file"
	print "    e.x: pass.txt"+end
	print
	file = raw_input(brown+'sha512_decoding > file >>> '+end)
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
		h = hashlib.sha512(password).hexdigest()
		if hash == h:
			print
			print green+"[+] Founded!"+end
			print
			print brown+" Hash: ",green,hash,end
			print brown+" Text: ",green,password,end
			print
			break
		else:
			print red+"Try: ",brown,password,end





