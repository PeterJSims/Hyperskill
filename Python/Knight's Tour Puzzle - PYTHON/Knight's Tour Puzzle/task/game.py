# Write your code here
class Board:
    MOVES = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    def __init__(self, row: int = 8, col: int = 8):
        """Create a board of size n by n with a default of a standard chess board"""
        self.width: int = col + 1
        self.height: int = row + 1
        self.cell_size: int = len(str(self.width * self.height))
        self.board: list[list] = [['_' * self.cell_size] * self.width for _ in range(self.height)]
        self.current_position: tuple = None
        self.visited = []

    def __str__(self):
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

    def determine_moves(self, position: tuple = None):
        if not position:
            position = self.current_position

        possible_moves = []
        for move in Board.MOVES:
            row_spot = position[0] - move[0]
            column_spot = position[1] - move[1]
            if self.check_position(row_spot, column_spot):
                possible_moves.append((row_spot, column_spot))
        return possible_moves

    def mark_spots(self, possible_spots: list[tuple]):
        for spot in possible_spots:
            count_marker = str(len(self.determine_moves((spot[0], spot[1]))) - 1)
            self.mark_position(spot[0], spot[1], count_marker)

    def mark_position(self, row: int, col: int, marker: str = 'X'):
        self.board[row][col] = (' ' * (self.cell_size - 1)) + marker
        self.current_position = row, col

    def check_position(self, row: int, column: int):
        return 0 <= row < self.height and 0 <= column < self.width


class BoardInterface:
    board: Board

    def main(self):

        board_row, board_col = self.get_input(set_board=True)
        self.board = Board(board_row, board_col)
        row, col = self.get_input()
        self.board.mark_position(row, col)
        print()

        spots = self.board.determine_moves()
        self.board.mark_spots(spots)
        print("Here are the possible moves:")
        print(self.board)

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
