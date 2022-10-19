package cinema;

import java.util.Scanner;

public class CinemaInterface {
    private static final Scanner scanner = new Scanner(System.in);

    public static Cinema createCinema() {
        System.out.println("Enter the number of rows:");
        int rows = scanner.nextInt();
        System.out.println("Enter the number of seats in each row:");
        int seatsPerRow = scanner.nextInt();
        System.out.println();

        return new Cinema(rows, seatsPerRow);
    }

    public static void getTicket(Cinema cinema) {
        System.out.println();
        System.out.println("Enter a row number:");
        int rowNumber = scanner.nextInt();
        System.out.println("Enter a seat number in that row:");
        int seatNumber = scanner.nextInt();
        System.out.println();

        if (validInput(cinema, rowNumber, seatNumber)) {
            cinema.buyTicket(rowNumber, seatNumber);
            System.out.println();
        } else {
            getTicket(cinema);
        }
    }

    public static boolean validInput(Cinema cinema, int row, int seatNumber) {
            if(row > cinema.getRows() || row < 1 || seatNumber > cinema.getSeatsPerRow() || seatNumber < 1){
                System.out.println("Wrong input!");
                return false;
            } else if(cinema.getSeat(row, seatNumber) != 'S'){
                System.out.println("That ticket has already been purchased!");
                return false;
            } else{
                return true;
            }
    }

    public static void printStatistics(Cinema cinema) {
        int purchased = cinema.getPurchasedTickets();
        int totalSeats = cinema.getTotalSeats();
        double percentage = purchased == 0 ? 0.0 : 1.0 * purchased / totalSeats * 100;

        System.out.println("Number of purchased tickets: " + purchased);
        System.out.printf("Percentage: %.2f%s%n", percentage, "%");
        System.out.println("Current income: $" + cinema.getIncome());
        System.out.println("Total income: $" + cinema.getTotalValue());


    }

    public static void main(String[] args) {

        Cinema cinema = createCinema();

        while (true) {
            System.out.println("1. Show the seats\n" +
                    "2. Buy a ticket\n" +
                    "3. Statistics\n" +
                    "0. Exit");
            int choice = scanner.nextInt();

            if (choice == 1) {
                cinema.displaySeats();
            } else if (choice == 2) {
                getTicket(cinema);
            } else if (choice == 3) {
                printStatistics(cinema);
            } else {
                break;
            }

        }
    }
}
