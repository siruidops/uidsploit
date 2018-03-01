import mechanize
import sys
import json

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	try:
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.addheaders = [('User-agent', 'Firefox')]
		res = br.open('http://pubproxy.com/api/proxy').read()
		js = json.loads(res)
		print
		for i in js.keys():
			if i == "data":
				for j in js[i]:
					data = j.iteritems()
					for c,d in data:
						if c == 'support':
							sup = d.iteritems()
							for k,o in sup:
								print brown,k,': ',green,o,end
							continue
						else:
							print brown,c,': ',green,d,end
			else:
				print brown,i,": ",green,js[i],end
		print
	except:
		print
		print red," [-] No Resoult!",end
		print