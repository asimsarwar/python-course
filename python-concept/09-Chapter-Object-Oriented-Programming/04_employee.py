class Employee:
    company = "Google"
    salary = 100

emp = Employee()
rajni = Employee()
emp.salary = 300
rajni.salary = 400

print(emp.company)
print(rajni.company)
Employee.company = "YouTube"
print(emp.company)
print(rajni.company)
print(emp.salary)
print(rajni.salary)