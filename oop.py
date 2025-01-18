
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def full_name(self):
        return f"{self.first} {self.last}"
    
emp_1 = Employee('Luk','Castillo',50000)
emp_2 = Employee('Viktor','Parang',40000)

print(emp_1.full_name())
print(emp_2.full_name())
