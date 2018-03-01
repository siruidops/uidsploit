import sys, urllib

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

paths = ['/phpMyAdmin/',
		'/phpmyadmin/',
		'/PMA/',
		'/admin/',
		'/dbadmin/',
		'/mysql/',
		'/myadmin/',
		'/phpmyadmin2/',
		'/phpMyAdmin2/',
		'/phpMyAdmin-2/',
		'/php-my-admin/',
		'/phpMyAdmin-2.2.3/',
		'/phpMyAdmin-2.2.6/',
		'/phpMyAdmin-2.5.1/',
		'/phpMyAdmin-2.5.4/',
		'/phpMyAdmin-2.5.5-rc1/',
		'/phpMyAdmin-2.5.5-rc2/',
		'/phpMyAdmin-2.5.5/',
		'/phpMyAdmin-2.5.5-pl1/',
		'/phpMyAdmin-2.5.6-rc1/',
		'/phpMyAdmin-2.5.6-rc2/',
		'/phpMyAdmin-2.5.6/',
		'/phpMyAdmin-2.5.7/',
		'/phpMyAdmin-2.5.7-pl1/',
		'/phpMyAdmin-2.6.0-alpha/',
		'/phpMyAdmin-2.6.0-alpha2/',
		'/phpMyAdmin-2.6.0-beta1/',
		'/phpMyAdmin-2.6.0-beta2/',
		'/phpMyAdmin-2.6.0-rc1/',
		'/phpMyAdmin-2.6.0-rc2/',
		'/phpMyAdmin-2.6.0-rc3/',
		'/phpMyAdmin-2.6.0/',
		'/phpMyAdmin-2.6.0-pl1/',
		'/phpMyAdmin-2.6.0-pl2/',
		'/phpMyAdmin-2.6.0-pl3/',
		'/phpMyAdmin-2.6.1-rc1/',
		'/phpMyAdmin-2.6.1-rc2/',
		'/phpMyAdmin-2.6.1/',
		'/phpMyAdmin-2.6.1-pl1/',
		'/phpMyAdmin-2.6.1-pl2/',
		'/phpMyAdmin-2.6.1-pl3/',
		'/phpMyAdmin-2.6.2-rc1/',
		'/phpMyAdmin-2.6.2-beta1/',
		'/phpMyAdmin-2.6.2-rc1/',
		'/phpMyAdmin-2.6.2/',
		'/phpMyAdmin-2.6.2-pl1/',
		'/phpMyAdmin-2.6.3/',
		'/phpMyAdmin-2.6.3-rc1/',
		'/phpMyAdmin-2.6.3/',
		'/phpMyAdmin-2.6.3-pl1/',
		'/phpMyAdmin-2.6.4-rc1/',
		'/phpMyAdmin-2.6.4-pl1/',
		'/phpMyAdmin-2.6.4-pl2/',
		'/phpMyAdmin-2.6.4-pl3/',
		'/phpMyAdmin-2.6.4-pl4/',
		'/phpMyAdmin-2.6.4/',
		'/phpMyAdmin-2.7.0-beta1/',
		'/phpMyAdmin-2.7.0-rc1/',
		'/phpMyAdmin-2.7.0-pl1/',
		'/phpMyAdmin-2.7.0-pl2/',
		'/phpMyAdmin-2.7.0/',
		'/phpMyAdmin-2.8.0-beta1/',
		'/phpMyAdmin-2.8.0-rc1/',
		'/phpMyAdmin-2.8.0-rc2/',
		'/phpMyAdmin-2.8.0/',
		'/phpMyAdmin-2.8.0.1/',
		'/phpMyAdmin-2.8.0.2/',
		'/phpMyAdmin-2.8.0.3/',
		'/phpMyAdmin-2.8.0.4/',
		'/phpMyAdmin-2.8.1-rc1/',
		'/phpMyAdmin-2.8.1/',
		'/phpMyAdmin-2.8.2/',
		'/sqlmanager/',
		'/mysqlmanager/',
		'/p/m/a/',
		'/PMA2005/',
		'/pma2005/',
		'/phpmanager/',
		'/php-myadmin/',
		'/phpmy-admin/',
		'/webadmin/',
		'/sqlweb/',
		'/websql/',
		'/webdb/',
		'/mysqladmin/',
		'/mysql-admin/',]

def __start__():
	print
	print green+"[+] Please enter url webserver"
	print "    e.x: [http, https]://example.com"+end
	print
	url = raw_input(brown+'pma_finder > url >>> '+end)
	
	try:
		tu = urllib.urlopen(url)
	except:
		print
		print red+"[-] Not found url: {} {}".format(url, end)
		print
		sys.exit()
		
	print
	for i in paths:
		urlm = url+i
		u = urllib.urlopen(urlm)
		if u.code == 200:
			print green+"[+]Founded!, url: ",brown,urlm,end
		else:
			print red+"[-]NotFound!, url: ",brown,urlm,end
	print

