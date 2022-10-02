import random
from string import ascii_lowercase

words = ['python', 'java', 'kotlin', 'javascript']


class Hangman:

    def __init__(self):
        self.guessed_letters = set()
        self.lives = 7
        self.current_word = random.choice(words)

    def main(self):
        print("H A N G M A N")
        print()
        self.menu()

    def menu(self):
        menu_choice = input('Type "play" to play the game, "exit" to quit: ').lower()
        if menu_choice == 'play':
            self._set_new_round_state()
            self.round()
            self.menu()
        elif menu_choice == 'exit':
            return None

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
        guess = input("Input a letter: ")
        if not self._validate_guess(guess):
            return None
        else:
            if guess in self.guessed_letters:
                print("You've already guessed this letter")
            elif guess not in self.current_word:
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
        """Return a boolean based on if the string is a lowercase English letter and has a length of one. Print a statement if one
         of these conditions is not met."""
        if len(guess) != 1:
            print("You should input a single letter")
            return False
        elif guess not in ascii_lowercase:
            print("Please enter a lowercase English letter")
            return False
        else:
            return True

    def _set_new_round_state(self) -> None:
        """Return round specific state to start but maintain cumulative score."""
        self.guessed_letters = set()
        self.lives = 7
        self.current_word = random.choice(words)


if __name__ == '__main__':
    game = Hangman()
    game.main()
