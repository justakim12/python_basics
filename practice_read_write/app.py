## read files
employee_file = open("practice_read_write/employees.txt", "r")

## check if file is readable
print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines())

employee_file.close()

## append
employee_file = open("practice_read_write/employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

## write
employee_file = open("practice_read_write/employees2.txt", "w")
employee_file.write("\nToby - Human Resources")
employee_file.close()
