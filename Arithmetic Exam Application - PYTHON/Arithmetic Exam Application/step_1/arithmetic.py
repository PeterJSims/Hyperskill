class Calculator:
    OPERATORS = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}

    @staticmethod
    def get_result(operation: str):
        x, op, y = operation.split()
        return Calculator.OPERATORS[op](int(x), int(y))


class UserInterface:
    def main(self):
        operation = input()
        if self.is_valid_input(operation):
            print(Calculator.get_result(operation))
        else:
            self.main()

    def is_valid_input(self, operation: str) -> bool:
        if len(operation.split()) != 3:
            print("Please provide an appropriate operation.")
            return False

        x, op, y = operation.split()

        if y == '0' and op == '/':
            print("Cannot divide by 0")
            return False

        try:
            _ = int(x)
            _ = int(y)
            return op in Calculator.OPERATORS
        except ValueError:
            print("Please provide an appropriate operation.")
            return False


if __name__ == '__main__':
    calc_interface = UserInterface()
    calc_interface.main()
