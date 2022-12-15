class Employee:
    pass
emp_1=Employee()
emp_2=Employee()

print (emp_1)
print(emp_2)

emp_1.first='Ahsan'
emp_1.last='Ali'
emp_1.email='Ahsan.ali@company.com'
emp_1.pay=5000

emp_2.first='Abdur'
emp_2.last='Rehman'
emp_2.email='Abdur.Rehman@company.com'
emp_2.pay=15000

print (emp_1.first)
print (emp_2.first)
print (emp_1.email)
print (emp_2.email)


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print (emp_1)
print(emp_2)