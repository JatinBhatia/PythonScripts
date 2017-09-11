#-------------------------------------------------------------------------------
# Name:        thecynaide downloader
# Purpose:  Download all comics from www.explosm.net
#
# Author:      Jatin Bhatia
#
# Created:
# Copyright:
# Licence:
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import urllib
import os
import sys
import re


dir = os.path.dirname(os.path.abspath(__file__))
Cyanidedir = dir + os.sep +"CynaideComics"

if not os.path.exists(Cyanidedir):
	os.makedirs(Cyanidedir)


for url_range in range(39,4319):
 	main_url = "http://explosm.net/comics/"+str(url_range)
 	print("*"*100)
 	print "Entered Page" + str(url_range)
	main_url_opener = urllib.urlopen(main_url)
	main_url_response = main_url_opener.read()
	main_url_soup = BeautifulSoup(main_url_response,"html.parser")
	try:
		img_src_link = main_url_soup.find("img",{"id" : "main-comic"})['src']
		f_img_src_link = img_src_link.replace("//","http://")
		myList = []
	except:
		print("*"*50)
		print ("Link Broken"+img_src_link)
		print("*"*50)
		continue
	del myList[:]
	myList.append(f_img_src_link)
	print myList


	for element in myList:
 		url = element
		print url

 		comicname = url.split('/')
 		comicname = comicname[-1]
 		print comicname

 		comicdir = Cyanidedir + os.sep + comicname

	 	if not os.path.exists(comicdir):
 			print "Downloading:"+comicname
 			os.makedirs(comicdir)
 		else:
 			if not len(os.listdir(Cyanidedir + os.sep)) == 0:
 				print "Neglected"+comicname+" because it already exists."
 				continue
 			else:
 				print "Downloading Comic: "+comicname

 		open_img = urllib.urlopen(url)
 		img_data = open_img.read()
 		filename = comicname
 		path = os.path.join(comicdir,filename)
 		with open(path,"wb") as data:
 			data.write(img_data)
	print "Completed download of comic: "+comicname

print "Download Compelete"

