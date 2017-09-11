#-------------------------------------------------------------------------------
# Name:        The Idealist downloader
# Purpose:  Download 100 timeline photos (FB API limit) in the The Idealist page.
#
# Author:      Jatin Bhatia
#
# Created:
# Copyright:
# Licence:
#-------------------------------------------------------------------------------

import facebook
import requests
import json
import os
import urllib

#Global variables
app_id = '<Your App Id here>'
app_secret = '<Your App Secret String here>'
img_data_url = []
img_id = []

dir = os.path.dirname(os.path.abspath(__file__))
Idealistdir = dir + os.sep +"Idealist"

if not os.path.exists(Idealistdir):
	os.makedirs(Idealistdir)

#Function to get the fb_token
def get_fb_token(app_id, app_secret):           
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with    
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result

token =  get_fb_token(app_id, app_secret)

#Accessing the Graph API
graph = facebook.GraphAPI(access_token=token, version='2.5')
url_id = '545133395520111?fields=photos.limit(500){images}'

post = graph.get_object(id=url_id)

for x in range(0,100):
	img_data_url.append(post["photos"]["data"][x]["images"][0]["source"])
	img_id.append(post["photos"]["data"][x]["id"])

i=0
for url in img_data_url:
   	open_img = urllib.urlopen(url)
	img_data = open_img.read()
	path = os.path.join(Idealistdir,img_id[i])
	if not os.path.exists(path):
		print "Downloading.."+str(img_id[i])
		print ("*" * 50)
		with open(path,"wb") as data:
   			data.write(img_data)
   	else:
   		print ("File already exists.."+str(img_id[i]))
   	i+=1
