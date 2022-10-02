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

    @staticmethod
    def evaluate_result(result_one: int, result_two: int) -> bool:
        return result_one == result_two


class UserInterface:
    def main(self):
        expression = Calculator.generate_expression()
        print(expression)
        result = Calculator.get_result(expression)
        user_guess = int(input())
        print("Right" if result == user_guess else "Wrong!")


if __name__ == '__main__':
    calc_interface = UserInterface()
    calc_interface.main()
