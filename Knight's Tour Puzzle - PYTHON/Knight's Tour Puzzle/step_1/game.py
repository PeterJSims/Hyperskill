# Write your code here
class Board:
    def __init__(self, n: int = 8):
        """Create a board of size n by n with a default of a standard chess board"""
        self.board = [['_'] * n for _ in range(n)]
        self.size = n

    def __str__(self):
        """Generate the string representation of the current board state. The most complicated aspect is the hackish padding for large sized arrays."""

        # Gather lines into the array below to join at return
        board_string = []
        border_row_size = (self.size * 2) + 4
        top_bottom_border = "  " + ('-' * border_row_size)

        board_string.append(top_bottom_border)
        for i in range(self.size, 0, -1):
            padding = ' ' if i <= 9 else ''
            board_string.append(f"{padding}{i} | {' '.join(self.board[i - 1])} |")

        board_string.append(top_bottom_border)
        board_string.append((' ' * 5) + f"{' '.join(str(i) for i in range(1, self.size + 1))}")

        return '\n'.join(board_string)

    def knight_position(self, row: int, col: int):
        self.board[row][col] = "X"


class Knight:
    pass


class BoardInterface:
    board: Board

    def main(self):
        self.board = Board()
        row, col = self.get_coordinates()
        self.board.knight_position(row, col)
        print(self.board)

    def get_coordinates(self) -> tuple[int]:
        raw_string = input("Enter the knight's starting position: ")
        while not self.validate_input(raw_string):
            raw_string = input("Enter the knight's starting position: ")
        return self.offset_coords(raw_string)

    def validate_input(self, user_string: str) -> bool:
        try:
            row_str, col_str = user_string.split()
            row, col = int(row_str), int(col_str)
            if not 1 <= row < self.board.size or not 1 <= col < self.board.size:
                print("Invalid dimensions!")
                return False
            return True
        except ValueError:
            print("Invalid dimensions!")
            return False

    def offset_coords(self, coordinates: str) -> tuple[int]:
        """Simple method to offset user inputs to zero index arrays and reverse natural column, row ordered input"""
        row, col = coordinates.split()
        return int(col) - 1, int(row) - 1


if __name__ == '__main__':
    game = BoardInterface()
    game.main()
