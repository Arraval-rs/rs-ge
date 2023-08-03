#####################################################
# RSGE_geSummary.py                                 #
# GE item summary elements and functions            #
#####################################################

import PySimpleGUI as sg
import RSGE_functions as RSGE_f

class GeWindow:
	def __init__(self):
		self.summary_frame = self.create_summary_frame(self.create_summary_item_frame())
		self.items = []

	def update_widgets(self, window, event, values):
		return

	def create_summary_item_frame(self):
		return sg.Frame(layout = 
									[
										[
											sg.Image(filename = "data/blank.png", size = (96,96)),
											sg.Text(text = 
															"Name: N/A\n" +
															"Price: 0 gp\n" +
															"HA: 0 gp\n" + 
															"Trend:\n" +
															" • 30 days: +0.0%\n" +
															" • 90 days: +0.0%\n" +
															" • 180 days: +0.0%", 
												key = "summary_stats")
										],
										[
											sg.Button(button_text = "Remove"),
											sg.Text(text = "Quantity: 0\nTotal Cost: 0 gp", key = "summary_total")
										]
									],
									title = "Tracked Items")

	# Item Summary (TOP RIGHT)
	# Multiline
	# Save Button
	# Load Button
	# Load Popup (different profiles)

	def create_summary_frame(self, summary_item_frame):
		return sg.Frame(layout = 
									[
										[
											sg.Text(text = "Total Cost: 0 gp")
										],
										[
											sg.Listbox(values = [], select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, size = (31, 10), key = "summary_list")
										],
										[summary_item_frame],
									],
									title = "Tracked Items")