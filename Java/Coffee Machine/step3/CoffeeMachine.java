package machine;

import java.util.Arrays;
import java.util.Scanner;

public class CoffeeMachine {
    private static final Scanner scanner = new Scanner(System.in);

    private int water;
    private int milk;
    private int beans;
    private int cupsPossible;

    public CoffeeMachine(int water, int milk, int beans) {
        this.water = water;
        this.milk = milk;
        this.beans = beans;
        this.cupsPossible = calculateTotalCupsPossible();
    }

    public static void main(String[] args) {
        CoffeeMachine machine = generateMachine();

        System.out.println("Write how many cups of coffee you will need:");
        int cupsNeeded = scanner.nextInt();
        machine.displayCupsPossible(cupsNeeded);

    }


    private static CoffeeMachine generateMachine() {
        System.out.println("Write how many ml of water the coffee machine has:");
        int water = scanner.nextInt();
        System.out.println("Write how many ml of milk the coffee machine has:");
        int milk = scanner.nextInt();
        System.out.println("Write how many grams of coffee beans the coffee machine has:");
        int beans = scanner.nextInt();
        return new CoffeeMachine(water, milk, beans);
    }

    private void displayCupsPossible(int needed){
        if ( this.cupsPossible > needed){
            int surplus = this.cupsPossible - needed;
            System.out.println("Yes, I can make that amount of coffee (and even " + surplus + " more than that)");
        } else if (this.cupsPossible < needed){
            System.out.println("No, I can only make " + this.cupsPossible + " cup(s) of coffee");
        } else {
            System.out.println("Yes, I can make that amount of coffee");
        }
    }
    private int calculateTotalCupsPossible() {
        int cupsPossible[] = {water / 200, milk / 50, beans / 15};
        return Arrays.stream(cupsPossible).min().getAsInt();
    }


    private static int calculateIngredient(int cups, String ingredient) {
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
