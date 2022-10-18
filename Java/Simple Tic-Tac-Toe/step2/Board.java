package tictactoe;

public class Board {
    private char[][] board;

    public Board(String s){
        board = stringToBoard(s);
    }


    private static char[][] stringToBoard(String s){
        char[][] board = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = s.charAt((i * 3) + j);
            }
        }
        return board;
    }

    public void show(){
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
