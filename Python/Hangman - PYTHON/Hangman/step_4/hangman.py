import random

words = ['python', 'java', 'kotlin', 'javascript']


class Hangman:
    def main(self):
        self.game()

    def game(self):
        print("H A N G M A N")
        computer_choice = random.choice(words)

        guess = input(f"Guess the word {self.get_display_word(computer_choice)}: ").lower()

        print("You survived!" if guess == computer_choice else 'You lost!')

    def get_display_word(self, word: str) -> str:
        return word[:3] + (len(word) - 3) * '-'


if __name__ == '__main__':
    game = Hangman()
    game.main()
