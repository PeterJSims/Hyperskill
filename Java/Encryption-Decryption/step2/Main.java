package encryptdecrypt;

import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String plainString = scanner.nextLine();
        int offset = scanner.nextInt();
        System.out.println(Encryptor.encrypt(plainString, offset));

    }
}
