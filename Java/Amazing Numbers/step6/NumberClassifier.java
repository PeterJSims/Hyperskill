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

    public static boolean isGapful(long n) {
        String numString = String.valueOf(n);
        if (numString.length() <= 2) return false;
        int firstLastNums = Integer.valueOf(numString.charAt(0) + "" + numString.charAt(numString.length() - 1));

        return n % firstLastNums == 0;
    }

    public static boolean isSpy(long n) {
        int sum = 0;
        int product = 1;
        String[] numStringArr = String.valueOf(n).split("");
        for (String s : numStringArr) {
            sum += Integer.valueOf(s);
            product *= Integer.valueOf(s);
        }
        return sum == product;
    }

    public static boolean isSquare(long n) {
        int squareRoot = (int) Math.sqrt(n);
        return squareRoot * squareRoot == n;
    }

    public static boolean isSunny(long n) {
        return isSquare(n + 1);
    }

}
