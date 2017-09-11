#-------------------------------------------------------------------------------
# Name:        tell_weather.py
# Purpose:  Tell Weather of your current location
#
# Author:      Jatin Bhatia
#
# Created:
# Copyright:
# Licence:
#-------------------------------------------------------------------------------
import urllib
import json

#Get your IPaddress
def getYourIP():
	data = urllib.urlopen('https://api.ipify.org').read()
	return data

#Get your City
def getYourCity(IP):
	url = 'http://ipinfo.io/' + IP + '/json'
	response = urllib.urlopen(url)
	data = json.load(response)
	city = data['city']
	return city

#Get Weather
def getWeather(City):
	appid = '8b9fd8475e251531fff0d70d200a135c'
	url='http://api.openweathermap.org/data/2.5/weather?q='+ City +'&appid='+appid
	response = urllib.urlopen(url)
	data = json.load(response)
	Temprature =  data['main']['temp']
	Description = data['weather'][0]['description']
	print 'Weather Details:'
	print 'City: '+City
	print 'Temprature: '+str(Temprature - 273)+' C'
	print 'Description: '+Description



IP   = getYourIP()
CITY = getYourCity(IP)
getWeather(CITY)