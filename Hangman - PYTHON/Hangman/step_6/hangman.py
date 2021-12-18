import random

words = ['python', 'java', 'kotlin', 'javascript']


class Hangman:

    def __init__(self):
        self.guessed_letters = set()
        # self.score = 0 # Not necessary for this round
        self.lives = 7
        self.current_word = random.choice(words)

    def main(self):
        print("H A N G M A N")
        print()
        self.round()

    def round(self):
        """Keep calling turns while there are remaining lives AND the word is not guessed. If one of these conditions is met,
        print a statement reflecting and and end the current turn."""
        while self.lives >= 0 and not self._is_guessed():
            self._turn()

        if self._is_guessed():
            print(self.current_word)
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You lost!")

    def _turn(self) -> None:
        """Execute a round of the game, and diminish the number of remaining lives depending on rules."""
        print()
        print(self._get_display_word())
        guess = input("Input a letter: ").lower()
        if not self._validate_guess(guess):
            print("Please enter a single letter")
            return None
        else:
            if guess not in self.current_word:
                print("That letter doesn't appear in the word")
                self.guessed_letters.add(guess)
                self.lives -= 1
            elif guess in self.current_word and guess in self.guessed_letters:
                print("No improvements")
                self.lives -= 1
            else:
                self.guessed_letters.add(guess)

    def _is_guessed(self) -> bool:
        """Check to see if the computer's randomly chosen word displays the same as the current """
        return self._get_display_word() == self.current_word

    def _get_display_word(self) -> str:
        """Iterate through a blank version of the computer's choice, replacing each character with a correctly guessed letter."""
        return ''.join(c if c in self.guessed_letters else '-' for c in self.current_word)

    def _validate_guess(self, guess: str) -> bool:
        """Ensure that the guess is both a char string and has a length of one, ensuring a single letter."""
        return guess.isalpha() and len(guess) == 1
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
