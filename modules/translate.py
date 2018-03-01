# -*- coding: UTF-8 -*-

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

import sys

def __start__():
	try:
		import goslate
	except ImportError:
		print
		print red+"[-] Not found 'goslate' library"+end
		print green+"    pip install goslate"+end
		print
		sys.exit()
	print
	print green+"[+] Please enter your text"
	print "    e.x: hello"+end
	print
	query = raw_input(brown+'translate > text >>> '+end)
	print
	print green+"[+] Please enter your language translate"
	print "    e.x: [fa, en, fr, ...]"+end
	print
	language = raw_input(brown+'translate > language >>> '+end)
	coding = goslate.Goslate()
	dicti = coding.translate(query, language)
	print
	print brown+" language: ",green,language,end
	print
	print green+" ",dicti,end
	print




