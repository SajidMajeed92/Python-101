# Classes and Instance Introduction

class Person:
    def __init__(self, name, gender, profession):
        # data members (instance variables)
        self.name = name
        self.gender = gender
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Gender:', self.gender, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)


# create object of a class
Ali = Person('Ali', 'Male', 'Software Engineer')
Ahmed = Person('Ahmed', 'Male', 'Computer Engineer')

# call methods
Ali.show()
Ali.work()
Ahmed.show()
Ahmed.work()
