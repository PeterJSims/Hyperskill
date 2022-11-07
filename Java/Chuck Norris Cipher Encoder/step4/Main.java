package chucknorris;

import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Input encoded string:");
        String userInput = scanner.nextLine();
        printResults(userInput);
    }

    private static void printResults(String userString) {
        System.out.println("The result: ");
        System.out.println(ChuckNorrisEncryptor.decrypt(userString));
    }
}