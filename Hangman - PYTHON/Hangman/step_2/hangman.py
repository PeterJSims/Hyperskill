class Interface:
    def main(self):
        print("H A N G M A N")
        guess = input("Guess the word: ").lower()
        print("You survived!" if guess == 'python' else 'You lost!')


if __name__ == '__main__':
    game = Interface()
    game.main()
