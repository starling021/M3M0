import Queue
import argparse
import base64
import binascii
import glob
import hashlib
import json
import marshal
import os
import os.path
import pprint
import random
import re
import requests
import smtplib
import socket
import sqlite3
import string
import sys
import telnetlib
import threading
import time
import urllib
import urllib2
import urlparse
import Queue
from colorama import *
from colorama import Fore, Back, init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from random import choice
from time import strftime
from urllib2 import urlopen
from urlparse import urlparse

init()

la7mar = '\033[91m'
la5dhar = '\033[92m'
ramadi = '\033[90m'
blid = '\033[1m'
star = '\033[4m'
bigas = '\033[07m'
bigbbs = '\033[27m'
hell = '\033[05m'
saker = '\033[25m'
labyadh = '\033[00m'
cyan = '\033[0;96m'


def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 

                   q#p         +-+-+-+-+-+-+-+-+-+
                  N###b        |m|a|r|w|a|n|0|0|7|
                 ####E'        +-+-+-+-+-+-+-+-+-+
                 N###b         
              ,######MN#.
             (N######MN#M     [M3M0]
             ###########R)    1)Reveers Ip
             @###########-    2)cms detector
             N###########p    3)SQLi LFI RFI XSS Scanner
            #############E    4)007Bot (Mass Shell Uploader & Brute)
            N############b    5)Modern login page (Bruteforcer)
           (N############p    6)Mass Upload Shell In Wordpress (user&password)
            NRR########RRE    7)Mass Upload Shell In Joomla (user&password)
            ;@##########M^    8)Mass Wordpress,Joomla,Drupal,Magento& OpenCart (Bruteforcer)
             N#########M#/    9)all Admin Login Bypass & Exploit
             7K###R#R###M7    10)MD5 Ckracker
             (N##M=(N##R-     11)Google Dorcker Bypass Captcha
             #N##-  N##M'     12) Laravel phpunit RCE
             jNRR'  NNNM/     13) vBulletin RCE
             4NRb   'TN#\
             4NN     NNT
              bL     N@
             4pN     b#p,
+-------- [M3M0] Hack Like a Bro Good Luck!! --------+

			                  """
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )


logo()

choice = raw_input( ' choice Number => ' )
if choice == '1':
    print("""\n\033[91m Just select one of the options available in the tool
	and but your domain

 y = yes 
 n = no\033[0m""")
    t = raw_input( '~>' )
    if t == 'y':
        if system() == 'Linux':
            os.system( "cd Tools/tool1 && chmod +x api.py && python2 api.py" )
        if system() == 'Windows':
            os.system( 'cd Tools/tool1 && api.py' )
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')
elif choice == '2':
        print("""\n\033[91m Go to Tools/tool2
        	Put Ur  List of Sites in tool2

         y = yes 
         n = no\033[0m""")
        t = raw_input( '~>' )
        if t == 'y':
            if system() == 'Linux':
                os.system( "cd Tools/tool2 && chmod +x cms.py && python2 cms.py" )
            if system() == 'Windows':
                os.system( 'cd Tools/tool2 && cms.py' )
            else:
                print('unknown error :| ')
        elif t == 'n':
            main()
        else:
            print('unknown error :| ')
elif choice == '3':
            print("""\n\033[91m Go to Tools/tool3 Just But Your Target	
             y = yes 
             n = no\033[0m""")
            t = raw_input( '~>' )
            if t == 'y':
                if system() == 'Linux':
                    os.system( "cd Tools/tool3 && chmod +x exp.py && python2 exp.py" )
                if system() == 'Windows':
                    os.system( 'cd Tools/tool3 && exp.py' )
                else:
                    print('unknown error :| ')
            elif t == 'n':
                main()
            else:
                print('unknown error :| ')
elif choice == '4':
                print("""\n\033[91m Go TO Tools / tool4 andd Add Your List	
                             y = yes 
                             n = no\033[0m""")
                t = raw_input( '~>' )
                if t == 'y':
                    if system() == 'Linux':
                        os.system( "cd Tools/tool4 && chmod +x Bot.py && python2 Bot.py" )
                    if system() == 'Windows':
                        os.system( 'cd Tools/tool4 && run.bat' )
                    else:
                        print('unknown error :| ')
                elif t == 'n':
                    main()
                else:
                    print('unknown error :| ')
elif choice == '5':
                    print("""\n\033[91m Just But The Target Login Page 
                     y = yes 
                     n = no\033[0m""")
                    t = raw_input( '~>' )
                    if t == 'y':
                        if system() == 'Linux':
                            os.system( "cd Tools/tool5 && chmod +x 007.py && python2 007.py" )
                        if system() == 'Windows':
                            os.system( 'cd Tools/tool5 && 007.py' )
                        else:
                            print('unknown error :| ')
                    elif t == 'n':
                        main()
                    else:
                        print('unknown error :| ')
elif choice == '6':
                        print("""\n\033[91m Go to Tools/tool6 
                        	Put Ur  List like this : https://site.com/wp-login.php@user#&pass@
                         y = yes 
                         n = no\033[0m""")
                        t = raw_input( '~>' )
                        if t == 'y':
                            if system() == 'Linux':
                                os.system( "cd Tools/tool6 && chmod +x up.py && python2 up.py" )
                            if system() == 'Windows':
                                os.system( 'cd Tools/tool6 && up.py' )
                            else:
                                print('unknown error :| ')
                        elif t == 'n':
                            main()
                        else:
                            print('unknown error :| ')
elif choice == '7':
                            print("""\n\033[91m Go to Tools/tool7 
                            	Put Ur  List like this : http://www.site.com/administrator/index.php&user&~password#
                             y = yes 
                             n = no\033[0m""")
                            t = raw_input( '~>' )
                            if t == 'y':
                                if system() == 'Linux':
                                    os.system( "cd Tools/tool7 && chmod +x shelljm.py && python2 shelljm.py" )
                                if system() == 'Windows':
                                    os.system( 'cd Tools/tool7 && shelljm.py' )
                                else:
                                    print('unknown error :| ')
                            elif t == 'n':
                                main()
                            else:
                                print('unknown error :| ')
elif choice == '8':
        print("""\n\033[91m Go to Tools/tool8
        	Put Ur  List of Sites in list.txt file 

         y = yes 
         n = no\033[0m""")
        t = raw_input( '~>' )
        if t == 'y':
            if system() == 'Linux':
                os.system( "cd Tools/tool8 && chmod +x bruter.pl && perl bruter.pl -l list.txt -p passwords.txt" )
            if system() == 'Windows':
                os.system( 'cd Tools/tool8 && perl bruter.pl -l list.txt -p passwords.txt' )
            else:
                print('unknown error :| ')
        elif t == 'n':
            main()
        else:
            print('unknown error :| ')
elif choice == '9':
        print("""\n\033[91m Go to Tools/tool9
        	Put Ur  List of Sites in tool9

         y = yes 
         n = no\033[0m""")
        t = raw_input( '~>' )
        if t == 'y':
            if system() == 'Linux':
                os.system( "cd Tools/tool9 && chmod +x cms.py && python2 cms.py" )
            if system() == 'Windows':
                os.system( 'cd Tools/tool9 && cms.py' )
            else:
                print('unknown error :| ')
        elif t == 'n':
            main()
        else:
            print('unknown error :| ')			
elif choice == '10':
        print("""\n\033[91m Just but your MD5 Hash

         y = yes 
         n = no\033[0m""")
        t = raw_input( '~>' )
        if t == 'y':
            if system() == 'Linux':
                os.system( "cd Tools/tool10 && chmod +x md5.py && python2 md5.py" )
            if system() == 'Windows':
                os.system( 'cd Tools/tool10 && md5.py' )
            else:
                print('unknown error :| ')
        elif t == 'n':
            main()
        else:
            print('unknown error :| ')
elif choice == '11':
        print("""\n\033[91m Just but your Dork

         y = yes 
         n = no\033[0m""")
        t = raw_input( '~>' )
        if t == 'y':
            if system() == 'Linux':
                os.system( "cd Tools/tool11 && php go.php" )
            if system() == 'Windows':
                os.system( 'cd Tools/tool11 && php go.php' )
            else:
                print('unknown error :| ')
        elif t == 'n':
            main()
        else:
            print('unknown error :| ')
elif choice == '12':
        print("""\n\033[91m Go to Tools/tool12
        	Put Ur  List of Sites in list.txt file

         y = yes 
         n = no\033[0m""")
        t = raw_input( '~>' )
        if t == 'y':
            if system() == 'Linux':
                os.system( "cd Tools/tool12 && python2 exp.py" )
            if system() == 'Windows':
                os.system( 'cd Tools/tool12 && python exp.py' )
            else:
                print('unknown error :| ')
        elif t == 'n':
            main()
        else:
            print('unknown error :| ')
elif choice == '13':
        print("""\n\033[91m Go to Tools/tool13
        	Put Ur  List of Sites in list.txt file

         y = yes 
         n = no\033[0m""")
        t = raw_input( '~>' )
        if t == 'y':
            if system() == 'Linux':
                os.system( "cd Tools/tool13 && php vBot.php list.txt" )
            if system() == 'Windows':
                os.system( 'cd Tools/tool13 && php vBot.php list.txt' )
            else:
                print('unknown error :| ')
        elif t == 'n':
            main()
        else:
            print('unknown error :| ')			
