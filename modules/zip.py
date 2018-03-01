import sys, zipfile

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Pleade enter zip file"
	print "    e.x: test.zip"+end
	print
	zip = raw_input(brown+"Zip > ZipFile >>> "+end)
	print
	print green+"[+] Pleade Enter Passwd File"
	print "    e.x: pass.txt"+end
	print
	passwd = raw_input(brown+"Zip > PassFile >>> "+end)
	try:
		passwdOPEN = open(passwd, "r")
		passwdWORD = passwdOPEN.readlines()
		passwdOPEN.readlines()
	except IOError:
		print
		print red+"[-] Not Found Password File: "+passwd+end
		print
		sys.exit()
	try:
		archive = zipfile.ZipFile(zip)
	except:
		print
		print red+"[-] Not Found ZipFile: %s OR Not Support ZipFile: %s %s"%(zip, zip, end)
        print
        sys.exit('\n')
	for password in passwdWORD:
		password = password.strip()
		print brown+"Try: "+password+end
		try:
			archive.extractall(pwd=password)
			print green+"[+] Founded!"+end
			print
			print brown+" ZipFile: "+green+zip+end
			print brown+" Password: "+green+password+end
			print
			sys.exit()
		except:
			pass