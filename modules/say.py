from sys import exit

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	try:
		import pyttsx
	except ImportError:
		print
		print red+"[-] Not found 'pyttsx' library"
		print green+"    pip install pyttsx"+end
		print
		exit()
	print
	print green+"[+] Please Enter Your Text"
	print "    e.x: Hello World"+end
	print
	text = raw_input(brown+"Text_Sound > Text >>> "+end)
	e = pyttsx.init()
	e.setProperty('rate',110)
	e.say(text)
	e.runAndWait()



