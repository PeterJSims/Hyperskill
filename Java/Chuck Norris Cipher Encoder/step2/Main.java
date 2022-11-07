package chucknorris;

import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Input string:");
        String userInput = scanner.nextLine();

        printResults(userInput);
    }

    private static void printResults(String userString) {
        System.out.println("The result: ");
        for (char c : userString.toCharArray()) {
            String s = String.format("%7s", Integer.toBinaryString(c)).replace(" ", "0");
            System.out.println(c + " = " + s);
        }
    }
}