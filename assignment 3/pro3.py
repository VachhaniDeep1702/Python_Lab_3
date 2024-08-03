# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Base class 2
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

# Derived class
class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()
        print(f"Department: {self.department}")

manager = Manager("Deep", 21, "M001", 100000, "IT")

manager.display_manager_info()
