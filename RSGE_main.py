#####################################################
# RSGE_main.py                                      #
# Event loop of the application                     #
#####################################################

#RSGE files
import RSGE_functions as RSGE_f

print('Last Updated: {}'.format(RSGE_f.lastUpdate()))
while(1):
	print('\nEnter an item:')
	item = input()
	if item == 'exit':
		break
	print('{} price is {} gp'.format(item, RSGE_f.priceCheck(item)))