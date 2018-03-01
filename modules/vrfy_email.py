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
		from validate_email import validate_email
	except ImportError:
		print
		print red+"[-] Not found 'validate_email' library"+end
		print green+"    pip install validate_email"+end
		print
		sys.exit()

	def scan(email):
		try:
			is_valid = validate_email(email,verify=True)
		except:
			print
			print red+"[-] please enable network"+end
			print
			sys.exit()
		print
		if str(is_valid).upper() == "TRUE":
			print green+"  [+] Founded!, email: {} {} {} is verify {}".format(brown, email, green, end)
		else:
			print red+"  [-] NotFound!, email: {} {} {} is incorect {}".format(brown, email, red, end)

	print
	print green+"[+] Please enter your type scan"+end
	print brown+"    e.x: [file, mail]"
	print "    file => a file to scan"
	print "    mail => a mail to scan"+end
	print
	vrfy = raw_input(brown+'email_verfy >>> '+end)
	if vrfy == 'file':
		print
		print green+"[+] Please enter your email file"
		print "    e.x: email.txt"+end
		print
		file = raw_input(brown+'email_verfy > file >>> '+end)
		try:
			fileO = open(file, 'r')
			word = fileO.readlines()
			fileO.close()
		except:
			print
			print red,"[-] Not found file: ",file,end
			print
			sys.exit()

		for i in word:
			i = i.strip()
			scan(i)
	elif vrfy == 'mail':
		print
		print green+"[+] Please enter your mail"
		print "    e.x: example@ex.com"+end
		print
		mail = raw_input(brown+'email_verfy > mail >>> '+end)
		scan(mail)


