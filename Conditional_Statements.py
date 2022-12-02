# python program to illustrate If statement
i = 10
if (i > 15):
	print("10 is less than 15")
print("I am Not in if")

# python program to illustrate If else statement
i = 20
if (i < 15):
    print ("i is Smaller than 15")
    print ("i'm in if Block")
else:
	print("i is Greater than 15")
	print("i'm in else Block")
print("I'm not in if and not in else Block")

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

# A school has following rules for Grading System:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter Marks and print the corresponding Grade.

marks = input("Enter Your Marks:")
if marks<25:
  print "F"
elif marks>=25 and marks<45:
  print "E"
elif marks>=45 and marks<50:
  print "D"
elif marks>=50 and marks<60:
  print "C"
elif marks>=60 and marks<80:
  print "B"
else:
  print "A"

#Take values of length and breadth of a rectangle from user and check if it is square or not.

print "Enter length"
length = input()
print "Enter breadth"
breadth = input()
if length == breadth:
  print "Yes, it is square"
else:
  print "No, it is only Rectangle"


#Take input of age of 3 people by user and determine oldest and youngest among them.

first_person_age = input("Enter first person age:")
second_person_age  = input("Enter Second person age:")
third_person_age  = input("Enter third person age:")

if first_person_age >= second_person_age and first_person_age >= third_person_age:
  print "Oldest is",first_person_age
elif second_person_age >= first_person_age and second_person_age >= third_person_age:
  print "Oldest is",second_person_age
elif third_person_age >= first_person_age and third_person_age >= second_person_age:
  print "Oldest is",third_person_age
else:
  print "All are equal"
#Check you are Eligible for vote
age = input("Enter Your age:")
if age>=18:
    print("Eligible for Vote")
else:
    print("Not Eligible for Vote")