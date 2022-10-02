import itertools


class RandomGenerator:

    def __init__(self):
        self.current_number = ''
        self.triads = {''.join(x): [0, 0] for x in itertools.product("01", repeat=3)}

    @property
    def current_length(self):
        return len(self.current_number)

    def generate_triads(self):
        for x in range(len(self.current_number[:-3])):
            triad = self.current_number[x:x + 3]
            if self.current_number[x + 3] == '0':
                self.triads[triad][0] += 1
            else:
                self.triads[triad][1] += 1


class Interface:
    def __init__(self):
        self.random_generator = RandomGenerator()
        self.min_length = 100

    def main(self):
        while self.random_generator.current_length < self.min_length:
            self.get_number()
            self.display_current_state()

        self.display_triads()

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

    def display_triads(self):
        self.random_generator.generate_triads()
        for k, v in self.random_generator.triads.items():
            print(f'{k}: {v[0]},{v[1]}')

    def trim_numbers(self, num_string: str) -> str:
        return ''.join(x for x in num_string if x in ['0', '1'])


if __name__ == '__main__':
    interface = Interface()
    interface.main()
