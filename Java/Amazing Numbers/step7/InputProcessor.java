package numbers;

import java.util.Arrays;

public class InputProcessor {
    protected static String[] generateStatusArray(long n) {
        StringBuilder statuses = new StringBuilder();
        if (NumberClassifier.isBuzz(n)) statuses.append("buzz ");
        if (NumberClassifier.isDuck(n)) statuses.append("duck ");
        if (NumberClassifier.isPalindrome(n)) statuses.append("palindromic ");
        if (NumberClassifier.isGapful(n)) statuses.append("gapful ");
        if (NumberClassifier.isSpy(n)) statuses.append("spy ");
        if (NumberClassifier.isSquare(n)) statuses.append("square ");
        if (NumberClassifier.isSunny(n)) statuses.append("sunny ");
        if (NumberClassifier.isJumping(n)) statuses.append("jumping ");
        if (NumberClassifier.isEven(n)) statuses.append("even ");
        if (!NumberClassifier.isEven(n)) statuses.append("odd ");
        return statuses.toString().split(" ");
    }


    protected static long[] parseRequest(String s) {
        return Arrays.stream(s.split(" "))
                .mapToLong(x -> Long.valueOf(x))
                .toArray();
    }

    protected static String[] parseProperties(String[] s) {
        if (s.length <= 2) throw new IllegalArgumentException("Array must contain one or more parameters");
        String[] props = new String[s.length - 2];

        // Transfer all items n=2+ from first array to new array
        for (int i = 2; i < s.length; i++) {
            props[i - 2] = s[i].toLowerCase();
        }
        return props;
    }

    protected static String getMutuallyExclusivePair(String[] properties) {
        String[] evenOdd = {"even", "odd"};
        String[] duckSpy = {"duck", "spy"};
        String[] sunnySquare = {"sunny", "square"};
        if (Arrays.asList(properties).containsAll(Arrays.asList(evenOdd))) return "EVEN, ODD";
        else if (Arrays.asList(properties).containsAll(Arrays.asList(duckSpy))) return "DUCK, SPY";
        else if (Arrays.asList(properties).containsAll(Arrays.asList(sunnySquare))) return "SUNNY, SQUARE";
        return "";
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
        for (String property : Menu.PROPERTIES) {
            if (property.equalsIgnoreCase(s)) return true;
        }
        return false;
    }
}
