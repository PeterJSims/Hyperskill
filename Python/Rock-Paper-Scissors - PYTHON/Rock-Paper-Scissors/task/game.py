import random


class RPS:
    def __init__(self):
        self.user = None
        self.user_score = None
        self.options = ["rock", "paper", "scissors"]

    def main(self):
        """Get the user input, get the user's choice options, and start the round of RPS+"""
        self.get_user()
        self.get_options()
        self.round()

    def round(self):
        choice = input()
        if choice in self.options:
            computer_choice = random.choice(self.options)
            results = self.get_results(computer_choice, choice)
            print(results)
            self.round()
        elif choice == '!rating':
            print(f"Your rating: {self.user_score}")
        elif choice == '!exit':
            return None
        elif choice not in self.options:
            print("Invalid input")
            self.round()

    def get_user(self) -> None:
        """Read the rating.txt file. Get the user's name and check against said file, loading the score if possible or setting it to 0."""
        users = {}
        with open('rating.txt') as f:
            for line in f:
                user, score = line.split()
                users[user] = int(score)
        name = input("Enter your name: ")
        print(f"Hello, {name}")
        self.user = name

        if name in users:
            self.user_score = users[name]
        else:
            self.user_score = 0

    def get_options(self):
        """For the extended version of the game, let the user provide an arbitrarily sized list of options, whose winning/losing
        options will be determined algorithmically."""
        options = input()
        if len(options) > 0:
            self.options = options.split(',')

        print("Okay, let's start")

    def get_results(self, computer_choice: str, user_choice: str) -> str:
        """Given the RPS+ algorithm, check the index of the user's choice against the index of the computer's choice."""
        computer_index = self.options.index(computer_choice)
        user_index = self.options.index(user_choice)

        if user_index > computer_index:
            user_index -= len(self.options)

        if computer_choice == user_choice:
            self.user_score += 50
            return f"There is a draw ({computer_choice})"
        elif computer_index - user_index > len(self.options) // 2:
            self.user_score += 100
            return f"Well done. The computer chose {computer_choice} and failed"
        else:
            return f"Sorry, but the computer chose {computer_choice}"


if __name__ == '__main__':
    game_interface = RPS()
    game_interface.main()
