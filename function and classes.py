"""
    Provide a full definition for a Python function called is ODD Digit, which takes a string as an argument and returns
    True if the value of the argument is a single-character string with value ‟1‟, ‟3‟, ‟5‟ ,"7"or ‟9‟ and returns False
    otherwise.
"""


def isOddDigit(s):
    if len(s) == 1 and s in ['1', '3', '5', '7', '9']:
        return True
    else:
        return False


print(isOddDigit("1"))  # True
print(isOddDigit("3"))  # True
print(isOddDigit("5"))  # True
print(isOddDigit("7"))  # True
print(isOddDigit("9"))  # True
print(isOddDigit("2"))  # False
print(isOddDigit("hello"))  # False

print("----------------------------------------")
print("----------------------------------------")


# Find a Prime Number
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


print(is_prime(4))


# Second Program
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False

print("----------------------------------------")
print("----------------------------------------")


# Odd Even Program
def is_odd_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(is_odd_even(2))  # True
print(is_odd_even(3))  # False
print(is_odd_even(4))  # True


# Program 2
def is_odd_even(n):
    return True if n % 2 == 0 else False


print(is_odd_even(3))


#
# # Calculator program using Menus
# def calculator():
#     while True:
#         # display menu
#         print("--- Calculator Menu ---")
#         print("0. Quit")
#         print("1. Add two numbers")
#         print("2. Subtract two numbers")
#         print("3. Multiply two numbers")
#         print("4. Divide two numbers")
#         choice = int(input("Enter your choice: "))
#
#         # perform requested action
#         if choice == 0:
#             print("Exiting calculator...")
#             break
#         elif choice == 1:
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("Enter the second number: "))
#             result = num1 + num2
#             print("The result is: ", result)
#         elif choice == 2:
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("Enter the second number: "))
#             result = num1 - num2
#             print("The result is: ", result)
#         elif choice == 3:
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("Enter the second number: "))
#             result = num1 * num2
#             print("The result is: ", result)
#         elif choice == 4:
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("Enter the second number: "))
#             if num2 != 0:
#                 result = num1 / num2
#                 print("The result is: ", result)
#             else:
#                 print("Cannot divide by zero")
#         else:
#             print("Invalid choice. Please enter a number between 0 and 4.")
#
#
# calculator()


# definition of the class starts here
class Person:
    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

        # defining class methods

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

        # end of the class definition


# Create an object of the class
person1 = Person("Abdur Rehman", 23)
# Create another object of the same class
person2 = Person("Asim", 102)
# call member methods of the objects
person1.showAge()
person2.showName()


class Animal:
    def speak(self):
        print("Animal Speaking")
    # child class Dog inherits the base class Animal


class Dog(Animal):
    def bark(self):
        print("dog barking")


d = Dog()
d.bark()
d.speak()


# Inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
    # The child class Dog inherits the base class Animal


class Dog(Animal):
    def bark(self):
        print("dog barking")
    # The child class Dogchild inherits another child class Dog


class DogChild(Dog):
    def eat(self):
        print("Eating bread...")


d = DogChild()
d.bark()
d.speak()
d.eat()
# Real Life Example of method overriding
class Bank:
    def getroi(self):
        return 10;


class SBI(Bank):
    def getroi(self):
        return 7;


class ICICI(Bank):
    def getroi(self):
        return 8;


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi());
print("SBI Rate of interest:", b2.getroi());
print("ICICI Rate of interest:", b3.getroi());