package minesweeper;

import java.util.Scanner;

public class Main {
    private final static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("How many mines do you want on the field?");
        int mines = scanner.nextInt();

        Field mineSweeper = new Field(mines);

        mineSweeper.displayBoard();
    }
}
