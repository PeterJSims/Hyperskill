from domino_set import DominoSet


class Board:
    def __init__(self):
        tiles = DominoSet().tiles
        self.player, self.computer = tiles[:7], tiles[7:14]
        self.stock_pieces = tiles[14:]
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
