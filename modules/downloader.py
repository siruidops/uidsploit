import sys,urllib,urlparse,os

end='\033[0m'
yellow='\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
tur="\033[0;36m"
pur="\033[0;35m"

def __start__():
	print
	print green+'[+] Please enter your url file address'
	print '    e.x: [http, https]://example.com/up/file/ex.zip'+end
	print
	url = raw_input(brown+'downloader > URL >>> '+end)
	s = urlparse.urlparse(url).path
	t = s.split('/')
	file = t[len(t)-1]
	try:
		u = urllib.urlopen(url)
		res = u.read()
	except Exception as error:
		print
		print red+' [-] ',error,end
		print
		sys.exit()
	try:
		f = open(file, 'w')
		f.write(res)
		f.close()
	except Exception as error:
		print
		print red+' [-] ',error,end
		print
		sys.exit()
	patho = os.getcwd()+'/'+file
	print
	print yellow+' [+] Success'+end
	print brown+'   Saved To '+green+patho+end
	print



