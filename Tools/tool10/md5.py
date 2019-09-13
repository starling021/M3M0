#~ C0d3d by Marwan007

import os
import requests

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
print("""
               _ _____     _                    _           
              | |  ___|   | |                  | |          
 _ __ ___   __| |___ \  __| | ___  ___ ___   __| | ___ _ __ 
| '_ ` _ \ / _` |   \ \/ _` |/ _ \/ __/ _ \ / _` |/ _ \ '__|
| | | | | | (_| /\__/ / (_| |  __/ (_| (_) | (_| |  __/ |   
|_| |_| |_|\__,_\____/ \__,_|\___|\___\___/ \__,_|\___|_|   
                                                            
    C0d3d by Marwan007 ~ instagram.com/mrwn.007                                                       
""")
md5 = input("[*] MD5 --> ")
print("[!] Please wait...")
try:
	r = requests.get("http://www.nitrxgen.net/md5db/" + md5)
	if r.headers['Content-Length'] == "0":
		print("[-] MD5 not cracked!")
	else:
		print("[+] MD5 Cracked --> " + r.text)
except:
	print("[-] Something went wrong! Please try again...")
