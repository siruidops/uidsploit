from sys import exit
import time

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	try:
		import autopy
	except ImportError:
		print
		print red+"[-] Not found 'autopy' library"
		print green+"    pip install autopy"+end
		print
		exit()
	print
	print green+"[+] Please enter time(secound) take screenshot"
	print "    e.x: 5"+end
	print
	try:
		rtime = int(raw_input(brown+"screenshot > time >>> "+end))
	except ValueError:
		print 
		print red+"[-] Please enter integer"+end
		print
		exit()
	time.sleep(rtime)
	timer = time.today()
	image = autopy.bitmap.capture_screen()
	name = "screenshot_",timer
	image.save(name)
	print
	print green+"[+] Saved to: ",name,end
	print



