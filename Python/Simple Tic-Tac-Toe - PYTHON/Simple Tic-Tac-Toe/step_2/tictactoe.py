class Board:
    def __init__(self, cell_str: str):
        self.board = [list(cell_str[:3]), list(cell_str[3:6]), list(cell_str[6:])]
        self.board_interface = BoardInterface()

    def print_board(self):
        print("here")
        self.board_interface.display_board(self.board)


class BoardInterface:

    @staticmethod
    def validate_cell_string(cell_str: str) -> bool:
        """Check if the string is the appropriate length of nine and only contains valid board characters"""
        if len(cell_str) != 9:
            return False
        return all(c in "OX _" for c in cell_str)

    @staticmethod
    def display_board(board: list) -> None:
        print("---------")
        print(f"| {' '.join(board[0])} |")
        print(f"| {' '.join(board[1])} |")
        print(f"| {' '.join(board[2])} |")
        print("---------")


class UserInterface:
    def main(self):
        cell_string = input("Enter cells: ")
        if BoardInterface.validate_cell_string(cell_string):
            board = Board(cell_string)
            board.print_board()


if __name__ == '__main__':
    interface = UserInterface()
    interface.main()
