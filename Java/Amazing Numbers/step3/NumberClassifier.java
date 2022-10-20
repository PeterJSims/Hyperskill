package numbers;

public class NumberClassifier {
    
    public static boolean isEven(long n) {
        return n % 2 == 0;
    }

    public static boolean isNatural(long n) {
        return n > 0;
    }

    public static boolean isBuzz(long n) {
        return n % 7 == 0 || n % 10 == 7;
    }

    public static boolean isDuck(long n) {
        String numString = String.valueOf(n);
        return numString.contains("0");
    }

    public static boolean isPalindrome(long n) {
        String numString = String.valueOf(n);
        for (int i = 0; i < numString.length() / 2; i++) {
            if (numString.charAt(i) != numString.charAt(numString.length() - 1 - i)) return false;
        }
        return true;
    }

}
