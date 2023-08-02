#####################################################
# RSGE_functions.py                                 #
# Code for the update functions of the application  #
#####################################################
import os
import io
import json
import urllib.request
from datetime import datetime
from datetime import timedelta


# Poll the RS GE API for the last updated date
def lastUpdate():
	url = 'https://secure.runescape.com/m=itemdb_rs/api/info.json'
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	date = datetime.fromisoformat('2002-02-27') + timedelta(days=data['lastConfigUpdateRuneday'])
	sinceUpdate = datetime.now() - date
	return 'Last Updated {} ({} ago)'.format(date, sinceUpdate)

def imageUrl(url):
	request = urllib.request.Request(url, headers = {"User-Agent" : "Magic Browser"})
	content = urllib.request.urlopen(request)
	return content.read()

def jsonDict(source, isUrl):
	if(isUrl):
		request = urllib.request.Request(source, headers={"User-Agent" : "Magic Browser"})
		content = urllib.request.urlopen(request)
		return json.loads(content.read())
	return json.loads(open(source, 'rt').read())

gazbot_dict = jsonDict("https://chisel.weirdgloop.org/gazproj/gazbot/rs_dump.json", True)