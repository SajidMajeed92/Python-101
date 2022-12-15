# The process of inheriting the properties of the parent class into a child class is called inheritance.
# The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.
# In Object-oriented programming, inheritance is an important aspect. The main purpose of inheritance is the re-usability of code because we can use the existing class to create a new class instead of creating it from scratch.
# In inheritance, the child class acquires all the data members, properties, and functions from the parent class. Also, a child class can also provide its specific implementation to the methods of the parent class.


# Example : Let’s create one parent class called ClassOne and one child class called ClassTwo to implement single inheritance.
# Base class
# Single Inheritance
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')


# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')


# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()


# Multiple Inheritance
# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)


# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)


# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)


# Create object of Employee
emp = Employee()

# access data
emp.person_info('Ali', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')


# Multiple Inheritance
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')


# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')


# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')


# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()


# Hierarchical Inheritance
# Example : Let’s create ‘Vehicle’ as a parent class and two child class ‘Car’ and ‘Truck’ as a parent class.
class Vehicle:
    def info(self):
        print("This is Vehicle")


class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)


class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)


obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')


# Example 2:
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")


# Sports Car can inherit properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")


# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()
