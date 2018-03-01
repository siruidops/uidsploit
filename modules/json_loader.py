import json, sys, urllib

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print red+"[+] Please enter url json"
	print "    e.x: [http, https]://example.com/uply.json"+end
	print
	js = raw_input(brown+'json_loader > url >>> '+end)
	try:
		u = urllib.urlopen(js).read()
	except:
		print
		print red+"[-] Not found url: ",js,end
		print
		sys.exit()
	try:
		json_data = json.loads(u)
	except:
		print
		print red+"[-] Not Support Json"+end
		print
		sys.exit()
	print
	for i in json_data.keys():
		print brown+i+" : "+green+str(json_data[i])+end
	print





