#####################################################
# RSGE_item.py                                      #
# Item objects used to hold various data            #
#####################################################

class RSGE_item:
	# default constructor
	def __init__(self, dict):
		id = None
		name = None
		quantity = None
		description = None
		value = None
		30day = None
		90day = None
		180day = None

	def __str__(self):
		return f"{self.name}{self.description}{self.value}{self.30day}{self.90day}{self.180day}"
