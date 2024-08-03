class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary

    def display_employee_details(self):
        print(f"Name: {self.name}")
        print(f"Date of Joining: {self.date_of_join}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

# Creating an Employee object
employee1 = Employee("Deep Vachhani", "28-02-2024", "Software Engineer", 75000)

# Displaying the employee details
employee1.display_employee_details()
