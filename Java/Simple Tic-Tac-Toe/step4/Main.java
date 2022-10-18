package tictactoe;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String field = scanner.nextLine();

        Board board = new Board(field);
        board.show();

        String s = scanner.nextLine();

        while (true) {
            if (validateInput(s, board)) {
                break;
            }
            s = scanner.nextLine();
        }
        int[] coordinates = parseCoordinates(s);
        board.updateCoordinate(coordinates[0], coordinates[1], 'X');
        board.show();
    }

    public static boolean validateInput(String s, Board board) {
        if (!areCoordinates(s)) return false;

        int[] coordinates = parseCoordinates(s);
        return board.checkCoordinate(coordinates[0], coordinates[1]);
    }

    private static boolean areCoordinates(String s) {
        try {
            String[] splitCoordinates = s.split(" ");
            int i = Integer.valueOf(splitCoordinates[0]);
            int j = Integer.valueOf(splitCoordinates[1]);
        } catch (NumberFormatException e) {
            System.out.println("You should enter numbers!");
            return false;
        }
        return true;
    }

    private static int[] parseCoordinates(String s) {
        String[] splitCoordinates = s.split(" ");
        int i = Integer.valueOf(splitCoordinates[0]);
        int j = Integer.valueOf(splitCoordinates[1]);
        return new int[]{i, j};
    }


}
