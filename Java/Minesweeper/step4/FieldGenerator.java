package minesweeper;

import java.util.Random;

public class FieldGenerator {
    final private static int SIZE = 9;
    private int startingMines;
    private char[][] field;

    public char[][] generateField(int mineCount) {
        startingMines = mineCount;
        field = generateBlankBoard(SIZE);
        this.placeMines();
        this.placeCounts();
        return this.field;
    }

    private char[][] generateBlankBoard(int size) {
        char[][] blankBoard = new char[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                blankBoard[i][j] = '.';
            }
        }
        return blankBoard;
    }

    private void placeMines() {
        Random random = new Random();
        int remaining = this.startingMines;

        while (remaining > 0) {
            int i = random.nextInt(9);
            int j = random.nextInt(9);
            if (field[i][j] == '.') {
                field[i][j] = 'X';
                remaining--;
            }
        }
    }

    private void placeCounts() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (field[i][j] != 'X') {
                    int numberOfNearbyMines = positionCount(i, j);
                    if (numberOfNearbyMines > 0) {
                        field[i][j] = Character.forDigit(numberOfNearbyMines, 10);
                    }
                }
            }
        }
    }

    private int positionCount(int i, int j) {
        // Checking each touching position from left to right, top to bottom
        int count = 0;

        // Top row
        if (i - 1 >= 0) {
            if (j - 1 >= 0) {
                if (field[i - 1][j - 1] == 'X') count++;
            }
            if (field[i - 1][j] == 'X') count++;
            if (j + 1 < SIZE) {
                if (field[i - 1][j + 1] == 'X') count++;
            }
        }
        // Middle row
        if (j - 1 >= 0) {
            if (field[i][j - 1] == 'X') count++;
        }
        if (j + 1 < SIZE) {
            if (field[i][j + 1] == 'X') count++;
        }

        // Bottom row
        if (i + 1 < SIZE) {
            if (j - 1 >= 0) {
                if (field[i + 1][j - 1] == 'X') count++;
            }
            if (field[i + 1][j] == 'X') count++;
            if (j + 1 < SIZE) {
                if (field[i + 1][j + 1] == 'X') count++;
            }
        }
        return count;
    }
}
