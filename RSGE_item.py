#####################################################
# RSGE_item.py                                      #
# Item objects used to hold various data            #
#####################################################

import RSGE_functions as RSGE_f

class RSGE_item:
	# default constructor
	def __init__(self, itemId, qty):
		url = 'https://secure.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={}'.format(itemId)
		item_dict = RSGE_f.jsonDict(url, True)
		self.id = itemId
		self.name = item_dict['item']['name']
		self.quantity = qty
		self.description = item_dict['item']['description']
		self.value = item_dict['item']['current']['price'] # change to info from gazbot
		self.day30 = item_dict['item']['day30']['change']
		self.day90 = item_dict['item']['day90']['change']
		self.day180 = item_dict['item']['day180']['change']
		self.image = RSGE_f.imageUrl(item_dict['item']['icon_large'])

	def __str__(self):
		return  (	f"ID: {self.id}\n"\
					f"Name: {self.name}\n"\
					f"Quantity: {self.quantity}\n"\
					f"Description: {self.description}"\
					f"Value: {self.value}\n"\
					f"30 Day Trend: {self.day30}\n"\
					f"90 Day Trend: {self.day90}\n"\
					f"180 Day Trend: {self.day180}\n"\
					f"Image Data: {self.image}"
				)