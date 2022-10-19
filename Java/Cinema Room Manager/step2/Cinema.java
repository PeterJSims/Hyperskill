package cinema;

import java.util.Scanner;

public class Cinema {

    private static int ROWS = 7;
    private static int SEATS_PER_ROW = 8;
    private char[][] seats;
    private int income;

    public Cinema(int rows, int seatsPerRow){
        ROWS = rows;
        SEATS_PER_ROW = seatsPerRow;
        income = calculateIncome(ROWS, SEATS_PER_ROW);

        seats = new char[ROWS][SEATS_PER_ROW];
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < SEATS_PER_ROW; j++) {
                seats[i][j] = 'S';
            }
        }
    }

    public void displaySeats(){
        System.out.println("Cinema:");
        System.out.print("  "); // top left padding

        for (int i = 1; i <= SEATS_PER_ROW; i++) System.out.print(i + " ");
        System.out.println();

        for (int i = 1; i <= ROWS; i++) {
            System.out.print(i + " ");
            for(char c: seats[i-1]) System.out.print(c + " ");
            System.out.println();
        }
    }

    private static int calculateIncome(int rows, int seatsPerRow){
        int totalSeats = rows * seatsPerRow;
        if(totalSeats <= 60){
            return totalSeats * 10;
        } else{
            int frontHalf = rows / 2;
            int backHalf = rows - frontHalf;
            return (frontHalf * seatsPerRow * 10) + (backHalf * seatsPerRow * 8);
        }
    }

    public int getIncome() {
        return income;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of rows:");
        int rows = scanner.nextInt();
        System.out.println("Enter the number of seats in each row:");
        int seatsPerRow = scanner.nextInt();

        Cinema cinema = new Cinema(rows, seatsPerRow);

        System.out.println("Total income:");
        System.out.println("$" + cinema.getIncome());
    }
}