# Create a code that performs addition, subtraction, multiplication, and
# division for different numbers of arguments. Use an abstratc class.
from abc import ABC, abstractmethod


class MathOperations(ABC):

    def __init__(self, *args):
        self.args = args

    @abstractmethod
    def addition(self):
        pass

    @abstractmethod
    def subtraction(self):
        pass

    @abstractmethod
    def multiplication(self):
        pass

    @abstractmethod
    def division(self):
        pass


class ApplyMath(MathOperations):

    def addition(self):
        num = 0
        for i in self.args:
            num += i
        return num

    def subtraction(self):
        # "num" should be equal to the first number in args
        num = self.args[0]
        # Starting the range with 1 to exclude the first number in args
        for i in range(1, len(self.args)):
            num = num - self.args[i]
        return num

    def multiplication(self):
        num = self.args[0]
        for i in range(1, len(self.args)):
            num = num * self.args[i]
        return num

    def division(self):
        return (self.args[0] / self.args[1])


# Create an instance
mathoper = ApplyMath(2, 2, 4, 2, 2)

# Addition
adding = mathoper.addition()
# print(adding)

# Subtraction
subtracting = mathoper.subtraction()
# print(subtracting)

# Multiplication
multiplication = mathoper.multiplication()
print(multiplication)

# Divsion
divsion = ApplyMath(8, 2)
# print(divsion.division())
