package bullscows;

import java.util.Arrays;

public class NumberGenerator {
    protected static final String FULL_RANGE = "0123456789abcdefghijklmnopqrstuvwxyz";
    protected static final int MAX_LENGTH = FULL_RANGE.length();


    public static String generateSecretNumber(int length, int charAmount) {
        char[] items = FULL_RANGE.substring(0, charAmount).toCharArray();
        shuffle(items);
        String randomizedNumber = String.valueOf(items);
        return randomizedNumber.substring(0, length);
    }


    private static void shuffle(char[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int r = i + (int) (Math.random() * (n - i));
            char swap = arr[r];
            arr[r] = arr[i];
            arr[i] = swap;
        }
        if (arr[0] == '0') { // random numbers should not start with 0
            char temp = arr[0];
            int r = (int) (Math.random() * (n));
            arr[0] = arr[r];
            arr[r] = temp;
        }
    }
}
