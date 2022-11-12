package minesweeper;

public class Field {
    char[][] field;
    int remainingMines;

    protected Field(int mines) {
        FieldGenerator fieldGenerator = new FieldGenerator();
        field = fieldGenerator.generateField(mines);
        remainingMines = mines;
    }

    protected boolean isMarkable(int i, int j) {
        return field[j][j] == '.';
    }

    protected boolean isNumber(int i, int j) {
        return Character.isDigit(field[i][j]);
    }

    protected void markCell(int i, int j) {
        field[i][j] = '*';
        remainingMines--;
    }

    protected boolean isFinished() {
        return remainingMines == 0;
    }


    protected void displayBoard() {
        System.out.println(" |123456789|");
        System.out.println("-|---------|");
        for (int i = 0; i < field.length; i++) {
            System.out.print((i + 1) + "|");
            for (int j = 0; j < field[i].length; j++) {
                if (field[i][j] == 'X') System.out.print('.');
                else System.out.print(field[i][j]);
            }
            System.out.println("|");
        }

        System.out.println("-|---------|");
    }
}
