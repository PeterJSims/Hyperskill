package minesweeper;

import java.util.Scanner;

public class Main {
    private final static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        play();
    }


    public static void play() {
        System.out.println("How many mines do you want on the field?");
        int mines = Integer.valueOf(scanner.nextLine());

        Field mineSweeper = new Field(mines);
        handleRounds(mineSweeper);
        System.out.println("Congratulations! You found all mines!");
    }

    public static void handleRounds(Field mineSweeper){
        String coordinatesString;
        mineSweeper.displayBoard();

        while (!mineSweeper.isFinished()) {

            System.out.println("Set/delete mines marks (x and y coordinates):");
            coordinatesString = scanner.nextLine();
            int[] parsedCoordinates = parseCoordinates(coordinatesString);

            if(parsedCoordinates == null){
                System.out.println("Please pass appropriate coordinates");
                continue;
            }

            int col = parsedCoordinates[0];
            int row = parsedCoordinates[1];

            if(mineSweeper.isNumber(row, col)){
                System.out.println("There is a number here!");
            } else {
                mineSweeper.markCell(row, col);
                System.out.println();
                mineSweeper.displayBoard();
            }

        }
    }

    private static int[] parseCoordinates(String rawCoordinates) {
        try {
            // Test that two numbers were given and also offset their values by 1 (as minefield is not zero indexed)
            String[] splitCoords = rawCoordinates.split(" ");
            return new int[]{Integer.parseInt(splitCoords[0]) - 1, Integer.parseInt(splitCoords[1]) - 1};

        } catch (Exception e) {
            return null;
        }
    }

}
