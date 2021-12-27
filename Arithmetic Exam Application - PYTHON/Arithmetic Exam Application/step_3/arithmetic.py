import random


class Calculator:
    OPERATORS = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 # '/': lambda x, y: x / y
                 }

    @staticmethod
    def get_result(expression: str) -> int:
        x, op, y = expression.split()
        return Calculator.OPERATORS[op](int(x), int(y))

    @staticmethod
    def generate_expression() -> str:
        x, y = random.randint(2, 9), random.randint(2, 9)
        op = random.choice(list(Calculator.OPERATORS))
        operation_string = f"{x} {op} {y}"
        return operation_string


class UserInterface:

    def __init__(self):
        self.rounds = 5
        self.correct = 0

    def main(self):
        while self.rounds > 0:
            self.round()
        print(f"Your mark is {self.correct}/5")

    def round(self):
        expression = Calculator.generate_expression()
        print(expression)
        result = Calculator.get_result(expression)
        user_guess = input()
        while not self.validate_input(user_guess):
            user_guess = input()

        correct = result == int(user_guess)
        if correct:
            self.correct += 1
        self.rounds -= 1
        print("Right" if correct else "Wrong!")

    def validate_input(self, user_input: str) -> bool:
        try:
            int(user_input)
            return True
        except ValueError:
            print("Incorrect format")
            return False


if __name__ == '__main__':
    calc_interface = UserInterface()
    calc_interface.main()
