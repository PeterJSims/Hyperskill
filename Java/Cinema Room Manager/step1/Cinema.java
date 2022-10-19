package cinema;

public class Cinema {
    private static final int ROWS = 7;
    private static final int SEATS = 8;
    private char[][] seats;

    public Cinema(){
        seats = new char[ROWS][SEATS];
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < SEATS; j++) {
                seats[i][j] = 'S';
            }
        }
    }

    public void displaySeats(){
        System.out.println("Cinema:");
        System.out.print("  "); // top left padding

        for (int i = 1; i <= SEATS; i++) System.out.print(i + " ");
        System.out.println();

        for (int i = 1; i <= ROWS; i++) {
            System.out.print(i + " ");
            for(char c: seats[i-1]) System.out.print(c + " ");
            System.out.println();
        }

    }


    public static void main(String[] args) {
        Cinema cinema = new Cinema();

        cinema.displaySeats();
    }
}