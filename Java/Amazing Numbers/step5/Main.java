package numbers;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    final static String[] PROPERTIES = {"EVEN", "ODD", "BUZZ", "DUCK", "PALINDROMIC", "GAPFUL", "SPY"};


    private static void generateContent(String rawInput) {
        String[] splitInput = rawInput.split(" ");
        String numsString;

        if (splitInput.length <= 2) {
            numsString = rawInput;
        } else {
            numsString = splitInput[0] + " " + splitInput[1];
        }

        if (!InputProcessor.isValidInput(numsString)) {
            System.out.println("The first parameter should be a natural number or zero.");
        } else {
            generateResults(numsString, splitInput);
        }
    }

    private static void generateResults(String numString, String[] splitInput) {
        long[] nums = InputProcessor.parseRequest(numString);
        if (splitInput.length == 1) {
            Printer.printSingleNumberProperties(nums[0]);
        } else {
            if (!NumberClassifier.isNatural(nums[1])) {
                System.out.println("The second parameter should be a natural number.");
            } else if (splitInput.length == 2) {
                Printer.printMultipleNumberProperties(nums[0], nums[1]);
            } else {
                String property = splitInput[2];
                if (!InputProcessor.isValidProperty(property)) {
                    Printer.printBadPropertyInfo(property);
                } else {
                    Printer.printMultipleNumberProperties(nums[0], nums[1], property);
                }
            }
        }
    }

    public static void menu() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Amazing Numbers!\n");
        Printer.printMenuOptions();

        while (true) {
            System.out.println("\nEnter a request:");
            String rawInput = scanner.nextLine();

            if (rawInput.equals("0")) break;
            if (rawInput.length() == 0) {
                Printer.printMenuOptions();
            } else {
                generateContent(rawInput);
            }
        }
        System.out.println("Goodbye!");
    }

    public static void main(String[] args) {
        menu();
    }
}
