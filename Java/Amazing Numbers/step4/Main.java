package numbers;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    private static void printSingleNumberProperties(long n) {
        System.out.println("Properties of " + n);
        System.out.println("        buzz: " + NumberClassifier.isBuzz(n));
        System.out.println("        duck: " + NumberClassifier.isDuck(n));
        System.out.println(" palindromic: " + NumberClassifier.isPalindrome(n));
        System.out.println("      gapful: " + NumberClassifier.isGapful(n));
        System.out.println("        even: " + NumberClassifier.isEven(n));
        System.out.println("         odd: " + !NumberClassifier.isEven(n));

    }

    private static void printMultipleNumberProperties(long n, long count) {
        for (long i = n; i < n + count; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(" ");
            }
            System.out.println(i + " is " + String.join(", ", generateStatusArray(i)));
        }
    }



    private static String[] generateStatusArray(long n) {
        StringBuilder statuses = new StringBuilder();
        if (NumberClassifier.isBuzz(n)) statuses.append("buzz ");
        if (NumberClassifier.isDuck(n)) statuses.append("duck ");
        if (NumberClassifier.isPalindrome(n)) statuses.append("palindrome ");
        if (NumberClassifier.isGapful(n)) statuses.append("gapful ");
        if (NumberClassifier.isEven(n)) statuses.append("even ");
        if (!NumberClassifier.isEven(n)) statuses.append("odd ");
        return statuses.toString().split(" ");
    }

    private static void printMenuOptions() {
        System.out.println("Supported requests:");
        System.out.println("- enter a natural number to know its properties;");
        System.out.println("- enter two natural numbers to obtain the properties of the list:");
        System.out.println("  * the first parameter represents a starting number;");
        System.out.println("  * the second parameter shows how many consecutive numbers are to be printed;");
        System.out.println("- separate the parameters with one space;");
        System.out.println("- enter 0 to exit.");
    }

    private static long[] parseRequest(String s) {
        return Arrays.stream(s.split(" "))
                .mapToLong(x -> Long.valueOf(x))
                .toArray();
    }

    private static boolean isValidInput(String s) {
        try {
            long[] temp = parseRequest(s);
            return (temp.length > 0 && temp.length <= 3) && NumberClassifier.isNatural(temp[0]);
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static void menu() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Amazing Numbers!\n");
        printMenuOptions();

        while (true) {
            System.out.println("\nEnter a request:");
            String rawInput = scanner.nextLine();

            if (rawInput.equals("0")) break;
            if (rawInput.length() == 0) {
                printMenuOptions();
            } else if (!isValidInput(rawInput)) {
                System.out.println("The first parameter should be a natural number or zero.");
            } else {
                long[] nums = parseRequest(rawInput);
                if (nums.length == 1) {
                    printSingleNumberProperties(nums[0]);
                } else {
                    if (!NumberClassifier.isNatural(nums[1])) {
                        System.out.println("The second parameter should be a natural number.");
                    } else {
                        printMultipleNumberProperties(nums[0], nums[1]);
                    }
                }
            }
        }
        System.out.println("Goodbye!");
    }

    public static void main(String[] args) {
        menu();
    }
}
