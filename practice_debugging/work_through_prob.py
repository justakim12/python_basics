# Define a function that iterates over a list of numbers
# multiplies each number by one less than its index position
# and returns the total sum of those products

values = [1,2,3,4,5]

# 1 * (0-1) = -1
# 2 * (1-1) = 0
# 3 * (1) = 3
# 4 * 2 = 8
# 5 * 3 = 15
# ==================
# -1 + 0 + 3 + 8 + 15 = 25 

def multiply_element(numbers):
    total = 0
    for index, number in enumerate(numbers): 
        total += number * (index - 1)
    return total

print(multiply_element(values))