package tictactoe;

public class Board {
    private char[][] board;
    private int emptyCells;

    public Board() {
        board = createBoard();
        emptyCells = 9;
    }

    private static char[][] createBoard() {
        char[][] board = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = ' ';
            }
        }
        return board;
    }

    public boolean checkCoordinate(int i, int j) {
        if (i < 1 || i > 3 || j < 0 || j > 3) {
            System.out.println("Coordinates should be from 1 to 3!");
            return false;
        }
        // Offset the 1-indexing
        i -= 1;
        j -= 1;
        char targetedChar = board[i][j];
        if (targetedChar == 'X' || targetedChar == 'O') {
            System.out.println("The cell is occupied! Choose another one!");
            return false;
        }
        return true;
    }

    public void updateCoordinate(int i, int j, char c) {
        // Update with the offset of coordinates being entered from 1 to 3
        board[i - 1][j - 1] = c;
        emptyCells--;
    }

    private char getWinningCharacter() {
        for (int i = 0; i < 3; i++) {
            if ((board[i][0] == board[i][1] && board[i][1] == board[i][2] && isPlayerChar(i, 0))) return board[i][0];
            if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && isPlayerChar(0, i)) return board[0][i];
        }
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && isPlayerChar(0, 0)) return board[0][0];
            // if all other scenarios weren't the winning row, it must be right to left diagonal
        else return board[0][2];
    }

    protected String determineState() {
        boolean isWinner = isWinner();
        if (emptyCells == 0 && !isWinner) return "Draw";
        if (isWinner) return getWinningCharacter() + " wins";
        else return "Game not finished";
    }

    public void printGameState() {
        System.out.println(determineState());
    }

    private boolean isPlayerChar(int i, int j) {
        return board[i][j] == 'X' || board[i][j] == 'O';
    }

    private boolean isWinner() {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && isPlayerChar(i, 0)) return true;
            if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && isPlayerChar(0, i)) return true;
        }
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && isPlayerChar(0, 0)) return true;
        if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && isPlayerChar(0, 2)) return true;
        return false;
    }

    public void show() {
        System.out.println("---------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.print("|\n");
        }
        System.out.println("---------");
    }
}
