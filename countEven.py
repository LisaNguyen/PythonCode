###COUNTS THE NUMBER OF EVEN NUMBERS IN AN ARRAY ###
def countEvens(nums):
	count = 0
	for x in nums:
		if(x%2 == 0):
			count+=1
	print count

countEvens([2,7,8,9])