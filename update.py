#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#  This Code Powered By Python 2.7

#
# -------------------------------
#
#       uidsploit - version 3.0
#
#  Developer: Sir uidops
#  E-mail: sir.u1d0p5@gmail.com
#  Github: https://github.com/siruidops/
#
# -------------------------------
#

#
# If you are find a bug please 
#      call with mee
#

#      Copyright for Sir.uidops

#
# If you can help the this project and creat
#      other tool hackings, ...
#      using python version 2
#      please call me ....
#

import sys, os, subprocess, urllib

try:
	c = os.system('clear')
except:
	try:
		c = os.system('cls')
	except:
		pass
version = urllib.urlopen('https://raw.githubusercontent.com/siruidops/uidsploit/master/version.txt').read()
fileO = open('version.txt', 'r')
wersion = fileO.readlines()
fileO.close()
if version == wersion:
	try:
		c = os.system('clear')
	except:
		try:
			c = os.system('cls')
		except:
			pass
	print
	print "[+] This program is update !"
	print
	sys.exit()
else:
	try:
		c = os.system('clear')
	except:
		try:
			c = os.system('cls')
		except:
			pass
	os.chdir('../')
	os.mkdir('uidsploit-%s'%(version))
	subprocess.call(('git', 'clone', url))
	try:
		c = os.system('clear')
	except:
		try:
			c = os.system('cls')
		except:
			pass
	os.chdir('uidsploit-%s'%(version))
	path = os.getcwd()
	print
	print "[+] Updated!"
	print
	print "[*] Saved to {}".format(path)
	print
	sys.exit()
	