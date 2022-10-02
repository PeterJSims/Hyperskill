import itertools
import random


class RandomGenerator:

    def __init__(self):
        self.current_number = ''
        self.triads = {''.join(x): [0, 0] for x in itertools.product("01", repeat=3)}
        self.prediction_string = ''
        self.final_user_number = ''

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

    def generate_prediction_string(self) -> str:
        starting_chars = self.generate_starting_triad()
        prediction_string = ''
        for x in range(len(self.final_user_number[:-3])):
            zero_count, one_count = self.triads[self.final_user_number[x:x + 3]]
            if zero_count > one_count:
                prediction_string += '0'
            elif zero_count < one_count:
                prediction_string += '1'
            else:
                prediction_string += str(random.randint(0, 1))
        return starting_chars + prediction_string

    def generate_starting_triad(self) -> str:
        return ''.join(str(random.randint(0, 1)) for _ in range(3))

    def generate_accuracy_results(self) -> int:
        correct_guess_count = sum(1 for u, c in zip(self.final_user_number[3:], self.prediction_string[3:]) if u == c)
        return correct_guess_count


class Interface:
    def __init__(self):
        self.random_generator = RandomGenerator()
        self.min_length = 100

    def main(self):
        while self.random_generator.current_length < self.min_length:
            self.get_number()
            self.display_current_state()
        print()

        self.random_generator.generate_triads()
        self.get_number(final=True)
        self.display_prediction()
        self.display_prediction_metrics()

    def get_number(self, final: bool = False):
        print(f"Print a {'random' if not final else 'test'} string containing 0 or 1:")
        print()
        user_string = input()
        trimmed_string = self.trim_numbers(user_string)
        if final:
            self.random_generator.final_user_number = trimmed_string
        else:
            self.random_generator.current_number += trimmed_string

    def display_current_state(self) -> str:
        current_len, needed_len = self.random_generator.current_length, self.min_length - self.random_generator.current_length
        if needed_len > 0:
            print(
                f'Current data length is {current_len}, {needed_len} {"symbol" if needed_len == 1 else "symbols"} left')
        else:
            print("Final data string:")
            print(self.random_generator.current_number)

    def display_prediction(self):
        prediction = self.random_generator.generate_prediction_string()
        self.random_generator.prediction_string = prediction
        print("prediction:")
        print(prediction)
        print()

    def display_prediction_metrics(self):
        correct_guess_count = self.random_generator.generate_accuracy_results()
        accuracy = correct_guess_count / (len(self.random_generator.final_user_number) - 3)
        print(
            f'Computer guessed right {correct_guess_count} out of {len(self.random_generator.final_user_number) - 3} symbols ({"{:.2f}".format(accuracy * 100)} %)')

    def trim_numbers(self, num_string: str) -> str:
        return ''.join(x for x in num_string if x in ['0', '1'])


if __name__ == '__main__':
    interface = Interface()
    interface.main()
# TODO
# loop for predictions
# money
# change display as needed

