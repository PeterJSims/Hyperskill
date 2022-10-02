from messages import messages


class Calculator:

    @staticmethod
    def execute_equation(x: float, y: float, op: str) -> float:
        """Simple execution based on operator"""
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        else:
            return x / y

    @staticmethod
    def validate_numeric(num_str: str) -> bool:
        """Ensuring that operations will be called on numeric values"""
        try:
            float(num_str)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_operator(operator_string: str) -> bool:
        """Only the four operators are included in this calculator's scope"""
        return operator_string in ['+', '-', '*', '/']

    @staticmethod
    def is_one_digit(num: float) -> bool:
        """Checks if the number is -10 < num < 10 and an integer value (not float)"""
        return num % 10 == abs(num) and float(num) == int(num)


class CalculatorInterface:

    def __init__(self):
        self.memory = 0

    def main(self) -> None:
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

    def _handle_calculations(self, x, y, op) -> None:
        """Call calculator operation methods and delegate to subprocesses.
        Recursively call the main method if the user wishes to continue."""

        result = Calculator.execute_equation(x, y, op)
        print(result)

        print("Do you want to store the result? (y / n): ")
        choice = input().lower()
        if choice in 'yes':
            self._handle_result_storage(result)

        print("Do you want to continue calculations? (y / n): ")
        choice = input().lower()

        return self.main() if choice in 'yes' else None

    def _check_laziness(self, x, y, op) -> str:
        """Determine a display string based on the flow-chart's 'laziness' conditions."""
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

    def _print_laziness(self, x, y, op) -> None:
        """Process and display the laziness string calculated in self._check_laziness() and display if length > 0"""
        laziness_str = self._check_laziness(x, y, op)
        if laziness_str:
            print(laziness_str)

    def _handle_memory_retrieval(self, input_x: str, input_y: str) -> tuple:
        """Get stored value and switch user's 'M' choice(s) for it"""
        if input_x == 'M':
            input_x = self.memory
        if input_y == 'M':
            input_y = self.memory
        return input_x, input_y

    def _handle_result_storage(self, result: float) -> None:
        """Store the value for complex numbers and determine true preference for saving simple one digit results."""
        if not Calculator.is_one_digit(result):
            self.memory = result
        else:
            current_message = 10
            while current_message <= 12:
                print(messages[f'msg_{current_message}'])
                choice = input().lower()
                if choice in 'yes':
                    current_message += 1
                else:
                    break

            if current_message > 12:
                self.memory = result


if __name__ == '__main__':
    interface = CalculatorInterface()
    interface.main()
