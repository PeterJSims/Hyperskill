import random


class RPS:
    CHOICES = ("rock", "paper", "scissors")
    WINNING_CHOICES = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


class Interface:
    def main(self):
        self.round()

    def round(self):
        choice = input()
        if choice in RPS.CHOICES:
            computer_choice = random.choice(RPS.CHOICES)
            results = self.get_results(computer_choice, choice)
            print(results)
            self.round()
        elif choice == '!exit':
            return None
        else:
            print("Invalid input")
            self.round()

    def get_results(self, computer_choice: str, user_choice: str) -> str:
        if computer_choice == user_choice:
            return f"There is a draw ({computer_choice})"
        elif RPS.WINNING_CHOICES[user_choice] == computer_choice:
            return f"Well done. The computer chose {computer_choice} and failed"
        else:
            return f"Sorry, but the computer chose {computer_choice}"


if __name__ == '__main__':
    game_interface = Interface()
    game_interface.round()
