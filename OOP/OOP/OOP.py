class Employee:
    def __init__(self, name, number, wage):
        self.Name = name
        self.Number = number
        self.Wage = wage

    def SetNumberOfHoursWorked(self, hours):
        self.HoursWorked = hours

    def GetWeeklySalary(self):
        return self.Wage * self.HoursWorked

def CreateEmployee():
    name = input("Enter employee's name: ")
    number = int(input("Enther employee's number: ") )
    wage = float(input("Enter employee's hourly wage: ") )
    employee = Employee(name, number, wage)
    return employee

employee_directory = []
number_of_employees = int(input("Please enter the numbers of employees: "))
for employee in range(number_of_employees):
    employeeRecord = CreateEmployee()
    employee_directory.append(employeeRecord)

for employee in employee_directory:
    print( employee.Name, "weekly salary:", employee.GetWeeklySalary() )