#!/usr/bin/env python
#
# Program Name : Main Menu for SmoothSec
# Script       : smoothsec.menu.py
# Version      : 0.1
# Date         : Sept 14, 2013
# Author       : Samiux (runnersam@gmail.com)
#

import sys,os,subprocess,time,urllib2
from time import *

def internet_check():
  
	if subprocess.Popen("ping -q -c 1 -w 2 www.google.com > /dev/null",shell=True).wait() == 0:
		print "Internet is working!"
	else:
		print "Internet is not working!"
		print "Internet connection is required for this script."
#		print "To continue without internet connectivity comment '#' the function at line 666.\n"
		sys.exit()
		
def clear():
	if subprocess.Popen("clear",shell=True).wait() == 0:
		print ""
	else:
		print "\n"
		print " [>] Failed to clear screen.\n"


#----------------------------------- Update functions!

def debian_update():

	print " [>] Updating and cleaning Debian Server, please wait.\n"
	
	if subprocess.Popen("sudo apt-get -q update && sudo apt-get -y dist-upgrade && sudo apt-get --purge autoremove -y && sudo apt-get -y --purge autoclean && sudo apt-get clean",shell=True).wait() == 0:
		print "\n"
		print " [>] Debian Server updated and cleaned successfully!\n"
	
	else:
		print "\n"
		print " [>] Failed to update Debian Server.\n"

def snort_rules_update():

	print " [>] Updating Snort Rules, please wait.\n"
	
	if subprocess.Popen("sudo smoothsec.snort.rules.update",shell=True).wait() == 0:
		print "\n"
		print " [>] Snort Rules updated successfully!\n"
	
	else:
		print "\n"
		print " [>] Failed to update Snort Rules.\n"


def suricata_rules_update():

	print " [>] Updating Suricata Rules, please wait.\n"
	
	if subprocess.Popen("sudo smoothsec.suricata.rules.update",shell=True).wait() == 0:
		print "\n"
		print " [>] Suricata Rules updated successfully!\n"
	
	else:
		print "\n"
		print " [>] Failed to update Suricata Rules.\n"




#----------------------------------------------- IPS!
	
def ids_standard():

        print " [>] IDS Standard Install, please wait.\n"

	if subprocess.Popen("sudo smoothsec.deploy.standard",shell=True).wait() == 0:
		print "\n"
        	print " [>] IDS Standard Install successfully!  Please reboot!\n"
	
	else: 
		print "\n"
		print " [>] Failed to install IDS Standard.\n"
	
def ids_console():

        print " [>] IDS Console Install, please wait.\n"

	if subprocess.Popen("sudo smoothsec.deploy.console",shell=True).wait() == 0:
		print "\n"
        	print " [>] IDS Console Install successfully!  Please reboot!\n"
	
	else: 
		print "\n"
		print " [>] Failed to install IDS Console.\n"
	
def ids_sensor():

        print " [>] IDS Sensor Install, please wait.\n"

	if subprocess.Popen("sudo smoothsec.deploy.sensor",shell=True).wait() == 0:
		print "\n"
        	print " [>] IDS Sensor Install successfully!  Please reboot!\n"
	
	else: 
		print "\n"
		print " [>] Failed to install IDS Sensor.\n"

#----------------------------------------------- IPS!

def ips_standard():

        print " [>] IPS Standard Install, please wait.\n"

	if subprocess.Popen("sudo smoothsec.deploy.inline.standard",shell=True).wait() == 0:
		print "\n"
        	print " [>] IPS Standard Install successfully!  Please reboot!\n"
	
	else: 
		print "\n"
		print " [>] Failed to install IPS Standard.\n"
	
def ips_console():

        print " [>] IPS Console Install, please wait.\n"

	if subprocess.Popen("sudo smoothsec.deploy.inline.console",shell=True).wait() == 0:
		print "\n"
        	print " [>] IPS Console Install successfully!  Please reboot!\n"
	
	else: 
		print "\n"
		print " [>] Failed to install IPS Console.\n"
	
def ips_sensor():

        print " [>] IPS Sensor Install, please wait.\n"

	if subprocess.Popen("sudo smoothsec.deploy.inline.sensor",shell=True).wait() == 0:
		print "\n"
        	print " [>] IPS Sensor Install successfully!  Please reboot!\n"
	
	else: 
		print "\n"
		print " [>] Failed to install IPS Sensor.\n"
	
#---------------------------------------------------- Utilities!

def switch_engine():

        print " [>] Switching Engine, please wait.\n"

	if subprocess.Popen("sudo smoothsec.switch.engine",shell=True).wait() == 0:
		print "\n"
        	print " [>] Switching Engine successfully!\n"
	
	else: 
		print "\n"
		print " [>] Failed to switch engine.\n"
	
def reset():

        print " [>] Reset to fresh install, please wait.\n"

	if subprocess.Popen("sudo smoothsec.reset",shell=True).wait() == 0:
		print "\n"
        	print " [>] Reset to fresh install successfully!  Please reboot!\n"
	
	else: 
		print "\n"
		print " [>] Failed to reset to fresh install.\n"
	

def script_update():

	print " [>] Updating this script.\n"
	
	subprocess.Popen("wget https://raw.github.com/smoothsec/dev/samiux/afpacket/final-3.4/smoothsec.menu.py -O smoothsec.menu.py.new",shell=True).wait()
	subprocess.Popen("mv smoothsec.menu.py.new smoothsec.menu.py",shell=True).wait()
	subprocess.Popen("chmod a+x smoothsec.menu.py",shell=True).wait()
	subprocess.Popen("mv smoothsec.menu.py /usr/local/sbin/smoothsec.menu",shell=True).wait()
	print "\n"
	print " [>] Update successfully, now please run the script again!\n"
	sleep(2)
	subprocess.Popen("smoothsec.menu",shell=True).wait()
	
def tryharder():

	print "\n"
	print " [>] Wrong choice, try again ... \n"

#----------------------------------- IDS Sub-Menus!

def ids_menu():

	clear()
	header()
	print " IDS Installation Menu\n"
	print " [>] 1. Standard (Web Console + Senors)"
	print " [>] 2. Distributed Console (Web Console only)"
	print " [>] 3. Distributed Sensor (Sensor only)"
	print " [>] A. Switch Detection Engine" 
	print " [>] !?@. Reset to Fresh Install"
	print " [>] x. Exit"

	try:
		choice = raw_input(" [>] Enter your choice: ")
	except KeyboardInterrupt:
		print "\n [>] Exiting!\n"
		sleep(1)
		sys.exit()

	if len(choice) > 4:
		tryharder()
		ids_menu()
	elif choice == "1":
		try:
			ids_standard()
			ids_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "2":
		try:
			ids_dist_console()
			ids_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()			
	elif choice == "3":
		try:
			ids_dist_sensor()
			ids_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "A":
		try:
			switch_engine()
			ids_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "!?@":
		try:
			reset()
			ids_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "x":
		print "\n [>] Exiting!\n"
		sleep(1)
		menu_main()
	else:
		tryharder()
		ids_menu()


#----------------------------------- IPS Sub-Menus!

def ips_menu():

	clear()
	header()
	print " IPS Installation Menu\n"
	print " [>] 1. Standard (Web Console + Senors)"
	print " [>] 2. Distributed Console (Web Console only)"
	print " [>] 3. Distributed Sensor (Sensor only)"
	print " [>] A. Switch Detection Engine" 
	print " [>] !?@. Reset to Fresh Install"
	print " [>] x. Exit"

	try:
		choice = raw_input(" [>] Enter your choice: ")
	except KeyboardInterrupt:
		print "\n [>] Exiting!\n"
		sleep(1)
		sys.exit()

	if len(choice) > 4:
		tryharder()
		ips_menu()
	elif choice == "1":
		try:
			ips_standard()
			ips_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "2":
		try:
			ips_dist_console()
			ips_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()			
	elif choice == "3":
		try:
			ips_dist_sensor()
			ips_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "A":
		try:
			switch_engine()
			ips_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "!?@":
		try:
			reset()
			ips_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "x":
		print "\n [>] Exiting!\n"
		sleep(1)
		menu_main()
	else:
		tryharder()
		ips_menu()


def rules_menu():

	clear()
	header()
	print " Rules Menu\n"
	print " [>] 1. Update Snort Rules"
	print " [>] 2. Update Suricata Rules"
	print " [>] 3. Update Snort and Suricata Rules"
	print " [>] x. Exit"

	try:
		choice = raw_input(" [>] Enter your choice: ")
	except KeyboardInterrupt:
		print "\n [>] Exiting!\n"
		sleep(1)
		sys.exit()

	if len(choice) > 2:
		tryharder()
		rules_menu()
	elif choice == "1":
		try:
			snort_rules_update()
			rules_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "2":
		try:
			suricata_rules_update()
			rules_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()			
	elif choice == "3":
		try:
			snort_rules_update()
			suricata_rules_update()
			rules_menu()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "x":
		print "\n [>] Exiting!\n"
		sleep(1)
		menu_main()
	else:
		tryharder()
		rules_menu()



#----------------------------------- Main Menus!

def header():
  
	print "\n SmoothSec - Intrusion Detection Made Simple"
	print "           http://wwww.smoothsec.org"
	print "       Script Version : 0.1 (Sept 14, 2013)"
	print "\n"

def menu_main():
	
	clear()
	header()
	print "			MAIN MENU\n"
        print " [>] 1. Update and clean Debian Server."
        print " [>] 2. Intrusion Detection (IDS) Installation"
	print " [>] 3. Intrusion Prevention (IPS) Installation"
	print " [>] 4. Update Rules Set"
	print " [>] 5. Update this script."
        print " [>] x. Quit."
	print "\n"

        try:
		choice = raw_input(" [>] Enter your choice: ")
	except KeyboardInterrupt:
		print "\n [>] Exiting!\n"
		sleep(1)
		sys.exit()
	
	if len(choice) > 2:
		tryharder()
		menu_main()
	elif choice == "1":
		try:
			debian_update()
			menu_main()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "2":
		try:
			ids_menu()
			menu_main()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "3":
		try:
			ips_menu()
			menu_main()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "4":
		try:
			rules_menu()
			menu_main()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "5":
		try:
			script_update()
		except KeyboardInterrupt:
			print "\n [>] Exiting!\n"
			sleep(1)
			sys.exit()
	elif choice == "x":
		print "\n [>] Exiting!\n"
		sleep(1)
		sys.exit()
	else:
		tryharder()
		menu_main()


internet_check()
menu_main()
