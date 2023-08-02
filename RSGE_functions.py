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

# Poll th RS GE API for the last updated date
def lastUpdate():
	url = 'https://secure.runescape.com/m=itemdb_rs/api/info.json'
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	date = datetime.fromisoformat('2002-02-27') + timedelta(days=data['lastConfigUpdateRuneday'])
	sinceUpdate = datetime.now() - date
	return '{} ({} ago)'.format(date, sinceUpdate)

def priceCheck(itemName):
	itemID = findItemID(itemName)
	if itemID is None:
		return 'N/A'
	url = 'https://secure.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={}'.format(itemID)
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	return data['item']['current']['price']

def findItemID(itemName):
	for item in item_dict:
		if 'name' in item:
			if item['name'] == itemName:
				return item['id']
	return

# Dictionary for JSON from https://chisel.weirdgloop.org/gazproj/cache
json_file = open("data/items.json", "rt")
json_text = json_file.read()
item_dict = json.loads(json_text)
