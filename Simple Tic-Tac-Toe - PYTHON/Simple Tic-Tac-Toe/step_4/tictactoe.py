class Board:
    def __init__(self, cell_str: str):
        self.board = [list(cell_str[:3]), list(cell_str[3:6]), list(cell_str[6:])]
        self.turn = 'X'

    def update_cell(self, row: int, col: int) -> None:
        self.board[row - 1][col - 1] = self.turn
        self.update_turn()

    def update_turn(self):
        """Switch turn instance variable to the opposite player's"""
        if self.turn == 'X':
            self.turn == 'O'
        else:
            self.turn == 'X'

    def return_game_state(self) -> str:
        """Collect a string resulting from the row, column, and diagonal char return methods. If it is longer than one,
        we have an impossible game. If it is empty and there are empty cells, the game is not finished. If it is empty
         and has no empty cells, the game is a draw. Otherwise, print the character from the string as the winning player."""
        state_string = self.row_win_char() + self.col_win_char() + self.diagonal_win_char()
        possible_char_count = self.check_char_counts()
        if not state_string and self.check_empty_cells() and possible_char_count:
            return "Game not finished"
        elif not state_string and not self.check_empty_cells():
            return "Draw"
        elif len(state_string) >= 2 or not possible_char_count:
            return "Impossible"
        else:
            return f"{state_string} wins"

    def row_win_char(self) -> str:
        """Check if each row only contains a single character, thus a winning row. Iterate through all rows in case an
        impossible game state exists."""
        winning_char = ''
        for row in self.board:
            if len(set(row)) == 1:
                winning_char += row[0]
        return winning_char

    def col_win_char(self) -> str:
        """Check if each column only contains a single character, thus a winning column. Iterate through all columns in case an
        impossible game state exists."""
        winning_char = ''
        for i in range(3):
            if len(set([self.board[0][i], self.board[1][i], self.board[2][i]])) == 1:
                winning_char += self.board[0][i]
        return winning_char

    def diagonal_win_char(self) -> str:
        """Check if each diagonal only contains a single character, thus a winning diagonal. Check both diagonals in case an
        impossible state exists."""
        winning_char = ''
        if len(set([self.board[0][0], self.board[1][1], self.board[2][2]])) == 1:
            winning_char += self.board[0][0]
        if len(set([self.board[0][2], self.board[1][1], self.board[2][0]])) == 1:
            winning_char += self.board[0][2]
        print(winning_char)
        return winning_char

    def check_char_counts(self) -> bool:
        """Check to make sure the difference between the counts of X and O characters is less than 2"""
        board_string = ''.join(''.join(c) for c in self.board)
        return abs(board_string.count('O') - board_string.count('X')) < 2

    def check_empty_cells(self) -> bool:
        """Check if there are empty cells in the board, which can either be a blank space or an underscore."""
        board_string = ''.join(''.join(c) for c in self.board)
        return board_string.count(" ") > 0 or board_string.count("_") > 0

    @staticmethod
    def validate_cell_string(cell_str: str) -> bool:
        """Check if the string is the appropriate length of nine and only contains valid board characters"""
        if len(cell_str) != 9:
            return False
        return all(c in "OX _" for c in cell_str)


class UserInterface:
    def main(self):
        cell_string = input("Enter cells: ")
        if Board.validate_cell_string(cell_string):
            game_board = Board(cell_string)
            self.print_board(game_board)
            # self.print_game_state(game_board)

            coordinate_string = input("Enter the coordinates: ")
            while not self.check_user_coordinates(coordinate_string, game_board):
                coordinate_string = input("Enter the coordinates: ")

            row, col = self.split_coordinates(coordinate_string)
            game_board.update_cell(row, col)

            self.print_board(game_board)
        else:
            self.main()

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


if __name__ == '__main__':
    interface = UserInterface()
    interface.main()
