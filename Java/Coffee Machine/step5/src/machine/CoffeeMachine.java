package machine;

import java.util.Arrays;
import java.util.Scanner;

public class CoffeeMachine {
    private static final Scanner scanner = new Scanner(System.in);

    private int money;
    private int water;
    private int milk;
    private int beans;
    private int cups;


    public CoffeeMachine(int money, int water, int milk, int beans, int cups) {
        this.money = money;
        this.water = water;
        this.milk = milk;
        this.beans = beans;
        this.cups = cups;
    }

    public CoffeeMachine() {
        this(550, 400, 540, 120, 9);
    }

    public static void main(String[] args) {
        CoffeeMachine machine = new CoffeeMachine();

        while (true) {
            System.out.println("Write action (buy, fill, take, remaining, exit):");
            String action = scanner.next();
            System.out.println();
            if (action.equalsIgnoreCase("buy")) machine.buy();
            else if (action.equalsIgnoreCase("fill")) machine.fill();
            else if (action.equalsIgnoreCase("take")) {
                int fullMoney = machine.take();
                System.out.println("I give you $" + fullMoney);
            } else if (action.equalsIgnoreCase("remaining")) System.out.println(machine);
            else break;
        }

    }

    public void buy() {
        System.out.println("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ");
        String choice = scanner.next();
        switch (choice) {
            case "1":
                if (canMakeCup(250, 1, 16)) {
                    printSuccess();
                    System.out.println("I have enough resources, making you a coffee!");
                    this.water -= 250;
                    this.beans -= 16;
                    this.money += 4;
                    this.cups--;
                } else {
                    System.out.print("Sorry, not enough " + returnMissingItem(250, 1, 16) + "!");
                }
                break;
            case "2":
                if (canMakeCup(350, 75, 20)) {
                    printSuccess();
                    this.water -= 350;
                    this.milk -= 75;
                    this.beans -= 20;
                    this.money += 7;
                    this.cups--;
                } else {
                    System.out.print("Sorry, not enough " + returnMissingItem(330, 75, 20) + "!");
                }
                break;
            case "3":
                if (canMakeCup(200, 100, 12)) {
                    printSuccess();
                    this.water -= 200;
                    this.milk -= 100;
                    this.beans -= 12;
                    this.money += 6;
                    this.cups--;
                } else {
                    System.out.print("Sorry, not enough " + returnMissingItem(200, 100, 12) + "!");
                }
                break;
            default:
                break;
        }
    }

    public void fill() {
        System.out.println("Write how many ml of water you want to add:");
        int addedWater = scanner.nextInt();
        System.out.println("Write how many ml of milk you want to add:");
        int addedMilk = scanner.nextInt();
        System.out.println("Write how many grams of coffee beans you want to add:");
        int addedBeans = scanner.nextInt();
        System.out.println("Write how many disposable cups you want to add:");
        int addedCups = scanner.nextInt();
        this.water += addedWater;
        this.milk += addedMilk;
        this.beans += addedBeans;
        this.cups += addedCups;
    }

    public int take() {
        int takenMoney = this.money;
        this.money = 0;
        return takenMoney;
    }

    private boolean canMakeCup(int waterNeeded, int milkNeeded, int beansNeeded) {
        int cupsPossible[] = {water / waterNeeded, milk / milkNeeded, beans / beansNeeded};
        return Arrays.stream(cupsPossible).min().getAsInt() > 0 && this.cups > 0;
    }

    private void printSuccess() {
        System.out.println("I have enough resources, making you a coffee!");
    }

    private String returnMissingItem(int waterNeeded, int milkNeeded, int beansNeeded) {
        if (waterNeeded > this.water) return "water";
        else if (milkNeeded > this.milk) return "milk";
        else if (beansNeeded > this.beans) return "beans";
        else if (this.cups == 0) return "cups";
        else return "";
    }

    @Override
    public String toString() {
        return "\nThe coffee machine has:\n" +
                this.water + " ml of water\n" +
                this.milk + " ml of milk\n" +
                this.beans + " g of coffee beans\n" +
                this.cups + " disposable cups\n" +
                this.money + " of money\n";
    }
}
