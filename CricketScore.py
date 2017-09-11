import urllib
import json
import schedule
import subprocess
import time
import sys


Team = 'India'
#To get the ID of the match
def GET_MATCH_ID():
	try:
		url = 'https://cricscore-api.appspot.com/csa'
		response = urllib.urlopen(url)	
		data = json.load(response)
		for info in data:
			if(info['t2'] == Team or info['t1'] == Team):
				Match_ID = info['id']
				#GET_MATCH_INFO(Match_ID)
				return Match_ID
	except:
		SEND_NOTIFY("Error")

	
#To get Info about the score
def GET_MATCH_INFO(Match_ID):
	url1 = 'https://cricscore-api.appspot.com/csa?id='+str(Match_ID)
	response = urllib.urlopen(url1)
	data = json.load(response)
	for info in data:
		if(info['id'] == Match_ID):
			return info['de']



#Function to display notification on the Ubuntu
def SEND_NOTIFY(message):
	subprocess.Popen(['notify-send', message])
	return



MATCH_ID = GET_MATCH_ID()

if (MATCH_ID == None):
 	SEND_NOTIFY("No Matches currently for "+Team)
else:
	MATCH_INFO = GET_MATCH_INFO(MATCH_ID)
	SEND_NOTIFY(str(MATCH_INFO))





