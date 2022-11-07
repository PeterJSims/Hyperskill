package chucknorris;

import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        start();
    }

    public static void start() {
        System.out.println("Please input operation (encode/decode/exit):");
        String userChoice = scanner.nextLine();

        while (!userChoice.equalsIgnoreCase("exit")) {
            if (!userChoice.equalsIgnoreCase("encode") && !userChoice.equalsIgnoreCase("decode")) {
                System.out.println("There is no \'" + userChoice + "\' operation");
            } else {
                String inputString = getInputString(userChoice);
                printResults(inputString, userChoice);
            }
            System.out.println();
            System.out.println("Please input operation (encode/decode/exit):");
            userChoice = scanner.nextLine();
        }

        System.out.println("Bye!");
    }

    private static String getInputString(String choice) {
        if (choice.equalsIgnoreCase("encode")) {
            System.out.println("Input string:");
        } else {
            System.out.println("Input encoded string: ");
        }
        String inputString = scanner.nextLine();
        return inputString;
    }

    private static void printResults(String userString, String choice) {
        if (choice.equalsIgnoreCase("encode")) {
            System.out.println("Encoded string: ");
            System.out.println(ChuckNorrisEncoder.encode(userString));
        } else {
            try {
                String decoded = ChuckNorrisEncoder.decode(userString);
                System.out.println("Decoded string: ");
                System.out.println(decoded);
            } catch (Exception e) {
                System.out.println("Encoded string is not valid.");
            }
        }
    }
}