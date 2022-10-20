package numbers;

import java.util.Scanner;

public class Main {

    private static void printNumberFacts(int n) {
        System.out.println("This number is " + NumberClassifier.returnEvenOddString(n) + ".");
        System.out.println("It is" + (NumberClassifier.isBuzz(n) ? " " : " not ") + "a Buzz number.");
        System.out.println("Explanation:");
        System.out.println(n + " " + NumberClassifier.buzzExplanation(n) + ".");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a natural number");
        int num = scanner.nextInt();
        if (!NumberClassifier.isNatural(num)) {
            System.out.println("This number is not natural!");
        } else {
            printNumberFacts(num);
        }
    }
}
