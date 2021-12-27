import random


class Calculator:
    """A class to store the logic for generating and evaluating the different levels' questions."""

    OPERATORS = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y
                 }

    @staticmethod
    def generate_expression() -> str:
        """Generate a string that follows X OPERATOR Y to display to user"""
        x, y = random.randint(2, 9), random.randint(2, 9)
        op = random.choice(list(Calculator.OPERATORS))
        operation_string = f"{x} {op} {y}"
        return operation_string

    @staticmethod
    def generate_square_root() -> int:
        """Generate a root which will be squared for the user via a separate method.
        This root exists for generating and validating the resulting square."""
        return random.randint(11, 29)

    @staticmethod
    def get_expression_result(expression: str) -> int:
        """Determine the result of an expression provided in the string format from generate_expression()"""
        x, op, y = expression.split()
        return Calculator.OPERATORS[op](int(x), int(y))

    @staticmethod
    def get_square_result(num: int):
        """Simply square and return a number. Separated from the interface in order to maintain class scope."""
        return num ** 2
