package bullscows;

import java.util.Scanner;

public class Main {
    static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        game(generateGameNumber());
    }


    private static String generateGameNumber() {
        System.out.println("Please, enter the secret code's length:");
        int length = scanner.nextInt();

        while (length > NumberGenerator.MAX_LENGTH) {
            System.out.println("Error: can't generate a secret number with a length of " + length +
                    " because there aren't enough unique characters.");
            length = scanner.nextInt();
        }

        System.out.println("Input the number of possible symbols in the code:");
        int symbolCount = scanner.nextInt();

        while (symbolCount < length) {
            System.out.println("Error: can't generate a secret number with less unique characters than the length.");
            symbolCount = scanner.nextInt();
        }

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
