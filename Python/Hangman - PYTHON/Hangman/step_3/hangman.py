import random

words = ['python', 'java', 'kotlin', 'javascript']


class Hangman:
    def main(self):
        print("H A N G M A N")
        guess = input("Guess the word: ").lower()
        computer_choice = random.choice(words)
        print("You survived!" if guess == computer_choice else 'You lost!')


if __name__ == '__main__':
    game = Hangman()
    game.main()
