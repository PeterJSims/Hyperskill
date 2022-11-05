package bullscows;

import java.util.Scanner;

public class Main {
    static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {

        String number = scanner.next();
        String answer = NumberGenerator.FIXED_NUMBER;

        ResultsPrinter.printResults(number, answer);
    }
}
