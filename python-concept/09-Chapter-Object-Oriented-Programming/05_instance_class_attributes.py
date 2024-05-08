class Employee:
    company = "Google"
    salary = 100

jack = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# jack.salary = 300
# rajni.salary = 400
jack.salary = 45
print(jack.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 