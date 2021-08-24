# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

# Write a Python program to calculate the sum of a list of numbers
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
    
print(list_sum([1,2,3,4]))

# Write a Python program to converting an integer to a string
def change_string(integer):
    return str(integer)
    
print(change_string(30))

# Write a Python program of recursion list sum
def recursion_sum(list):
    total = 0
    for element in list:
        if type(element) == type(list):
            total += recursion_sum(element)
        else:
            total += element
    return total

print(recursion_sum([1, 2, [3,4],[5,6]]))

# Write a Python program to get the factorial of a non-negative integer
def factorial(integer):
    if integer <= 1:
        return 1
    else:
        return integer * (factorial(integer-1))

print(factorial(4))

# Write a Python program to get the sum of a non-negative integer.
## sum_of_integer(231) =  1 + (sum_of_integer(23))
## sum_of_integer(23) = 3 + (sum_of_integer(2))
## sum_of_integer(2) = 2 + 0
def sum_of_integer(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_integer(int(n/10))

print(sum_of_integer(231))