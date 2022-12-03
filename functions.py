def welcome():
    print("Introduction to function")
welcome()

# def name():
#     name= input("Enter your Name:")
#     print(name,"Welcome to Python 101")
# name()
# def add():
#     number1= int(input("Number 1 is:"))
#     number2 = int(input("Number 2 is:"))
#     sum = number1+number2
#     print("Sum of two numbers is:", sum)
# add()
# def product():
#     number1= int(input("Number 1 is:"))
#     number2 = int(input("Number 2 is:"))
#     result = number1*number2
#     print("Product of two numbers is:", result)
# product()

# def difference():
#     number1= int(input("Number 1 is:"))
#     number2 = int(input("Number 2 is:"))
#     result = number1-number2
#     print("Difference of two numbers is:", result)
# difference()
# def division():
#     number1= int(input("Number 1 is:"))
#     number2 = int(input("Number 2 is:"))
#     result = number1/number2
#     print("Division of two numbers is:", result)
# division()

# def addNumbers(x,y):
#     sum = x + y
#     return sum
# output = addNumbers(12,9)
# print(output)

# def diffNumbers(x,y):
#     diff = x - y
#     return diff
# output = diffNumbers(12,9)
# print(output)

# def productOfNumber(x,y):
#     product = x * y
#     return product
# output = productOfNumber(12,9)
# print(output)

# def divisionOfNumber(x,y):
#      division = x / y
#      return division
# output = divisionOfNumber(12,3)
# print(output)

# def myFruits(f1, f2, f3, f4):
#     FruitsList = [f1, f2, f3, f4]
#     return FruitsList
# output = myFruits("Apple", "Bannana", "Grapes", "Orange")
# print(output)
#
# def myAnimals(a1,a2,a3):
#     Animalgroup = {'Kitten':a1,'Puppy':a2,'Pup':a3}
#     return Animalgroup
#
# output = myAnimals("Cat","Dog","Rat")
# print(output)

# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
#
# print(max_of_two(3, 6, -5))
# print(max_of_three(3, 6, -5))

# def myChocolates(cList):
#     for i in cList:
#         print(i)
#
# chocolateList = ["Dairy Milk","Snickers","Kitkat"]
# myChocolates(chocolateList)

# def Calendar(year, month, date=''):
#     print(year, month, date)
# Calendar(2023, 2, 14)

# def SwapTwoNumbers(a, b):
#     print("Before Swap: ", a, b)
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b
# a, b = SwapTwoNumbers(17, 24)
# print("After Swap: ", a, b)

# def palindromeCheck(num):
#     temp = num
#     rev = 0
#     while (num != 0):
#         r = num % 10
#         rev = rev * 10 + r
#         num = num // 10
#     if (rev == temp):
#         print(temp, "is a palindrome number")
#     else:
#         print(temp, "is not a palindrome number")
#
#
# palindromeCheck(131)
# palindromeCheck(34)

# def factorial(n):
#     fact = 1
#     while (n != 0):
#         fact *= n
#         n = n - 1
#     print("The factorial is", fact)
# inputNumber = int(input("Enter the number: "))
# factorial(inputNumber)

# function with default argument
# def show_employee(name, salary=9000):
#     print("Name:", name, "salary:", salary)
#
# show_employee("Ben", 12000)
# show_employee("Jessa")
# # Python function to sum all the numbers in a list.
# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))

# def carea(radius):
#     area = 3.14*radius*radius
#     print('Area of circle is', area)
#
# a = 5
# carea(a)

# def isPrime(number):
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#     return True
# def main():
#     for n in range(100,501):
#         if isPrime(n):
#             print(n, end=' ')
# main()
#
# def show_choices():
#     print('\nMenu')
#     print('1. Add')
#     print('2. Subtract')
#     print('3. Multiply')
#     print('4. Divide')
#     print('5. Exit')
#
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# def main():
#     while (True):
#         show_choices()
#         choice = input('Enter choice(1-5): ')
#         if choice == '1':
#             x = int(input('Enter first number: '))
#             y = int(input('Enter second number: '))
#             print('Sum =', add(x, y))
#
#         elif choice == '2':
#             x = int(input('Enter first number: '))
#             y = int(input('Enter second number: '))
#             print('Difference =', subtract(x, y))
#
#         elif choice == '3':
#             x = int(input('Enter first number: '))
#             y = int(input('Enter second number: '))
#             print('Product =', multiply(x, y))
#
#         elif choice == '4':
#             x = int(input('Enter first number: '))
#             y = int(input('Enter second number: '))
#             if y == 0:
#                 print('Error!! divide by zero')
#             else:
#                 print('Quotient =', divide(x, y))
#
#         elif choice == '5':
#             break
#
#         else:
#             print('Invalid input')
#
#
# main()

