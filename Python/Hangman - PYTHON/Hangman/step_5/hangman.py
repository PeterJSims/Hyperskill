import random

words = ['python', 'java', 'kotlin', 'javascript']


class Hangman:

    def __init__(self):
        self.guessed_letters = set()
        # self.score = 0 # Not necessary for this round
        self.lives = 7
        # self.current_word = random.choice(words)
        self.current_word = 'python'

    def main(self):
        print("H A N G M A N")
        print()
        self.round()

    def round(self):
        # while self.lives >= 0 or not self._is_guessed(): # This round only looks for the number of turns
        while self.lives >= 0:
            self._turn()
            print()

        print("Thanks for playing!")
        print("We'll see how well you did in the next stage")

    def _turn(self) -> None:
        """Execute a round of the game, and return a boolean if it is completed via life loss or guessing correctly."""
        print(self._get_display_word())
        guess = input("Input a letter: ").lower()
        if not self._validate_guess(guess):
            print("Please enter a letter")
            return None
        else:
            if guess not in self.current_word:
                print("That letter doesn't appear in the word")
                self.guessed_letters.add(guess)
                self.lives -= 1
            else:
                self.guessed_letters.add(guess)
                self.lives -= 1

    def _is_guessed(self) -> bool:
        return self._get_display_word() == self.current_word

    def _get_display_word(self) -> str:
        """Iterate through a blank version of the computer's choice, replacing each character with a correctly guessed letter."""
        return ''.join(c if c in self.guessed_letters else '-' for c in self.current_word)

    def _validate_guess(self, guess: str) -> bool:
        return guess.isalnum()
    #
    # def _set_new_round_state(self) -> None:
    #     """Return round specific state to start but maintain cumulative score."""
    #     self.guessed_letters = set()
    #     self.lives = 7
    #
    # def _reset_score(self) -> None:
    #     """Turn cumulative score back to zero"""
    #     self.score = 0


if __name__ == '__main__':
    game = Hangman()
    game.main()
