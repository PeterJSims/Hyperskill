package bullscows;

import java.util.Scanner;

public class Main {
    static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
//
//        String number = scanner.next();
//        String answer = NumberGenerator.FIXED_NUMBER;
//
//        ResultsPrinter.printResults(number, answer);

        int length = scanner.nextInt();

        if (length <= 10) {
            String secretNumberString = NumberGenerator.generateSecretNumber(length);
            System.out.println("The random secret number is " + secretNumberString + ".");
        } else {
            System.out.println("Error: can't generate a secret number with a length of " + length +
                    " because there aren't enough unique digits.");
        }

    }
}
