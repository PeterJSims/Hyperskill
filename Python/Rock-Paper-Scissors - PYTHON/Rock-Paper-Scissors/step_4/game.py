import random


class RPS:
    CHOICES = ("rock", "paper", "scissors")
    WINNING_CHOICES = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


class Interface:
    def __init__(self):
        self.user = None
        self.user_score = None

    def main(self):
        self.get_user()

        self.round()

    def round(self):
        choice = input()
        if choice in RPS.CHOICES:
            computer_choice = random.choice(RPS.CHOICES)
            results = self.get_results(computer_choice, choice)
            print(results)
            self.round()
        elif choice == '!rating':
            print(f"Your rating: {self.user_score}")
        elif choice == '!exit':
            return None
        else:
            print("Invalid input")
            self.round()

    def get_user(self) -> None:
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

    def get_results(self, computer_choice: str, user_choice: str) -> str:
        if computer_choice == user_choice:
            self.user_score += 50
            return f"There is a draw ({computer_choice})"
        elif RPS.WINNING_CHOICES[user_choice] == computer_choice:
            self.user_score += 100
            return f"Well done. The computer chose {computer_choice} and failed"
        else:
            return f"Sorry, but the computer chose {computer_choice}"


if __name__ == '__main__':
    game_interface = Interface()
    game_interface.main()
