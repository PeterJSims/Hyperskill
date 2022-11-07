package chucknorris;

import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Input string:");
        String userInput = scanner.nextLine();
        System.out.println(String.join(" ", userInput.split("")));

    }
}