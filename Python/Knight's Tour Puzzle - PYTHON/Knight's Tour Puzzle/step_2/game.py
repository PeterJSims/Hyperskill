# Write your code here
class Board:
    def __init__(self, row: int = 8, col: int = 8):
        """Create a board of size n by n with a default of a standard chess board"""
        self.width = col + 1
        self.height = row + 1
        self.cell_size = len(str(self.width * self.height))
        self.board = [['_' * self.cell_size] * self.width for _ in range(self.height)]

    def __str__(self):
        """Generate the string representation of the current board state. The most complicated aspect is the hackish padding for large sized arrays."""

        # Gather lines into the array below to join at return
        board_string = []
        top_bottom_border = f'{" " * len(str(self.height))}{(self.width * (self.cell_size + 1) + 3) * "-"}'

        board_string.append(top_bottom_border)
        for i in range(len(self.board), 0, -1):
            padding = ' ' if i <= 9 and self.height > 9 else ''
            board_string.append(padding + f"{i}| {' '.join(self.board[i - 1])} |")

        board_string.append(top_bottom_border)
        board_string.append('  ' + ''.join([' ' * self.cell_size +
                                            str(i) for i in range(1, self.width + 1)]))

        return '\n'.join(board_string)

    def set_knight_position(self, row: int, col: int):
        self.board[row][col] = ('_' * (self.cell_size - 1)) + "X"


class Knight:
    pass


class BoardInterface:
    board: Board

    def main(self):

        board_row, board_col = self.get_input(set_board=True)
        self.board = Board(board_row, board_col)
        row, col = self.get_input()
        self.board.set_knight_position(row, col)
        print(self.board)
        # self.board.display_board()

    def get_input(self, set_board: bool = False) -> tuple[int]:
        input_message = "Enter your board dimensions: " if set_board else "Enter the knight's starting position: "
        raw_string = input(input_message)
        while not self.validate_input(raw_string, set_board=set_board):
            raw_string = input(input_message)
        return self.offset_coords(raw_string)

    def validate_input(self, user_string: str, set_board: bool = False) -> bool:
        error_message = "Invalid dimensions!" if set_board else "Invalid position!"

        try:
            col_str, row_str = user_string.split()
            col, row = int(col_str), int(row_str)

            if set_board:
                if not 0 < row or not 0 < col:
                    print(error_message)
                    return False
            elif not set_board:
                if not 1 <= row <= self.board.height or not 1 <= col <= self.board.width:
                    print(error_message)
                    return False
            return True
        except ValueError:
            print(error_message)
            return False

    def offset_coords(self, coordinates: str) -> tuple[int]:
        """Simple method to offset user inputs to zero index arrays and reverse natural column, row ordered input"""
        row, col = coordinates.split()
        return int(col) - 1, int(row) - 1


if __name__ == '__main__':
    game = BoardInterface()
    game.main()
# TODO figure out cell size and adjust printing -> DONE
# TODO knight logic
