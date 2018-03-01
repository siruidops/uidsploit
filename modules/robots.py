import sys
import urllib

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

def __start__():
	print
	print green+"[-] Please enter url website"
	print "    e.x: [http, https]://example.com"+end
	print
	url = raw_input(brown+'robots_scanner > URL >>> '+end)
	if 'http' in url:
		pass
	else:
		print
		sys.exit()
	print
	for i in search:
		ur = url+'/'+i
		try:
			u = urllib.urlopen(ur)
			if u.code == 200:
				print green+' [+] 200: '+ur+end
			else:
				print brown+' [!] '+str(u.code)+': '+ur+end
		except:
			pass
	print
