package minesweeper;

public class Field {
    char[][] field;
    int remainingMines;

    public Field(int mines) {
        FieldGenerator fieldGenerator = new FieldGenerator();
        field = fieldGenerator.generateField(mines);
        remainingMines = mines;
    }


    public void displayBoard() {
        for (char[] row : this.field) {
            System.out.println(new String(row));
        }
    }
}
