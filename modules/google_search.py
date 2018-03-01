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
		from google import search
	except ImportError:
		print
		print red+"[-] Not found 'google' library"+end
		print green+"    pip install google"+end
		print
		sys.exit()
	
	print
	print green+"[+] Please enter query"
	print "    e.x: learn penetration testing"+end
	print
	query = raw_input(brown+'google_search > query >>> '+end)
	try:
		s = search(query)
	except:
		print
		print red+"[-] Please enable network"+end
		print
		sys.exit()
	print
	for i in s:
		print green+'  '+i+end
	print




