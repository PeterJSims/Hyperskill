package minesweeper;

import java.util.Random;

public class FieldGenerator {
    final private static int DEFAULT_SIZE = 9;
    private int startingMines;
    private char[][] field;

    public char[][] generateField(int mineCount) {
        startingMines = mineCount;
        field = generateBlankBoard(DEFAULT_SIZE);
        this.placeMines();
        return this.field;
    }


    public int getStartingMines() {
        return startingMines;
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
}
