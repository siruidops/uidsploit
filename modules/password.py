import random, string, sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	char = string.ascii_letters + string.punctuation + string.digits
	password = "".join(random.choice(char) for x in range(random.randint(8,16)))
	print
	print brown+"[+] Your password:"
	print "  ",password,end
	print



