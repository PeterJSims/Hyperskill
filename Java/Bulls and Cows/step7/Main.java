package bullscows;

import java.util.Scanner;

public class Main {
    static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String gameNumberString = generateGameNumber();
        if (!gameNumberString.isEmpty()) game(gameNumberString);
    }

    private static String generateGameNumber() {
        int length;
        int symbolCount;
        System.out.println("Please, enter the secret code's length:");
        String lengthString = scanner.next();

        if (InputValidator.isValidInput(lengthString)) {
            length = Integer.valueOf(lengthString);
        } else {
            return "";
        }

        if (!InputValidator.isValidLength(length)) return "";


        System.out.println("Input the number of possible symbols in the code:");
        String symbolCountString = scanner.next();

        if (InputValidator.isValidInput(symbolCountString)) {
            symbolCount = Integer.valueOf(symbolCountString);
        } else {
            return "";
        }

        if (!InputValidator.isValidSymbolAmount(symbolCount, length)) return "";

        String secretNumber = NumberGenerator.generateSecretNumber(length, symbolCount);
        String stars = ResultsGenerator.getBlankSecret(length);
        String range = ResultsGenerator.getSymbolRangeString(symbolCount);
        System.out.println("The secret is prepared: " + stars + " (" + range + ").");
        return secretNumber;
    }


    private static void game(String secretNumber) {
        int n = secretNumber.length();

        System.out.println("Okay, let's start a game!");

        boolean isFinished = false;
        int turn = 1;
        while (!isFinished) {
            System.out.println("Turn " + turn + ":");
            String guess = scanner.next();
            if (guess.length() != n) {
                System.out.println("Please enter a guess of length " + n + ".");
                continue;
            }
            System.out.println(ResultsGenerator.getResultsString(guess, secretNumber));
            isFinished = BullsCowsCalculator.isGameFinished(guess, secretNumber);
            turn++;
        }

        System.out.println("Congratulations! You guessed the secret code!");
    }
}
