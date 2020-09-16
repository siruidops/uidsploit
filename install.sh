#!/bin/bash
# -*- coding: UTF-8 -*-

# This Code Powered By Bash

#
# -------------------------------
#
#       uidsploit(uidops) v 3.0
#
#  Developer: Sir uidops
#  E-mail: sir.u1d0p5@gmail.com
#  Github: https://github.com/siruidops/
#
# -------------------------------
#

#
# If you are find a bug please 
#        call with mee
#

# Copyright for Sir uidops

#
# If you can help the this project and creat
#   other tool hackings, ...
#   using python version 2 or 3
#   please call me ....
#


echo
echo "--- \033[33m welcome to uidsploit v3 install \033[0m ---"
echo
echo " 0) exit"
echo " 1) install"
echo " 2) uninstall"
echo
read -p " your choice [1-2] 0 for exit: " pil;
case $pil in
1)
sudo pip2 install -r requirements.txt
echo
clear
cp run.sh /usr/bin/uidsploit
mkdir -p /opt/uidsploit
mkdir -p /opt/uidsploit/core
cp -R modules/ /opt/uidsploit/
cp uidsploit.py /opt/uidsploit/
cp version.txt /opt/uidsploit/
cp log.txt /opt/uidsploit/
chmod +x /usr/bin/uidsploit
chmod +x /opt/uidsploit/uidsploit.py
echo
echo "uidsploit installed!"
echo "   run using \"uidsploit\" command"
echo

;;
2)
clear
echo 
echo " [*] Uninstalling ..."
echo
rm -irf /opt/uidsploit/
rm /usr/bin/uidsploit
sleep 5s
echo
echo " [*] Uninstalled !"
echo
;;
0)
exit 0
;;
esac


