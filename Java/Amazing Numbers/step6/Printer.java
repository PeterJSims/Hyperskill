package numbers;

import java.util.Arrays;

public class Printer {
    protected static void printSingleNumberProperties(long n) {
        System.out.println("Properties of " + n);
        System.out.println("        buzz: " + NumberClassifier.isBuzz(n));
        System.out.println("        duck: " + NumberClassifier.isDuck(n));
        System.out.println(" palindromic: " + NumberClassifier.isPalindrome(n));
        System.out.println("      gapful: " + NumberClassifier.isGapful(n));
        System.out.println("         spy: " + NumberClassifier.isSpy(n));
        System.out.println("      square: " + NumberClassifier.isSquare(n));
        System.out.println("       sunny: " + NumberClassifier.isSunny(n));
        System.out.println("        even: " + NumberClassifier.isEven(n));
        System.out.println("         odd: " + !NumberClassifier.isEven(n));

    }

    protected static void printMultipleNumberProperties(long n, long count) {
        System.out.println();
        for (long i = n; i < n + count; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(" ");
            }
            System.out.println(i + " is " + String.join(", ", InputProcessor.generateStatusArray(i)));
        }
    }

    protected static void printMultipleNumberProperties(long n, long count, String property) {
        System.out.println();
        for (long i = n; count > 0; i++) {
            String[] returnedProperties = InputProcessor.generateStatusArray(i);
            for (String item : returnedProperties) {
                if (item.equalsIgnoreCase(property)) {
                    for (int j = 0; j < 10; j++) {
                        System.out.print(" ");
                    }
                    System.out.println(i + " is " + String.join(", ", returnedProperties));
                    count--;
                }
            }
        }
    }

    protected static void printMultipleNumberProperties(long n, long count, String[] properties) {
        System.out.println();
        for (long i = n; count > 0; i++) {
            String[] returnedProperties = InputProcessor.generateStatusArray(i);
            if (Arrays.asList(returnedProperties).containsAll(Arrays.asList(properties))) {
                for (int j = 0; j < 10; j++) {
                    System.out.print(" ");
                }
                System.out.println(i + " is " + String.join(", ", returnedProperties));
                count--;
            }
        }
    }


    protected static void printBadPropertyInfo(String property) {
        System.out.println("The property [" + property.toUpperCase() + "] is wrong.");
        System.out.print("Available properties: [" + " "
                + String.join(", ", Menu.PROPERTIES) + "]");
    }

    protected static void printMultipleBadProperties(String properties) {
        System.out.println("The properties [" + properties.toUpperCase() + "] are wrong.");
        System.out.print("Available properties: [" + " "
                + String.join(", ", Menu.PROPERTIES) + "]");
    }

    protected static void printMutuallyExclusiveProperties(String properties) {
        System.out.println("The request contains mutually exclusive properties: [" + properties + "]");
        System.out.println("There are no numbers with these properties.");
    }

    protected static void printMenuOptions() {
        System.out.println("Supported requests:");
        System.out.println("- enter a natural number to know its properties;");
        System.out.println("- enter two natural numbers to obtain the properties of the list:");
        System.out.println("  * the first parameter represents a starting number;");
        System.out.println("  * the second parameter shows how many consecutive numbers are to be printed;");
        System.out.println("- two natural numbers and two properties to search for;;");
        System.out.println("- separate the parameters with one space;");
        System.out.println("- enter 0 to exit.");
    }


}
