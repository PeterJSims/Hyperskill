package cinema;

import java.util.Scanner;

public class CinemaInterface {
    private static final Scanner scanner = new Scanner(System.in);
    public static Cinema createCinema(){
        System.out.println("Enter the number of rows:");
        int rows = scanner.nextInt();
        System.out.println("Enter the number of seats in each row:");
        int seatsPerRow = scanner.nextInt();
        System.out.println();

        return new Cinema(rows, seatsPerRow);
    }



    public static void main(String[] args) {

        Cinema cinema = createCinema();

        while(true){
            System.out.println("1. Show the seats\n" +
                    "2. Buy a ticket\n" +
                    "0. Exit");
            int choice = scanner.nextInt();

            if(choice == 1){
                cinema.displaySeats();
            } else if (choice == 2){
                System.out.println();
                System.out.println("Enter a row number:");
                int rowNumber = scanner.nextInt();
                System.out.println("Enter a seat number in that row:");
                int seatNumber = scanner.nextInt();
                cinema.buyTicket(rowNumber, seatNumber);
                System.out.println();
            } else {
                break;
            }
        }

    }
}
