package encryptdecrypt;

import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        start();
    }

    private static void start(){
        String mode = scanner.nextLine();
        String plainString = scanner.nextLine();
        int offset = scanner.nextInt();

        if(mode.equalsIgnoreCase("dec")) offset = -offset;

        System.out.println(Encryptor.encrypt(plainString, offset));
    }
}
