import sys, time

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	try:
		import pyperclip
	except ImportError:
		print
		print red+"[-] Not found 'pyperclip' library"
		print "    pip install pyperclip"+end
		print
		sys.exit()
	list = []
	while True:
		try:
			if pyperclip.paste() != "None":
				value = pyperclip.paste()
				if value not in list:
					list.append(value)
				else:
					pass
				print brown+str(list)+end
				time.sleep(3)
		except KeyboardInterrupt:
			print
			sys.exit()
	
	
	
	