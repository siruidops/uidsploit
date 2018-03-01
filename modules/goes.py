import sys, random

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	ring = 6
	h = random.randint(0, 50)
	print
	print green+"[+] Please enter a integer 0 to 50"
	print "    e.x: 34"+end
	print
	while True:
		ring = ring-1
		if ring == 0:
			print
			print red+"[-] Sorry!"+end
			print
			print brown+" Number: ",green,h,end
			print
			break
		else:
			pass
		num =  input(brown+"goes > number >>> "+end)
		if num == h:
			print 
			print green+"[+] Sucess!"+end
			print
			print brown+" Number: ",green,h,end
			print
			sys.exit()
		elif num > h:
			print
			print blue+"[*] Your number is "+green+"'higth'"+end
			print
		elif num < h:
			print
			print blue+"[*] Your number is "+green+"'Low'"+end
			print
		else:
			pass






		