#! /usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
import os
import datetime

dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
os.makedirs('Bing',exist_ok=True)
url = 'http://www.bing.com/' 
soup = requests.get(url)
p=13+soup.text.find("g_img=")
s=''
while soup.text[p]!="'" and soup.text[p]!='"':
	s=s+soup.text[p]
	p=p+1
image_url=url+s
res = requests.get(image_url)
with open(os.path.join('Bing',cd+'.jpg'),'wb') as file:
    file.write(res.content) 
os.system('gsettings set org.gnome.desktop.background picture-uri file://'+os.getcwd()+'/Bing/'+cd+'.jpg')
os.system('notify-send "Wallpaper Updated" "Thank you for using"')
