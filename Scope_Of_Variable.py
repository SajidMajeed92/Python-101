# A variable scope specifies the region where we can access a variable.
# Based on the scope, we can classify Python variables into three types:

# Local Variables
# Global Variables
# Nonlocal Variables
#
# Python Local Variables
# When we declare variables inside a function, these variables will have a local scope (within the function).
# We cannot access them outside the function.

def greet():
    name = 'Muhammad'
    print('Hello ', name)


greet()
# print(name)


num = 0


def demo():
    # print(num)
    num = 1
    print("The Number is:", num)


demo()
print(num)

# Python Global Variables
# In Python, a variable declared outside of the function or in global scope is known as a global variable.
# This means that a global variable can be accessed inside or outside of the function.

# declare global variable
message = 'Hello'


def greet():
    # declare local variable
    print('Local', message)


greet()
print('Global', message)

greeting = "Hello"


def change_greeting(new_greeting):
    global greeting
    greeting = new_greeting


def greeting_world():
    world = "World"
    print(greeting, world)


change_greeting("Hi")
greeting_world()


# NonLocal or Enclosing Scope

# Nonlocal Variable is the variable that is defined in the nested function.
# It means the variable can be neither in the local scope nor in the global scope.
# To create a nonlocal variable nonlocal keyword is used.
# In the following code, we created an outer function, and there is a nested function inner().
# In the scope of outer() function inner() function is defined.
# If we change the nonlocal variable as defined in the inner() function, then changes are reflected in the outer function.


def outer():
    first_num = 1

    def inner():
        nonlocal first_num
        first_num = 0
        second_num = 1
        print("inner - second_num is: ", second_num)

    inner()
    print("outer - first_num is: ", first_num)


outer()
