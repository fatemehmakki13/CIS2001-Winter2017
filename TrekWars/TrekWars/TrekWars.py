class Alignment:
    US = 1
    THEM = 2
    CHAOTIC = 3

class Employee:
    def __init__(self):
        self.ID = 0
        self.Name = ""
        self.Hour_Rate = 0.0
        self.Manager = None
        self.Alignment = None

    def GetSalary(self):
        return self.Hour_Rate * 40

class SalariedEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.Weekly_Salary = 0

    def GetSalary(self):
        return self.Weekly_Salary


def PrintEmployee(employee):
    if isinstance(employee, Employee):
        print("ID: %d - Name: %s - Weekly Salary: %.2f" % ( employee.ID, employee.Name, employee.GetSalary() ) )
        if employee.Manager != None:
            print("\tManager's Name: %s" % employee.Manager.Name )
        if employee.Alignment == Alignment.US:
            print("Team us!")
        elif employee.Alignment == Alignment.THEM:
            print("Booo!")
        else:
            print("watch out!")

    else:
        print("can't print: " + employee)

employee1 = Employee()
employee1.ID = 123
employee1.Name = "Robert"
employee1.Hour_Rate = 10.5
employee1.Alignment = Alignment.US

employee2 = Employee()
employee2.ID = 234
employee2.Name = "Bryant"
employee2.Hour_Rate = 11.5
employee2.Alignment = Alignment.THEM


manager = SalariedEmployee()
manager.ID = 345
manager.Name = "Fatemeh"
manager.Weekly_Salary = 1000
manager.Alignment = Alignment.CHAOTIC


employee1.Manager = manager
employee2.Manager = manager

PrintEmployee(employee1)
PrintEmployee(employee2)
PrintEmployee(manager)
PrintEmployee("print me!")