# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import datetime
import subprocess

dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
os.makedirs('Bing',exist_ok=True)
url = 'http://www.bing.com/' 
sc = requests.get(url)
soup = BeautifulSoup(sc.text,"html5lib")
#print(soup.text)
p=13+soup.text.find("g_img=")
s=''
while soup.text[p]!="'" and soup.text[p]!='"':
	s=s+soup.text[p]
	p=p+1
image_url=url+s
res = requests.get(image_url)
with open(os.path.join('Bing',cd+'.bmp'),'wb') as file:
    file.write(res.content) 
p=subprocess.Popen(['runas', '/user:Yash Mittal', 'REG ADD "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "'+os.getcwd()+'\Bing'+chr(92)+cd+'.bmp" /f'])
p.communicate()
p.wait()
p=subprocess.Popen(['runas', '/user:Yash Mittal', 'RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters'])
p.communicate()
p.wait()