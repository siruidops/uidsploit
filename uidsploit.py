#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#
# -------------------------------
#
#       uidsploit - version 3.0
#
#  Developer: uidops
#  E-mail: uidopssu@gmail.com
#  Github: https://github.com/siruidops/
#
# -------------------------------
#

#
# If you are find a bug please 
#      call with mee
#

#      Copyright for uidops

#
# If you can help the this project and creat
#      other tool hackings, ...
#      using python
#      please call me ....
#

# -*- Library -*-
import sys, time, urllib, re, os, subprocess, ssl, smtplib, json
from datetime import datetime

# -*- Core -*-
import core

# -*- Information Gathering -*-
import modules.port as port_scan# Port Scanner
import modules.whois_domain as whois_domain# Whois
import modules.banner as banner# Banner Grabbing
import modules.technology as detect# Detect Technology
import modules.waf as waf# Waf Scanner
import modules.robots as robots# Robots Txt Scanner
import modules.ip as ip# IP Finder
import modules.host as host# host Finder
import modules.ping as ping# Ping
import modules.ex_email as ex_email# Extract E-mail
import modules.vrfy_email as vrfy_email# Verfy Email
import modules.smtp_enum as smtp_enum# SMTP Enum
import modules.dir_scanner as dir_scanner# dir scanner
import modules.pma_finder as pma# PHP MY ADMIN Finder
import modules.ip_publick as ip_publick# Your IP Publcik
import modules.info as info# Info Your System
import modules.google_search as googles# Google Search
import modules.IP_Locator as ipl# IP Locator
import modules.json_loader as js# Json Loader
import modules.paste_jacking as pj# Clipboard Jacking

# -*- Hash Encoding -*-
import modules.binary as binary# Binary
import modules.base64_encoding as base64_e# Base64
import modules.md5_encoding as md5_e# Md5
import modules.sha1_encoding as sha1_e# SHA1
import modules.sha224_encoding as sha224_e# SHA224
import modules.sha256_encoding as sha256_e# SHA256
import modules.sha384_encoding as sha384_e# SHA384
import modules.sha512_encoding as sha512_e# SHA512

# -*- Hash Decoding -*-
import modules.base64_decoding as base64_d# Base64
import modules.md5_decoding as md5_d# Md5
import modules.sha1_decoding as sha1_d# SHA1
import modules.sha224_decoding as sha225_d# SHA224
import modules.sha256_decoding as sha256_d# SHA256
import modules.sha384_decoding as sha384_d# SHA384
import modules.sha512_decoding as sha512_d# SHA512

# -*- Danial of service -*-
import modules.dos as dos# DoS
import modules.ddos as ddos# DDoS
import modules.ddos_router as ddos_r# DDoS Router

# -*- Brute Force -*-
import modules.wordpress as wp# WordPress
import modules.config as config # Config
import modules.smtp as smtp# SMTP
import modules.facebook as facebook# Facebook
import modules.gmail as gmail# Gmail Cracker
import modules.zip as zip# zip

# -*- Others -*-
import modules.goes as goes# Goes
import modules.translate as trans# Translate
import modules.password as passwd# Password Creator
import modules.screenshot as ss# Screenshot
import modules.say as say# Convert text to sound
import modules.proxy as proxy# Get Proxy
import modules.downloader as down# Downloader
import modules.serv as serv# Serv

# -*- Colors -*-
end='\033[0m'
yellow='\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
tur="\033[0;36m"
pur="\033[0;35m"

# -*- Quit -*-
def qu():
	try:
		raw_input(yellow+'[+] Please press enter to show modules ...'+end)
	except KeyboardInterrupt:
		print
		sys.exit()
	program()

# -*- Start Program -*-
def program():
	try:
		c = os.system('clear')
	except:
		try:
			c = os.system('cls')
		except:
			pass
	print
	print green+" -*- uidsploit version 3 -*-"+end
	print
	print green+":: Modules ::"+end
	print 
	print blue+" Information Gathering:"+end
	print brown+"   1) Port Scaner"+end
	print brown+"   2) Whois"+end
	print brown+"   3) Banner Grabbing"+end
	print brown+"   4) Dns Resolver"+end
	print brown+"   5) Detect Technology"+end
	print brown+"   6) Waf Scanner"+end
	print brown+"   7) Robots.txt Scanner"+end
	print brown+"   8) IP Finder"+end
	print brown+"   9) Host Finder"+end
	print brown+"  10) Ping"+end
	print brown+"  11) Extract Email as Webpage"
	print brown+"  12) Email Verfy"
	print brown+"  13) SMTP Enum"
	print brown+"  14) Dir scanner"
	print brown+"  15) phpmyadmin finder"
	print brown+"  16) Your IP Publick"
	print brown+"  17) Info your system"
	print brown+"  18) Google Sesrching"
	print brown+"  19) IP Locator"
	print brown+"  20) Json Loader"
	print brown+"  21) Clipboard Jacking"+end
	print
	print blue+" Hash Encoding:"+end
	print brown+"  22) Binary Encoding"
	print "  23) Base64 Encoding"
	print "  24) MD5    Encoding"
	print "  25) SHA1   Encoding"
	print "  26) SHA224 Encoding"
	print "  27) SHA256 Encoding"
	print "  28) SHA384 Encoding"
	print "  29) SHA512 Encoding"+end
	print
	print blue+" Hash Decoding"+end
	print brown+"  30) Base64 Decoding"
	print "  31) MD5    Decoding"
	print "  32) SHA1   Decoding"
	print "  33) SHA224 Decoding"
	print "  34) SHA256 Decoding"
	print "  35) SHA384 Decoding"
	print "  36) SHA512 Decoding"+end
	print
	print blue+" Danial of service attack:"+end
	print brown+"  37) DoS"
	print "  38) DDoS"
	print "  39) DDos Router (aircrack-ng)"+end
	print
	print blue+" Brute Force:"+end
	print brown+"  40) wordpress "
	print "  41) config "
	print "  42) SMTP"
	print "  43) facebook"
	print "  44) gmail"
	print "  45) zip"+end
	print
	print blue+" Others:"+end
	print brown+"  46) goes"
	print "  47) translate"
	print "  48) password creator"
	print "  49) screenshot"
	print "  50) convert text to sound"
	print "  51) get proxy"
	print "  52) downloader"
	print "  53) serv"+end
	print

	try:
		number = raw_input(tur+'uidsploit > modules > [choice 1 to 50 | 99 for exit] >>> '+end)
	except:
		print
		sys.exit()
	
	if number == '99':
		print
		sys.exit()
		
	#####################
	#####################
	
	elif number == '1':
		try:
			port_scan.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '2':
		try:
			whois_domain.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '3':
		try:
			banner.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '4':
		try:
			try:
				import dns.resolver
			except ImportError:
				print
				print red+"[-] Not found 'dns.resolver' library"+end
				print green+"    pip install dnspython"+end
				print
				sys.exit()
			print
			print green+"[+] Please enter domain"
			print "   e.x: example.com"+end
			print
			domain = raw_input(brown+'dns_resolver > domain >>> '+end)
			print
			print green+"[+] Please enter type scan"
			print "    e.x: [A, MX, NS, ...]"+end
			print
			typer = raw_input(brown+'dns_resolver > type >>> '+end)
			try:
				answers = dns.resolver.query(domain, str(typer))
			except:
				print
				print red+"[-] Not found type or domain"+end
				print brown+" type: "+green+typer+end
				print brown+" domain: "+green+domain+end
				print
				sys.exit()
			print
			print blue+"[+] dns resolver for '{}' : {}".format(domain, end)
			print
			for i in answers.response.answer:
				for j in i.items:
					print green+"  ",j,end
			print
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '5':
		try:
			detect.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################

	#####################
	#####################
	
	elif number == '6':
		try:
			waf.__start__()
		except KeyboardInterrupt():
			print
			sys.exit()
		qu()
		
	#####################
	#####################

	elif number == '7':
		try:
			robots.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()

	#####################
	#####################
	elif number == '8':
		try:
			ip.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '9':
		try:
			host.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '10':
		try:
			ping.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '11':
		try:
			ex_email.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '12':
		try:
			vrfy_email.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()

	#####################
	#####################
	
	elif number == '13':
		try:
			smtp_enum.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()

	#####################
	#####################

	elif number == '14':
		try:
			dir_scanner.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '15':
		try:
			pma.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '16':
		try:
			ip_publick.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '17':
		try:
			info.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '18':
		try:
			googles.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '19':
		try:
			ipl.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '20':
		try:
			js.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '21':
		try:
			pj.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '22':
		try:
			binary.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '23':
		try:
			base64_e.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '24':
		try:
			md5_e.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '25':
		try:
			sha1_e.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################

	elif number == '26':
		try:
			sha224_e.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '27':
		try:
			sha256_e.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '28':
		try:
			sha384_e.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '29':
		try:
			sha512_e.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '30':
		try:
			base64_d.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '31':
		try:
			md5_d.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '32':
		try:
			sha1_d.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '33':
		try:
			sha224_d.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '34':
		try:
			sha256_d.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '35':
		try:
			sha384_d.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '36':
		try:
			sha512_d.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '37':
		try:
			dos.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '38':
		try:
			ddos.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '39':
		try:
			ddos_r.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '40':
		try:
			wp.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '41':
		try:
			config.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '42':
		try:
			smtp.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '43':
		try:
			facebook.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '44':
		try:
			gmail.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '45':
		try:
			zip.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '46':
		try:
			goes.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '47':
		try:
			trans.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '48':
		try:
			passwd.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '49':
		try:
			ss.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '50':
		try:
			say.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()
	
	#####################
	#####################
	
	elif number == '51':
		try:
			proxy.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()

	#####################
	#####################
	
	#####################
	#####################
	
	elif number == '52':
		try:
			down.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()
		qu()

	#####################
	#####################

	#####################
	#####################
	
	elif number == '53':
		try:
			serv.__start__()
		except KeyboardInterrupt:
			print
			sys.exit()

	else:
		try:
			print
			raw_input(red+"[-] Not found your command '{}', Press enter to show modules ...{}".format(number,end))
			print
		except:
			print
			sys.exit()
		program()

# -*- Main -*-
def main():
	print
	hello = yellow+"""
	
             _/      _/                 _/        _/      
                    _/    _/_/_/       _/                _/
     _/  _/ _/ _/_/_/     _/          _/ _/_/_/  _/ _/_/_/_/_/
    _/  _/ _/ _/  _/       _/ _/_/_/ _/ _/   _/ _/     _/
   _/_/_/ _/ _/_/_/   _/_/_/ _/  _/ _/  _/_/_/ _/     _/
                            _/_/_/                   _/
                           _/
                          _/ \033[0;32m version 3.0 \033[33m
                         _/
	"""+end
	print hello
	print
	print brown+"developer: "+green+'sir uidops'+end
	print brown+"e-mail   : "+green+'sir.u1d0p5@gmail.com'+end
	print brown+"github   : "+green+'https://github.com/siruidops/uidsploit/'+end
	print
	print green+" show   "+end+'< show modules'
	print green+" update "+end+'< update uidsploit'
	print green+" exit   "+end+'< exit'
	print
	try:
		res = raw_input(brown+'uidsploit >>> '+end)
	except:
		print
		sys.exit()
	if res == 'show':
		try:
			c = os.system('clear')
		except:
			try:
				c = os.system('cls')
			except:
				pass
		program()
	elif res == 'update':
		try:
			c = os.system('clear')
		except:
			try:
				c = os.system('cls')
			except:
				pass
		version = urllib.urlopen('https://raw.githubusercontent.com/siruidops/uidsploit/master/version.txt').read()
		fileO = open('version.txt', 'r')
		wersion = fileO.readlines()
		fileO.close()
		if version == wersion:
			try:
				c = os.system('clear')
			except:
				try:
					c = os.system('cls')
				except:
					pass
			print
			print "[+] This program is update !"
			print
			sys.exit()
		else:
			try:
				c = os.system('clear')
			except:
				try:
					c = os.system('cls')
				except:
					pass
			os.chdir('../')
			os.mkdir('uidsploit-%s'%(version))
			subprocess.call(('git', 'clone', url))
			cls = os.system('clear')
			os.chdir('uidsploit-%s'%(version))
			path = os.getcwd()
			print
			print "[+] Updated!"
			print
			print "[*] Saved to {}".format(path)
			print
			sys.exit()
	elif res == 'exit':
		print
		sys.exit()
	else:
		main()





# -*- Run Tool -*-
if __name__ == '__main__':
	main()
else:
	print
	sys.exit()


