from calculator import Calculator


class UserInterface:

    def __init__(self):
        self.rounds = 5
        self.correct = 0
        self.level = 0

    def main(self):
        self.level = self.get_level()

        while self.rounds > 0:
            self.round()

        print(f"Your mark is {self.correct}/5. Would you like to save the results? Enter yes or no.")

        if input().lower() in 'yes':
            self.save_results()

    def get_level(self) -> int:
        """Determine the type of questions that the round will contain."""
        print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
        choice = input()
        if not self.validate_input(choice) and choice not in ['1', '2']:
            self.get_level()
        else:
            return int(choice)

    def round(self):
        """Run through five rounds of the user's choice in level. Incorrect format in responses will not deduct a round."""
        if self.level == 1:
            computer_question = Calculator.generate_expression()
        else:
            computer_question = Calculator.generate_square_root()

        print(computer_question)

        if self.level == 1:
            result = Calculator.get_expression_result(computer_question)
        else:
            result = Calculator.get_square_result(computer_question)

        user_guess = input()
        while not self.validate_input(user_guess):
            user_guess = input()

        correct = result == int(user_guess)

        if correct:
            self.correct += 1

        self.rounds -= 1
        print("Right" if correct else "Wrong!")

    def save_results(self):
        """Get the user's name and save to a results file."""
        level_text = 'simple operations with numbers 2-9' if self.level == 1 else 'integral squares of 11-29'
        print("What is your name?")
        name = input()
        with open('results.txt', 'a+') as f:
            f.write(
                f"{name}: {self.correct}/5 in level {self.level} ({level_text}.)")
        print('The results are saved in "results.txt".')

    def validate_input(self, user_input: str) -> bool:
        """Return if the input can be cast to integer with the side effect of alerting the user to the issue."""
        try:
            int(user_input)
            return True
        except ValueError:
            print("Incorrect format")
            return False
