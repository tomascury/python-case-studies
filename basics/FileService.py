
try:
    employee_file = open("files/employees.txt", "r+")
    print(employee_file.read())
    employee_file.write("\nToby - Human Resources")
    print(employee_file.read())
    employee_file.close()
except PermissionError:
    print("File is not readable")
