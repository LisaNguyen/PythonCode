
toDo = []

"""
ASK THE USER WHAT WOULD THEY LIKE TO ADD TO THEIR LIST 
ADDS THIS TO THE LIST 
THEN ASK THEM IF THEY WOULD LIKE TO ENTER ANOTHER task
"""
def addToList():
		task = raw_input("What would you like to add to your list? ")
		toDo.append(task)
		
		anotherTask = raw_input("Would you like to add another task to your list? ")
		if(anotherTask.lower() == "yes"):
			addToList()

		else:
			printList()

"""
PRINTS OUT ALL OF THE TASKS ENTERED TO THE LIST
"""

def printList():
	print "You have added the following to your todo list:"
	for x in toDo:
		print x 

"""
STARTS BY ASKING IF THE USER WOULD LIKE TO ENTER ANYTHING TO THEIR LIST
"""
response = raw_input("Would you like to add a task to your todo list? ")
if(response.lower() == "yes"):
	addToList()

else:
	print "OK, have a nice day!"