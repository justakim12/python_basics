from constants import INPUT_NUMBERS


class Calculate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x/self.y

first_cal = Calculate(INPUT_NUMBERS.A,INPUT_NUMBERS.B)

print(first_cal.add())
print(first_cal.subtract())
print(first_cal.multiply())
print(first_cal.divide())