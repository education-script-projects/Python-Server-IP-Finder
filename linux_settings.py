#!/usr/bin/env Python
#-*- coding: utf-8 -*-

from __future__ import division

#########################################################
#      FREERADIUS USERS SETTINGS - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################

import os
import sys
import math
import socket

#################################################################
linux_settings = """ 
                     _     ___ _   _ _   ___  __
                    | |   |_ _| \ | | | | \ \/ /
                    | |    | ||  \| | | | |\  / 
                    | |___ | || |\  | |_| |/  \ 
                    |_____|___|_| \_|\___//_/\_\            
            ____  _____ _____ _____ ___ _   _  ____ ____  
           / ___|| ____|_   _|_   _|_ _| \ | |/ ___/ ___| 
           \___ \|  _|   | |   | |  | ||  \| | |  _\___ \ 
            ___) | |___  | |   | |  | || |\  | |_| |___) |
           |____/|_____| |_|   |_| |___|_| \_|\____|____/      
	
    #########################################################
    #            LINUX  SETTINGS - GH0ST S0FTWARE           #
    ######################################################### 
    #                       CONTACT                         #
    #########################################################
    #              DEVELOPER : İSMAİL TAŞDELEN              #                       
    #        Mail Address : pentestdatabase@gmail.com       #
    # LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
    #           Whatsapp : + 90 534 295 94 31               #
    #########################################################

			1) HOSTNAME SETTINGS
			2) DNS SETTINGS
			3) SOURCES LIST SETTINGS
			4) TERMINAL TEXT SETTINGS
			5) CONTACT
"""
###############################################################
hostname_settings_text = """
#########################################################
#          HOSTNAME SETTINGS - GH0ST S0FTWARE           #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#                  Twitter : @RTiwit                    #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""
###############################################################
dns_settings_text = """
#########################################################
#             DNS SETTINGS - GH0ST S0FTWARE             #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#                  Twitter : @RTiwit                    #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################                                                               
"""
###############################################################
soureslist_settings_text = """
#########################################################
#        SOURCES LIST SETTINGS - GH0ST S0FTWARE         #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#                  Twitter : @RTiwit                    #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################                                                               
"""
###############################################################
contact_text = """
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#                  Twitter : @RTiwit                    #
#           Whatsapp : + 90 534 295 94 31               #
######################################################### 
"""
###############################################################
terminal_settings_text = """
#########################################################
#        TERMINAL TEXT SETTINGS - GH0ST S0FTWARE        #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#                  Twitter : @RTiwit                    #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""
###############################################################
print linux_settings
islem = input("Yapmak İstediğiniz İşlem Numarasını Giriniz : ")
os.system('cls' if os.name == 'nt' else 'clear')
###############################################################
if islem == 1:	
	print hostname_settings_text
	os.system("/etc/hostname")
	hostname = raw_input("Yeni hostname adinizi giriniz : ")
	hostnamefile = open("/etc/hostname", "w")
	hostnamefile.write(hostname)
	loading = "New hostname setting saved... ( Loading... %100 )"
	print loading
	hostnamefile.close()
###############################################################
if islem == 2:
	print dns_settings_text
	os.system("/etc/resolv.conf")
	dns = raw_input("Bir dns adresi giriniz : ")
	dnsfile = open("/etc/resolv.conf", "w")
	dnsfile.write("# Generated by NetworkManager" "\n"+ "nameserver" + " " + dns )
	loading = "New dns setting saved... ( Loading... %100 )"
	print loading
	dnsfile.close()
###############################################################
if islem == 3:
	print soureslist_settings_text
	os.system("/etc/apt/sources.list")
	source_name = raw_input("Kaynak icin bir isim belirleyiniz : ")
	source = raw_input("Bir kaynak giriniz : ")
	source_file = open("/etc/apt/sources.list", "a")
	source_file.write("\n" + "#" + source_name + "\n" + source)
	loading = "New source list setting saved... ( Loading... %100 )"
	print loading
	source_file.close()
###############################################################
if islem == 4:
	print terminal_settings_text
	os.system("/etc/bash.bashrc")
	terminal_text = raw_input("Ternimal yazisi icin bir isim belirleyiniz : ")
	terminal_text_settings_file = open("/etc/bash.bashrc", "a")
	terminal_text_settings_file.write("\n" + "clear" + "\n" + "figlet" + " " + terminal_text)
	loading = "New terminal text setting saved... ( Loading... %100 )"
	print loading
	terminal_text_settings_file.close()
###############################################################
if islem == 5:
	print contact_text
###############################################################
