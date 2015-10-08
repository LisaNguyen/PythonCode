menu = {"roast chicken": 19.95, "boeuf bourguignon": 27.95, "chicken korma": 22.95, "Irish coffee": 5.95, } 

total = 0

def addItems():
	item = raw_input("What would you like to order?")
	global total

	total += menu[item]
	response = raw_input("Would you like to order another item?")

	if(response.lower() == "yes"):
		addItems()
	

	else: 
		"OK, I'll bring your order to the kitchen now"
		print "Your total is %d" % total

addItems()
