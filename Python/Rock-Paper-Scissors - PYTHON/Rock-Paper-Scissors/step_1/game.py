import random


class RPS:
    CHOICES = ["rock", "paper", "scissors"]
    COMBINATIONS = {
        "WINNING": {"rock": "scissors", "paper": "rock", "scissors": "paper"},
        "LOSING": {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    }

    @staticmethod
    def round():
        # computer_choice = random.choice(RPS.CHOICES)
        choice = input()
        print(f"Sorry, but the computer chose {RPS.COMBINATIONS['LOSING'][choice]}")


class Interface:
    pass


if __name__ == '__main__':
    RPS.round()
