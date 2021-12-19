# https://codingcompiler.com/python-coding-interview-questions-answers/

class MangleNumber:
    # Write a program to reverse a number in Python
    def calculate_reverse_number(self, number) -> None:
        reverse = 0
        while number > 0:
            left = number % 10
            reverse = reverse * 10 + left
            number = number // 10
        return print(f"The reverse of the number is: {reverse}")

    # Write a program to find the sum of the digits of a number in Python
    def calculate_sum_of_digits(self, number) -> None:
        total = 0
        while number > 0:
            digits = number % 10
            total = total + digits
            number = number // 10
        return print(f"The sum of the digits of the number is: {total}")

    # Write a Python Program to Count the Number of Digits in a Number
    def count_num_of_digits(self, number) -> None:
        count = 0
        while number > 0:
            count = count + 1
            number = number // 10
        return print(f"The count of number of the digits of the number is: {count}")


mangle_number = MangleNumber()
mangle_number.calculate_reverse_number(1234)
mangle_number.calculate_sum_of_digits(1234)
mangle_number.count_num_of_digits(1234)
print('-------------------------------')


class Exercise2:
    def swap_first_last(self, list_of_num: list) -> None:
        size = len(list_of_num)
        
        temp = list_of_num[0]
        list_of_num[0] = list_of_num[size-1]
        list_of_num[size-1] = temp
        return print(f'Swapped list is {list_of_num}')

swap_list = Exercise2()
swap_list.swap_first_last([1,2,3,4])
