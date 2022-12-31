# Practice Question 1: Using the while loop, print the square and cube of all numbers between 10 and 20 (included).Your output should look like this: “The square of 10 is 100. The cube of 10 is 1000.”
# x = 9
# while x < 20:
#     x = x+1
#     print(f"The square of {x} is {x*x} and cube of {x} is {x*x*x}")
# Practice Question 2: Ask the user for their favorite month of the year, favorite number, and favorite animal. Create a passcode that is a concatenation of the three strings, for example “may4cat”. Using the while loop, ask the user to enter the correct passcode. The user should be allowed to proceed only when the correct passcode is entered.
# month = input("What is your favorite month of the year?")
# number = input("What is your favorite number?")
# animal = input("What is your favorite animal?")
# print(f" Your Password is the concatenation of the three answer that you gave")
# password = month + number + animal
# guess = 0
# while guess != password:
#     guess = input("Enter your password to proceed")
# print("Password accepted")

# Practice Question 3:  Using the while loop, produce the following output:
#
# *
# **
# ***
# ****
# ***
# **
# *
#
# x = 0
# while x < 4:
#     x = x+1
#     print("*" * x)
# while x > 1:
#     x = x-1
#     print("*" * x)

# Practice Question 4: Using the while loop, produce the following output (which should look like rhombus).
#
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
#
# x = 0
# while x < 4:
#     x = x+1
#     print(" " * (4 - x) + "*" * x)
# while x > 1:
#     x = x-1
#     print(" " * (4 - x) + "*" * x)

# Practice Question 5 : Ask the user to enter two integers. Then ask the user to calculate the product of the two integers. The user has three attempts to give a correct answer. If the correct answer is not given the program terminates providing a correct answer to the user. Program requirements:
# - Do not use IF statements.
# - Implement error handling for all user input (initial numbers and the product).
# - Use the while loop for getting the correct initial input.
# - Use the while loop for getting the correct solution (also remember the maximum of three attempts).
while True:
    a = input("Enter First Integer")
    b = input("Enter Second Integer")
    max_attempts = 3
    try:
        a, b = int(a), int(b)
    except:
        print("Incorrect Input")
        continue
    else:
        break
guess = 0
attempts = 0
while guess != (a*b) and attempts <3:
    attempts = attempts+1
    while True:
        guess = input(f"Attempts #{attempts}.what is {a}*{b}?")
        try:
            guess = int(guess)
        except:
            print("Incorrect Input")
            continue
        else:
            break
print(f"Your answer is {guess}. Correct answer is {a*b}")


