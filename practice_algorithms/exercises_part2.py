# https://codingcompiler.com/python-coding-interview-questions-answers/

# Write a program to reverse a number in Python
class ReverseNumber:
    def calculate_reverse_number(self, number: int) -> str:
        reverse = 0
        while number > 0:
            left = number % 10
            reverse = reverse * 10 + left
            number = number // 10
        return print(f"The reverse of the number is: {reverse}")


reverse_number = ReverseNumber()
reverse_number.calculate_reverse_number(12356)


# Write a program to find the sum of the digits of a number in Python
class SumOfDigits:
    def calculate_sum_of_digits(self, number: int) -> int:
        total = 0
        while number > 0:
            digits = number % 10
            total = total + digits
            number = number // 10
        return print(f"The sum of the digits of the number is: {total}")


sum_of_digits = SumOfDigits()
sum_of_digits.calculate_sum_of_digits(555)


# Write a Python Program to Count the Number of Digits in a Number
class CountDigits():
    def count_num_of_digits(self, number):
        count = 0
        while number > 0:
            count = count + 1
            number = number // 10
        return print(f"The count of number of the digits of the number is: {count}")


count_of_digits = CountDigits()
count_of_digits.count_num_of_digits(555)



