messages = {"msg_0": "Enter an equation",
            "msg_1": "Do you even know what numbers are? Stay focused!",
            "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "msg_3": "Yeah... division by zero. Smart move...",
            "msg_4": "Do you want to store the result? (y / n):",
            "msg_5": "Do you want to continue calculations? (y / n):",
            "msg_6": " ... lazy",
            "msg_7": " ... very lazy",
            "msg_8": " ... very, very lazy",
            "msg_9": "You are"}


class Calculator:

    @staticmethod
    def execute_equation(x: float, y: float, op: str) -> float:
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        else:
            return x / y

    @staticmethod
    def validate_numeric(num_str: str):
        try:
            float(num_str)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_operator(operator_string: str):
        return operator_string in ['+', '-', '*', '/']

    @staticmethod
    def is_one_digit(num: float) -> bool:
        return num % 10 == abs(num) and float(num) == int(num)


class CalculatorInterface:

    def __init__(self):
        self.memory = 0

    def main(self):
        print(messages['msg_0'])
        calc = input()
        x, op, y = calc.split()

        x, y = self._handle_memory_retrieval(x, y)

        if not Calculator.validate_numeric(x) or not Calculator.validate_numeric(y):
            print(messages['msg_1'])
            self.main()
        elif not Calculator.validate_operator(op):
            print(messages['msg_2'])
            self.main()
        else:
            x, y = float(x), float(y)
            if op == '/' and float(y) == 0:
                self._print_laziness(x, y, op)
                print(messages['msg_3'])
                self.main()
            else:
                # After passing checks, handle the main call
                self._print_laziness(x, y, op)
                self._handle_calculations(x, y, op)

    def _handle_calculations(self, x, y, op):
        result = Calculator.execute_equation(x, y, op)
        print(result)

        print("Do you want to store the result? (y / n): ")
        choice = input().lower()
        if choice in 'yes':
            self._handle_memory_storage(result)

        print("Do you want to continue calculations? (y / n): ")

        choice = input().lower()
        if choice in 'yes':
            self.main()
        else:
            return None

    def _check_laziness(self, x, y, op):
        msg = ""

        if Calculator.is_one_digit(x) and Calculator.is_one_digit(y):
            msg += messages['msg_6']

        if (x == 1 or y == 1) and op == '*':
            msg += messages['msg_7']

        if (x == 0 or y == 0) and (op in ['+', '-', '*']):
            msg += messages['msg_8']

        if msg:
            msg = messages['msg_9'] + msg

        return msg

    def _print_laziness(self, x, y, op):
        laziness_str = self._check_laziness(x, y, op)
        if laziness_str:
            print(laziness_str)

    def _handle_memory_retrieval(self, input_x: str, input_y: str) -> tuple:
        if input_x == 'M':
            input_x = self.memory
        if input_y == 'M':
            input_y = self.memory
        return input_x, input_y

    def _handle_memory_storage(self, result: float):
        self.memory = result


if __name__ == '__main__':
    interface = CalculatorInterface()
    interface.main()
