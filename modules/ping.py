import os, sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Please enter domain or ip"
	print "    e.x: [example.com, 0.0.0.0]"+end
	print
	victim = raw_input(brown+'ping > victim >>> '+end)
	response = os.system("ping -c 1 "+victim)
	if response == 0:
		print
		print green+"[+] Host {} is up {}".format(victim,end)
		print
	else:
		print
		print red+"[-] Host {} is down {}".format(victim,end)
		print



