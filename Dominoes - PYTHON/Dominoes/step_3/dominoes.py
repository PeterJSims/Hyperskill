import random


class DominoSet:
    def __init__(self):
        self.tiles = DominoSet.generate_set()

    @staticmethod
    def generate_set() -> list:
        """Generate a set of tiles ranging from [0,0] to [6, 6]"""
        tiles = []
        for i in range(7):
            for j in range(7):
                tiles.append([i, j])
        random.shuffle(tiles)
        return tiles


class Board:
    def __init__(self):
        tiles = DominoSet().tiles
        self.stock_pieces = tiles[:14]
        self.player, self.computer = tiles[:7], tiles[7:14]
        self.snake, self.current_player = self.set_start()

    def set_start(self) -> (list, str):
        """Logic for determining the highest starting domino (ie [5, 5] or [6, 6], remove tile from corresponding user and return user's name"""
        doubles_player = [tile for tile in self.player if tile[0] == tile[1]]
        doubles_computer = [tile for tile in self.computer if tile[0] == tile[1]]

        player_max = max(doubles_player, default=[-1, -1])
        computer_max = max(doubles_computer, default=[-1, -1])
        if player_max == computer_max:
            # This is an impossible condition unless both returned [-1,-1] above
            return None, None
        elif player_max > computer_max:
            self.player.remove(player_max)
            return [player_max], 'computer'
        else:
            self.computer.remove(computer_max)
            return [computer_max], 'player'

    def change_player(self):
        """Set the state of current player to its opposite."""
        if self.current_player == 'computer':
            self.current_player = 'player'
        else:
            self.current_player = 'computer'

    def check_start(self) -> bool:
        """These two conditions must be 'truthy' in order for starting conditions to be met."""
        return self.snake and self.current_player

    def print_tiles(self):
        """Simple iteration through a player's tiles. Indexing starts at 1."""
        print("Your pieces:")
        for idx, tile in enumerate(self.player):
            print(f'{idx + 1}: {tile}')
        print()

    def print_snake(self):
        """If a snake's length exceeds six, print the first and last three items, otherwise print all of them."""
        if len(self.snake) <= 6:
            print(''.join(str(x) for x in self.snake))
        else:
            print('...'.join([''.join(str(x) for x in self.snake[:3]),
                              ''.join(str(x) for x in self.snake[-3:])]))

    def check_draw(self) -> bool:
        """A draw is determined by the far left and far right numbers matching, and the count of that number being at least 8."""
        count = 0
        if self.snake[0][0] == self.snake[-1][1]:
            target = self.snake[0][0]
            for tile in self.snake:
                for num in tile:
                    if num == target:
                        count += 1
        return count >= 8

    def check_win(self):
        """Checks if either player has zero tiles, thus winning."""
        return len(self.player) == 0 or len(self.computer) == 0

    def check_end_status(self) -> (bool, str):
        """Check if a draw or win has occurred, and return a boolean if met and the winning player."""
        if self.check_draw():
            return True, 'draw'
        elif self.check_win():
            winner = 'player' if len(self.player) == 0 else 'computer'
            return True, winner
        else:
            return False, None

    def reset(self):
        """Generate a new set of starting pieces and starting state."""
        tiles = DominoSet().tiles
        self.stock_pieces = tiles[:14]
        self.player, self.computer = tiles[:7], tiles[7:14]
        self.snake, self.current_player = self.set_start()


class Dominos:
    def __init__(self):
        self.game = Board()

    def main(self):
        while not self.game.check_start():
            self.new_game()
        self.round()

    def round(self):
        while True:
            print("=" * 70)
            print(f'Stock size: {len(self.game.stock_pieces)}')
            print(f'Computer pieces: {len(self.game.computer)}')
            print()
            self.game.print_snake()
            print()
            self.game.print_tiles()
            finished, ending_state = self.game.check_end_status()
            if finished:
                self.print_ending(ending_state)
                return False
            else:
                self.move()

    def move(self):
        """Have the current player make their move, then switch who is set as current."""
        if self.game.current_player == 'player':
            self.handle_player_move()
        else:
            self.handle_computer_move()
        self.game.change_player()

    def handle_player_move(self):
        """Take a user choice, validate, and move the piece from stock to player or player to snake. """
        print("Status: It's your turn to make a move. Enter your command.")
        user_input = input()

        while not self.validate_input(user_input):
            user_input = input()

        move = abs(int(user_input))

        if move == 0:
            if self.game.stock_pieces:
                new_tile = self.game.stock_pieces.pop()
                self.game.player.append(new_tile)
        else:
            tile = self.game.player.pop(move - 1)
            if user_input.startswith('-'):
                self.game.snake = [tile] + self.game.snake
            else:
                self.game.snake.append(tile)

    def handle_computer_move(self):
        """Generate a random number within the length of the computer's pieces. Index starts at 0 as no user input taken."""
        print("Status: Computer is about to make a move. Press Enter to continue...")
        _ = input()
        random_choice = random.randint(-len(self.game.computer), len(self.game.computer))

        if random_choice == 0:
            if self.game.stock_pieces:
                new_tile = self.game.stock_pieces.pop()
                self.game.computer.append(new_tile)
        else:
            tile = self.game.computer.pop(abs(random_choice) - 1)
            if random_choice < 0:
                self.game.snake = [tile] + self.game.snake
            else:
                self.game.snake.append(tile)

    def print_ending(self, ending_state: str):
        """Print the ending state of win, lose, or draw."""
        ending_string = "Status: The game is over. "
        if ending_state == 'draw':
            print(ending_string + "It's a draw!")
        elif ending_state == 'computer':
            print(ending_string + "The computer won!")
        else:
            print(ending_string + "You won!")

    def validate_input(self, input_str: str) -> bool:
        """Ensure that the input is both an integer and within the length of the player's stock (index starting at 1)"""
        try:
            tile = abs(int(input_str))
            if tile > len(self.game.player):
                print("Invalid input. Please try again.")
                return False
            return True
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
            return False

    def new_game(self):
        self.game.reset()


if __name__ == '__main__':
    game = Dominos()
    game.main()
