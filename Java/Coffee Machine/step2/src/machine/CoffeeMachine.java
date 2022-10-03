package machine;

import java.util.Scanner;

public class CoffeeMachine {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Write how many cups of coffee you will need:");
        int cups = scanner.nextInt();

        System.out.print("For " + cups + (cups == 1 ? " cup " : " cups ") + "of coffee you will need:");
        System.out.println(calculateIngredient(cups, "water") + " ml of water");
        System.out.println(calculateIngredient(cups, "milk") + " ml of milk");
        System.out.println(calculateIngredient(cups, "beans") + " g of coffee beans");


    }

    public static int calculateIngredient(int cups, String ingredient) {
        int returnedMeasurement = 0;
        switch (ingredient) {
            case "water":
                returnedMeasurement = cups * 200;
                break;
            case "milk":
                returnedMeasurement = cups * 50;
                break;
            case "beans":
                returnedMeasurement = cups * 15;
            default:
                break;
        }
        return returnedMeasurement;
    }
}
