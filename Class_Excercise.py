# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelX = Vehicle(240, 18)
print("Maximum Speed of Vehicle is :", modelX.max_speed, "\n" "Maximum Mileage given by Vehicle is :", modelX.mileage)


# Create a Vehicle class without any variables and methods
class Vehicle:
    pass


# Define a class that can add and subtract two numbers.
class add_sub:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define 'add' method
    def add(self):
        return self.x + self.y

    # define 'subtract' method
    def subtract(self):
        return self.x - self.y


if __name__ == '__main__':
    x = 10
    y = 6
    # create an instance
    opp = add_sub(x, y)

    # call add method
    print("The Function return the difference between", x, "and ", y, 'is: ', opp.add())

    # print(opp.add())

    # call subtract method
    print("The Function return the difference between", x, "and ", y, 'is: ', opp.subtract())


# Define class and instance attributes

class Cylinder:
    # class attribute
    pi = 3.14

    def __init__(self, radius, height):
        # instance variables
        self.radius = radius
        self.height = height


if __name__ == '__main__':
    c1 = Cylinder(4, 20)
    c2 = Cylinder(10, 50)

    print('pi for c1:', c1.pi, "and c2:", c2.pi)
    print('Radius for c1:', c1.radius, "and c2:", c2.radius)
    print('Height for c1:', c1.height, "and c2:", c2.height)
    print('Pi for both c1 and c2 is:', Cylinder.pi)


# Define class and instance methods
class Cylinder:
    # class attribute
    pi = 3.14

    def __init__(self, radius, height):
        # instance variables
        self.radius = radius
        self.height = height

    # instance method
    def volume(self):
        return Cylinder.pi * self.radius ** 2 * self.height

    # class method
    @classmethod
    def description(cls):
        return 'This is a Cylinder class that computes the volume using Pi=', cls.pi


if __name__ == '__main__':
    c1 = Cylinder(40, 2)  # create an instance/object

    print('Volume of Cylinder:', c1.volume())  # access instance method
    print(Cylinder.description())  # access class method via class
    print(c1.description())  # access class method via instance


# Render a class’s attributes and methods protected.
class Article:
    def __init__(self, title, page_count):
        # initialize protected attributes
        self._title = title
        self._page_count = page_count

    # define protected method
    def _show(self):
        # access protected attributes inside class
        print("Article Title: ", self._title)
        print("Page Count: ", self._page_count)


class Author(Article):
    def __init__(self, name, title, page_count):
        Article.__init__(self, title, page_count)
        self.name = name

    def display(self):
        print("Author Name: ", self.name)
        # access Article's protected method
        self._show()
        print("------------------ \n")


author = Author("Eyong Kevin", "Python Classes and Objects", 3000)
author.display()
# access protected data
print(author._title)


# Render a class’s attributes and methods private.
class Language:
    # private class attribute
    __country = "Cameroon"

    def __init__(self, name):
        # initialize private instance attribute
        self.__name = name

    # private method
    def __show(self):
        # access private attributes
        print("Country: ", Language.__country)
        print("Name :", self.__name)

    # public method
    def display(self):
        # access private method within class
        self.__show()


lang = Language("English")
lang.display()

# access private variable and method
lang._Language__show()
print("Access Private Name: ", lang._Language__name)
