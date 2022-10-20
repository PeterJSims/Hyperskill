package numbers;

import java.util.Arrays;

public class InputProcessor {
    protected static String[] generateStatusArray(long n) {
        StringBuilder statuses = new StringBuilder();
        if (NumberClassifier.isBuzz(n)) statuses.append("buzz ");
        if (NumberClassifier.isDuck(n)) statuses.append("duck ");
        if (NumberClassifier.isPalindrome(n)) statuses.append("palindromic ");
        if (NumberClassifier.isGapful(n)) statuses.append("gapful ");
        if (NumberClassifier.isEven(n)) statuses.append("even ");
        if (!NumberClassifier.isEven(n)) statuses.append("odd ");
        if (NumberClassifier.isSpy(n)) statuses.append("spy ");
        return statuses.toString().split(" ");
    }


    protected static long[] parseRequest(String s) {
        return Arrays.stream(s.split(" "))
                .mapToLong(x -> Long.valueOf(x))
                .toArray();
    }

    protected static boolean isValidInput(String s) {
        try {
            long[] temp = parseRequest(s);
            return (temp.length > 0 && temp.length <= 3) && NumberClassifier.isNatural(temp[0]);
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static boolean isValidProperty(String s) {
        for (String property : Main.PROPERTIES) {
            if (property.equalsIgnoreCase(s)) return true;
        }
        return false;
    }
}
