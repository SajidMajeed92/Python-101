#Python for loop to iterate through the letters in a word
for i in "The Royal Colosseum":
    print(i)

for i in "The Royal Colosseum":
    print(i, end="")
#Python for loop using the range() function
for j in range(5):
    print(j)
#Python for loop to iterate through a list
AnimalList = ['Cat','Dog','Tiger','Cow']
for x in AnimalList:
    print(x)
#Python for loop to iterate through a dictionary
programmingLanguages = {'J':'Java','P':'Python'}
for key in programmingLanguages.keys():
    print(key,programmingLanguages[key])
#Python for loop using the zip() function for parallel iteration
a1 = ['Python','Java','CSharp']
b2 = [1,2,3]
for i,j in zip(a1,b2):
    print(i,j)
#Using else statement inside a for loop in Python
flowers = ['Jasmine','Lotus','Rose','Sunflower']
for f in flowers:
    print(f)
else:
    print('Done')
#Nested for loops in Python (one loop inside another loop)
list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

for x in list1:
    for y in list2:
        print(x,y)
#Using break statement inside a for loop in Python
vehicles = ['Car','Cycle','Bus','Tempo']

for v in vehicles:
    if v == "Bus":
        break
    print(v)
#Python for loop to count the number of elements in a list
numbers = [12,3,56,67,89,90]
count = 0

for n in numbers:
    count += 1

print(count)
#Python for loop to find the sum of all numbers in a list
numbers = [12,3,56,67,89,90]
sum = 0

for n in numbers:
    sum += n

print(sum)
#Python for loop to copy elements from one list to another
list1 = ['Mango', 'Banana', 'Orange']
list2 = []
for i in list1:
    list2.append(i)

print(list2)
# Python for loop to find the maximum element in a list
numbers = [1, 4, 50, 80, 12]
max = 0

for n in numbers:
    if (n > max):
        max = n

print(max)
# Python for loop to find the minimum element in a list
numbers = [1,4,50,80,12]
min = 1000

for n in numbers:
    if(n<min):
        min = n

print(min)
# Python for loop to print the multiples of 3 using range() function
# printing multiples of 3 till 20

for i in range(3,20,3):
  print(i)

# Python for loop to iterate Over a Set
soc_set = {"Twitter", "Facebook", "Instagram", "Quora"}

for platform in soc_set:
    print(platform)

#  Python for loop to iterate Over a Tuple
footballers_tuple = ("Ronaldo", "Mendy", "Lukaku", "Lampard", "Messi", "Pogba")

for footballer in footballers_tuple:
    print(footballer, end=" ")

# While Loop
number = 0
while number < 10:
    print("Number is" ,number)
    number = number + 1

# Example of using while loops in Python
n = 1

while n < 5:
    print("The Royal Colosseum")
    n = n+1
# Example of using the break statement in while loops
n = 1

while n < 5:
    print("The Royal Colosseum")
    n = n+1
    if n == 3:
        break
# Adding elements to a list using while loop
myList = []
i = 0
while len(myList) < 4:
    myList.append(i)
    i += 1
print(myList)
# Printing the items in a tuple using while loop
myTuple = (10,20,30,40,50,60)
i = 0
while i < len(myTuple):
    print(myTuple[i])
    i += 1

# Finding the sum of numbers in a list using while loop
myList = [23,45,12,10,25]
i = 0
sum = 0
while i < len(myList):
    sum += myList[i]
    i += 1
print(sum)

# Popping out elements from a list using while loop
fruitsList = ["Mango","Apple","Orange","Guava"]
while fruitsList:
    print(fruitsList.pop())
print(fruitsList)

# Python while loop to take inputs from the user
n = int(input("Enter a number: "))
while n != 0:
    n = int(input("Enter zero to quit: "))
# check whether the number is Even or Odd
while True:
    user_input = int(input("Enter an integer: "))
    if user_input % 2 != 0:
        print("This number of odd")
        break
    print("This number is even")

# Finding the average of 5 numbers using while loop
start = 5
sum = 0
count = 0
while start > 0:
    count += 1
    number = int(input("Enter the number "))
    sum += number
    start -= 1
average = sum / count
print("Average of given Numbers:", average)
# Printing the square of numbers using while loop
n = 1
while n <= 5:
    squareNum = n**2
    print(n,squareNum)
    n += 1
# Finding the sum of even numbers using while loop
even_sum=0
i=0
while(i<15):
  even_sum=even_sum+i
  i=i+2
print("sum =",even_sum)