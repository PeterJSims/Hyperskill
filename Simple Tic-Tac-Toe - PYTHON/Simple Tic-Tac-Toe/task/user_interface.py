from board import Board


class UserInterface:
    def main(self):
        game_board = Board()
        self.game(game_board)

    def game(self, game_board: Board):
        """Each call to game represents a full game of tic-tac-toe, played until a finished state arrives."""
        self.print_board(game_board)

        current_state = game_board.return_game_state()

        if current_state == 'Game not finished':

            coordinate_string = input("Enter the coordinates: ")
            while not self.check_user_coordinates(coordinate_string, game_board):
                coordinate_string = input("Enter the coordinates: ")

            row, col = self.split_coordinates(coordinate_string)
            game_board.update_cell(row, col)
            self.game(game_board)
        else:
            self.print_game_state(game_board)

    def print_board(self, game_board: Board) -> None:
        print("---------")
        print(f"| {' '.join(game_board.board[0])} |")
        print(f"| {' '.join(game_board.board[1])} |")
        print(f"| {' '.join(game_board.board[2])} |")
        print("---------")

    def print_game_state(self, game_board: Board) -> None:
        """Grab the Board's state via internal checks and print the result."""
        print(game_board.return_game_state())

    def split_coordinates(self, coordinate_string: str) -> tuple:
        """Return a tuple of the coordinates the user has provided"""
        return int(coordinate_string.split()[0]), int(coordinate_string.split()[1])

    def check_user_coordinates(self, coordinates: str, board: Board):
        """Run checks for the user provided coordinate string, and print statements relevant to the error. Return a boolean
        based on if the check(s) passed."""
        try:
            if len(coordinates.split()) != 2:
                print("Please provide two coordinates")
                return False
            split_coordinates = coordinates.split()
            row, col = int(split_coordinates[0]), int(split_coordinates[1])
            if not 1 <= row <= 3 or not 1 <= row <= 3:
                print("Coordinates should be from 1 to 3!")
                return False
            elif board.board[row - 1][col - 1] not in '_ ':
                print("This cell is occupied! Choose another one!")
                return False
            return True
        except ValueError:
            print("You should enter numbers!")
            return False
