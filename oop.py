
class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = f"{first}.{last}@company.com".lower()

        Employee.num_of_employees += 1
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.salary *= self.raise_amount
    
emp_1 = Employee('Luk','Castillo',50000)
emp_2 = Employee('Viktor','Parang',40000)

print(emp_1.full_name())
print(emp_2.full_name())
print(emp_2.salary)

emp_2.apply_raise()
print(emp_2.salary)

print(Employee.raise_amount)
print(emp_1.raise_amount)

print(Employee.__dict__)