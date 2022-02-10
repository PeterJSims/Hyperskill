from board import Board
from computer_move_utils import ComputerMoveUtils


class Dominos:
    def __init__(self):
        self.game = Board()

    def main(self):
        while not self.game.check_start():
            self.new_game()
        self._round()

    def _round(self):
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
                self._print_ending(ending_state)
                return False
            else:
                self._move()

    def _move(self):
        """Have the current player make their move, then switch who is set as current."""
        if self.game.current_player == 'player':
            self._handle_player_move()
        else:
            self._handle_computer_move()
        self.game.change_player()

    def _handle_player_move(self):
        """Take a user choice, validate, and move the piece from stock to player or player to snake. """
        print("Status: It's your turn to make a move. Enter your command.")
        user_input = input()

        while not self._validate_input(user_input) or not self._validate_move(user_input):
            user_input = input()

        move = abs(int(user_input))

        if move == 0:
            if self.game.stock_pieces:
                new_tile = self.game.stock_pieces.pop()
                self.game.player.append(new_tile)
        else:
            side = 'left' if user_input.startswith('-') else 'right'
            tile = self._flip_tile(self.game.player.pop(move - 1), side)
            if side == 'left':
                self.game.snake = [tile] + self.game.snake
            else:
                self.game.snake.append(tile)

    def _handle_computer_move(self):
        """Use the ComputerMoveUtils methods via _optimal_move() and place tile accordingly.."""
        print("Status: Computer is about to make a move. Press Enter to continue...")
        _ = input()
        computer_choice = self._optimal_move()
        if computer_choice == 0:
            if self.game.stock_pieces:
                new_tile = self.game.stock_pieces.pop()
                self.game.computer.append(new_tile)
        else:
            side = 'left' if computer_choice < 0 else 'right'
            tile = self._flip_tile(self.game.computer.pop(abs(computer_choice) - 1), side)
            if side == 'left':
                self.game.snake = [tile] + self.game.snake
            else:
                self.game.snake.append(tile)

    def _optimal_move(self):
        """Determine the optimal move the computer can make via a chain of DominoGameUtil methods."""
        counts = ComputerMoveUtils.count_occurrences(self.game.computer)
        points_list = ComputerMoveUtils.generate_sorted_point_list(counts, self.game.computer)
        move_side, optimal_piece = ComputerMoveUtils.determine_move_side_and_target(self.game.snake, points_list)

        # Finally, see if this optimal piece exists in the computer's tiles.
        if move_side != 0 and optimal_piece:
            for index in range(len(self.game.computer)):
                piece = self.game.computer[index]
                if piece == optimal_piece:
                    return (index + 1) * move_side

        return 0

    def _print_ending(self, ending_state: str):
        """Print the ending state of win, lose, or draw."""
        ending_string = "Status: The game is over. "
        if ending_state == 'draw':
            print(ending_string + "It's a draw!")
        elif ending_state == 'computer':
            print(ending_string + "The computer won!")
        else:
            print(ending_string + "You won!")

    def _validate_input(self, input_str: str) -> bool:
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

    def _validate_move(self, raw_move_str: str) -> bool:
        """Except for when the choice is 0, the chosen tile must contain the digit on the needed side of the snake."""
        move = abs(int(raw_move_str))

        # A move of 0 is always valid
        if move == 0:
            return True

        chosen_tile = self.game.player[move - 1] if self.game.current_player == 'player' else self.game.computer[
            move - 1]

        # Check if the number at the far left of the snake is in the tile
        if raw_move_str.startswith('-') and self.game.snake[0][0] in chosen_tile:
            return True
        # Check if the number at the far right of the snake is in the tile
        elif self.game.snake[-1][1] in chosen_tile:
            return True

        # If one of the two conditions above was not met, it is not a valid move and the user (not computer) must be notified.
        if self.game.current_player == 'player':
            print("Illegal move. Please try again.")
        return False

    def _flip_tile(self, tile: list, side: str) -> list:
        """As the tile is valid at this point of call, this method just matches the necessary snake number to the side of the tile needed."""
        if side == 'left' and tile[1] != self.game.snake[0][0]:
            tile.reverse()
        elif side == 'right' and tile[0] != self.game.snake[-1][1]:
            tile.reverse()
        return tile

    def new_game(self):
        self.game.reset()
        self.main()


if __name__ == '__main__':
    game = Dominos()
    game.main()
