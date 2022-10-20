package numbers;

import java.util.Scanner;

public class Main {

    private static void printNumberFacts(int n){
        System.out.println("This number is " + NumberClassifier.returnEvenOddString(n) + ".");
        System.out.println("It is" + (NumberClassifier.isBuzz(n) ? " ":" not ") + "a Buzz number.");
        System.out.println("Explanation:");
        System.out.println(n + " " + NumberClassifier.buzzExplanation(n) + ".");
    }
    private static void printNumberProperties(int n){
        System.out.println("Properties of " + n);
        System.out.printf("%13s%n", "even: " + NumberClassifier.isEven(n));
        System.out.printf("%13s%n", "odd: " + !NumberClassifier.isEven(n));
        System.out.printf("%13s%n", "buzz: " + NumberClassifier.isBuzz(n));
        System.out.printf("%13s%n", "duck: " + NumberClassifier.isDuck(n));

    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a natural number");
        int num = scanner.nextInt();
        if(!NumberClassifier.isNatural(num)){
            System.out.println("This number is not natural!");
        } else {
            printNumberProperties(num);
        }
    }
}
