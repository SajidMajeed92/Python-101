# We can define the User defined functions in multiple ways.
# The following are the list of available types of functions in Python.

# With no argument and no return value.
# With no argument and with a Return value.
# Argument and No Return value.
# With argument and return value.

# Types of Functions in Python
# **Python Function with No argument and No Return value**
# With No Arguments, and No Return Value
def Adding():
    a = 20
    b = 30
    Sum = a + b
    print("After Calling :", Sum)


Adding()


# ** Python Function with no argument and with a Return value**
# No arguments and with a Return value Example
# With No Arguments, and with Return Value
def Multiplication():
    a = 10
    b = 25
    Multi = a * b
    return Multi


print("After Calling the Multiplication : ", Multiplication())


# **Python Function with argument and No Return value**
# With Arguments, and NO Return Value
def Multiplications(a, b):
    Multi = a * b
    print("After Calling the Function:", Multi)


Multiplications(10, 20)


# **Python Function with argument and Return value**
# Wwith Arguments, and Return Value
def Addition(a, b):
    Sum = a + b
    return Sum


# We are calling it Outside the Definition
print("After Calling :", Addition(25, 45))


# Example: Parameterized Function
def greet(name):
    print('Hello ', name)


greet('Ahmed')  # calling function with argument
greet(123)


# Multiple Parameters
def greet(name1, name2, name3):
    print('Hello ', name1, ' , ', name2, ', and ', name3)


greet('Steve', 'Bill', 'Yash')  # calling function with string argument


# Unknown Number of Arguments
def greet(*names):
    print('Hello ', names[0], ', ', names[1], ', ', names[3])


greet('Ahsan', 'Bilal', 'Sarim')


# The following function works with any number of arguments.
def greet(*names):
    i = 0
    print('Hello ', end='')
    while len(names) > i:
        print(names[i], end=', ')
        i += 1


greet('Ahsan', 'Bilal', 'Sarim')
greet('Steve', 'Bill', 'Yash', 'Kapil', 'John', 'Amir')


# Function with Keyword Arguments
# In order to call a function with arguments, the same number of actual arguments must be provided.
# However, a function can be called by passing parameter values using the parameter names in any order.
# For example, the following passes values using the parameter names.

def greet(firstname, lastname):
    print('Hello', firstname, lastname)


greet(lastname='Jobs', firstname='Ahmed')  # passing parameters in any order using keyword argument


# Keyword Argument **kwarg
def greet(**person):
    print('Hello ', person['firstname'], person['lastname'])


greet(firstname='Steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55)
greet(firstname='Bill')  # raises KeyError
