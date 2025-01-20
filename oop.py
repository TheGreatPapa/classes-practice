
class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        Employee.num_of_employees += 1

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.salary}')"
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"

    def __add__(self, other):
        return self.salary + other.salary
    def __len__(self):
        return len(self.full_name)

    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com".lower()

    def apply_raise(self):
        self.salary *= self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() ==  5 or day.weekday() == 6:
            return False
        return True
    
class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f'---> {emp.full_name}')
        



emp_1 = Employee('Luk','Castillo',50000)
emp_2 = Employee('Viktor','Parang',40000)

#print(emp_1.full_name)
#print(emp_2.full_name)
#print(emp_2.salary)

emp_2.apply_raise()
#print(emp_2.salary)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)

#print(Employee.__dict__)

Employee.set_raise_amt(1.05)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_1 = 'Steve-Smith-30000'
emp_str_1 = 'Wipe-Ass-80000'

Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2025,1,20)
#print(Employee.is_workday(my_date))

dev_1 = Developer('Juan', 'Mendez', 100000, 'Python')

#print(help(Developer))
#print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 100000, [dev_1])
mgr_1.add_emp(emp_1)
mgr_1.add_emp(emp_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Developer))
print(issubclass(Developer,Employee))

      
print(emp_1)
print(repr(dev_1))
print(str(dev_1))

print(emp_1 + emp_2)
print(len(emp_1))

emp_1.full_name = 'New Guy'

print(emp_1)

del emp_1.full_name
print(emp_1)
print(emp_2.email)
