package numbers;

import java.util.Scanner;

public class Main {

    private static void printNumberProperties(long n){
        System.out.println("Properties of " + n);
        System.out.printf("%13s%n", "even: " + NumberClassifier.isEven(n));
        System.out.printf("%13s%n", "odd: " + !NumberClassifier.isEven(n));
        System.out.printf("%13s%n", "buzz: " + NumberClassifier.isBuzz(n));
        System.out.printf("%13s%n", "duck: " + NumberClassifier.isDuck(n));
        System.out.printf("%13s%n", "palindromic: " + NumberClassifier.isPalindrome(n));

    }

    public static void printMenuOptions(){
        System.out.println("Welcome to Amazing Numbers!\n");
        System.out.println("Supported requests:");
        System.out.println("- enter a natural number to know its properties;");
        System.out.println("- enter 0 to exit.");
    }


    public static void menu(){
        Scanner scanner = new Scanner(System.in);

        printMenuOptions();

        while(true) {
            System.out.println("\nEnter a request\n");
            long num = scanner.nextLong();

            if(num == 0) break;

            if(!NumberClassifier.isNatural(num)){
                System.out.println("The first parameter should be a natural number or zero.");
            } else {
                printNumberProperties(num);
            }
        }
        System.out.println("Goodbye!");
    }

    public static void main(String[] args) {
        menu();

    }
}
