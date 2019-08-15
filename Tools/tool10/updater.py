# -*- encoding: utf-8 -*-
#Written by: Marwan007 - M3m0
import os,sys
from .color import *
if sys.version_info[0]==3:
	from urllib.request import urlopen
elif sys.version_info[0]==2:
	from urllib import urlopen

def check():
	f = open( os.path.join("Tools","version.txt"), 'r')
	file_data = f.read().strip()
	try:
		version = urlopen('https://raw.githubusercontent.com/mrwn007/M3M0/master/Tools/version.txt').read().decode('utf-8').strip()
	except:
		error("Can't reach Internet !!!")
		sys.exit(0)

	if version=="1.0":
		return R+Bold+"This is very old version stop using it ! M3M0 became framework now, pull it! :D"
	elif version != file_data:
		return file_data+R+" but new version is available!"
	else:
		return file_data
