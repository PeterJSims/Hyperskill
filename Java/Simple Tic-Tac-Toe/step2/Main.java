package tictactoe;

import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String field = scanner.nextLine();
        Board board = new Board(field);
        board.show();
    }
}
