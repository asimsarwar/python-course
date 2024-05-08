class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

emp = Employee()
emp.salary = 100000
emp.getSalary() # Employee.getSalary(asim)