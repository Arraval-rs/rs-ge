#####################################################
# RSGE_lookup.py                                    #
# Item Lookup elements and functions                #
#####################################################

import PySimpleGUI as sg
import RSGE_functions as RSGE_f

class LookupWindow:

	def __init__(self):
		self.lookup_frame = self.create_lookup_frame(self.create_lookup_item_frame())

	def update_widgets(self, window, event, values):
		return

	def create_lookup_frame(self, lookup_item_frame):
		return sg.Frame(layout = 
							[
								[
									sg.Input(size = (25, 1), key = "lookup_input"), 
									sg.Button(button_text = "Search")
								],
								[
									sg.Listbox(values = [], select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, size = (31, 10), key = "lookup_list")
								],
								[
									lookup_item_frame
								]
							], 
							title = "Item Lookup")

	def create_lookup_item_frame(self):
		return sg.Frame(layout = 
									[
										[
											sg.Image(filename = "data/blank.png", size = (96,96)),
											sg.Text(text = 
															"Name: N/A\n" +
															"Description: N/A\n" +
															"Price: 0 gp\n" +
															"Trend:\n" +
															" • 30 days: +0.0%\n" +
															" • 90 days: +0.0%\n" +
															" • 180 days: +0.0%", 
												key = "lookup_stats")
											],
										[
											sg.Button(button_text = "Add"), 
											sg.Input(default_text = "1", size = (10, 1), enable_events = True, key = "lookup_quantity"),
											sg.Text(text = "Total cost: 0 gp", key = "lookup_total")
										]
									], 
									title = "Item Stats")