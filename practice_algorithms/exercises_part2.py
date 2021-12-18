# https://codingcompiler.com/python-coding-interview-questions-answers/

# Write a program to reverse a number in Python
class ReverseNumber:
    def reverse_number(self, number: int) -> str:
        reverse = 0
        while number > 0:
            left = number % 10
            reverse = reverse * 10 + left
            number = number // 10
        return print(f"The reverse of the number is: {reverse}")

test = ReverseNumber()
test.reverse_number(12356)
