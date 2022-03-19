class RandomGenerator:
    def __init__(self):
        self.current_number = ''

    @property
    def current_length(self):
        return len(self.current_number)


class Interface:
    def __init__(self):
        self.random_generator = RandomGenerator()
        self.min_length = 100

    def main(self):
        while self.random_generator.current_length < self.min_length:
            self.get_number()
            self.display_current_state()

    def get_number(self):
        print("Print a random string containing 0 or 1:")
        print()
        user_string = input()
        trimmed_string = self.trim_numbers(user_string)
        self.random_generator.current_number += trimmed_string

    def display_current_state(self) -> str:
        current_len, needed_len = self.random_generator.current_length, self.min_length - self.random_generator.current_length
        if needed_len > 0:
            print(
                f'Current data length is {current_len}, {needed_len} {"symbol" if needed_len == 1 else "symbols"} left')
        else:
            print("Final data string:")
            print(self.random_generator.current_number)

    def trim_numbers(self, num_string: str) -> str:
        return ''.join(x for x in num_string if x in ['0', '1'])


if __name__ == '__main__':
    interface = Interface()
    interface.main()
