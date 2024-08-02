class Employee:
    def __init__(self, name, join_date, designation, salary):
        self.name = name
        self.join_date = join_date
        self.designation = designation
        self.salary = salary

# Create an object of the Employee class
emp = Employee("John Doe", "2022-01-01", "Manager", 50000)

# Display employee information
print("Employee Name:", emp.name)
print("Date of Joining:", emp.join_date)
print("Designation:", emp.designation)
print("Salary:", emp.salary)

output:-
