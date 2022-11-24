# python program to illustrate If statement
i = 10
if (i > 15):
	print("10 is less than 15")
print("I am Not in if")

# python program to illustrate If statement by getting input from the user
#number = int(input("Enter Your Desired Number which you want to check:"))
#if (number > 15):
#	print("Number is greater than 15")
#print ("I am Not in if")

# python program to illustrate If else statement
i = 20
if (i < 15):
    print ("i is Smaller than 15")
    print ("i'm in if Block")
else:
	print("i is Greater than 15")
	print("i'm in else Block")
print("I'm not in if and not in else Block")

# Example 2: Python Nested if
# python program to illustrate nested If statement
i = 10
if (i == 10):
	#  First if statement
	if (i < 15):
		print("i is smaller than 15")
	# Nested - if statement
	# Will only be executed if statement above
	# it is true
	if (i < 12):
		print("i is smaller than 12 too")
	else:
		print("i is greater than 15")

