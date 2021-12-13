messages = {"msg_0": "Enter an equation",
            "msg_1": "Do you even know what numbers are? Stay focused!",
            "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?"}


class Calculator:
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


class Interface:
    def main(self):
        print(messages['msg_0'])
        calc = input()
        x, op, y = calc.split()
        if not Calculator.validate_numeric(x) or not Calculator.validate_numeric(y):
            print(messages['msg_1'])
            self.main()
        elif not Calculator.validate_operator(op):
            print(messages['msg_2'])
            self.main()


if __name__ == '__main__':
    interface = Interface()
    interface.main()
