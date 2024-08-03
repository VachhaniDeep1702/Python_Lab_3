class Calculator:
    def __init__(self):
        self.__result = 0  # Private variable to store the result

    def add(self, value):
        self.__result += value

    def subtract(self, value):
        self.__result -= value

    def get_result(self):
        return self.__result

calc = Calculator()

calc.add(10)
calc.subtract(3)

print(f"The result is: {calc.get_result()}")
