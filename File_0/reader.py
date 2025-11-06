with open("employees.txt", "r") as file:
    employees = file.readlines()
for employee in employees:
    print(employee.strip())