# Class Attributes
#
# When we design a class, we use instance variables and class variables.
# In Class, attributes can be defined into two parts:
#
# Instance variables: The instance variables are attributes attached to an instance of a class.
# We define instance variables in the constructor ( the __init__() method of a class).
#
# Class Variables: A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.

class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age


s1 = Student("Ahmed", 12)
# access instance variables
print('Student:', s1.name, s1.age)

# access class variable
print('School name:', Student.school_name)

# Modify instance variables
s1.name = 'Ali'
s1.age = 14
print('Student:', s1.name, s1.age)

# Modify class variables
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)


#
# Class Methods
#
# Instance method: Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods.
# Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method.
# Static method: It is a general utility method that performs a task in isolation. Inside this method,
# we do not use instance or class variable because this static method does not have access to the class attributes.
#

# class methods demo
class Student:
    # class variable
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age

    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name


s1 = Student("Harry", 12)

# call instance methods
s1.show()
s1.change_age(14)

# call class method
Student.modify_school_name('XYZ School')
# call instance methods
s1.show()


#
# Class Naming Convention
# Naming conventions are essential in any programming language for better readability. If we give a sensible name, it will save our time and energy later. Writing readable code is one of the guiding principles of the Python language.
#
# We should follow specific rules while we are deciding a name for the class in Python.
#
# Rule-1: Class names should follow the UpperCaseCamelCase convention
# Rule-2: Exception classes should end in 'Error'.
# Rule-3: If a class is callable (Calling the class from somewhere), in that case, we can give a class name like a function.
# Rule-4: Python has built-in classes are typically lowercase words

class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)


# creating object of the class
obj = Fruit("Apple", "red")

# Modifying Object Properties
obj.name = "strawberry"

# calling the instance method using the object obj
obj.show()

# Output Fruit is strawberry and Color is red


# Delete Objects
# In Python, we can also delete the object by using a del keyword. An object can be anything like, class object, list, tuple, set, etc.
class Employee:
    department = "IT"

    def show(self):
        print("Department is ", self.department)


emp = Employee()
emp.show()

# delete object
del emp

# Accessing after delete object
emp.show()
# Output : NameError: name 'emp' is not defined
