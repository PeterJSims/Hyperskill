package cinema;

import java.util.Scanner;

public class Cinema {
    private static int ROWS = 7;
    private static int SEATS_PER_ROW = 8;
    private char[][] seats;
    private int income;

    public Cinema(int rows, int seatsPerRow) {
        ROWS = rows;
        SEATS_PER_ROW = seatsPerRow;
        income = 0;
        seats = new char[ROWS][SEATS_PER_ROW];

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < SEATS_PER_ROW; j++) {
                seats[i][j] = 'S';
            }
        }
    }

    public void displaySeats() {
        System.out.println();
        System.out.println("Cinema:");
        System.out.print("  "); // top left padding

        for (int i = 1; i <= SEATS_PER_ROW; i++) System.out.print(i + " ");
        System.out.println();

        for (int i = 1; i <= ROWS; i++) {
            System.out.print(i + " ");
            for (char c : seats[i - 1]) System.out.print(c + " ");
            System.out.println();
        }
        System.out.println();
    }

    public void buyTicket(int row, int seatInRow) {
        int price = getTicketCost(row);
        System.out.println("Ticket price: $" + price); // temp for Step 3 display need
        income += price;
        updateSeat(row, seatInRow);
    }

    private int getTicketCost(int row) {
        int totalSeats = ROWS * SEATS_PER_ROW;
        if (totalSeats <= 60) {
            return 10;
        } else {
            int frontHalf = ROWS / 2;
            System.out.println("frontHalf: " + frontHalf);
            if (row <= frontHalf) {
                return 10;
            } else {
                return 8;
            }
        }
    }

    private void updateSeat(int row, int seat) {
        // offset 1-indexing
        seats[row - 1][seat - 1] = 'B';

    }

    public int getIncome() {
        return income;
    }

}