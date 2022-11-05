package bullscows;

public class ResultsGenerator {

    protected static String getResultsString(String userString, String answerString) {
        int[] results = BullsCowsCalculator.generateCounts(userString, answerString);

        return generateResultsString(results);
    }


    protected static String getBlankSecret(int length) {
        StringBuilder s = new StringBuilder();
        for (int i = 0; i < length; i++) {
            s.append("*");
        }
        return s.toString();
    }

    protected static String getSymbolRangeString(int symbolCount) {
        String nums = getNumRangeString(symbolCount);
        String letters = getAlphabetRangeString(symbolCount);
        if (letters.isEmpty()) {
            return nums;
        } else {
            return nums + ", " + letters;
        }

    }


    private static String getNumRangeString(int symbolCount) {
        if (symbolCount > 10) {
            return "0-9";
        } else {
            char endChar = NumberGenerator.FULL_RANGE.charAt(symbolCount - 1);
            return "0-" + endChar;
        }
    }

    private static String getAlphabetRangeString(int symbolCount) {
        if (symbolCount == 36) {
            return "a-z";
        } else if (symbolCount < 11) {
            return "";
        } else {
            char endChar = NumberGenerator.FULL_RANGE.charAt(symbolCount - 1);
            return "a-" + endChar;
        }
    }


    private static String generateResultsString(int[] results) {
        StringBuilder s = new StringBuilder();

        if (results[0] > 0) {
            if (results[0] == 1) s.append("1 bull");
            else s.append(results[0] + " bulls");
        }
        if (results[0] > 0 && results[1] > 0) {
            s.append(" and ");
        }
        if (results[1] > 0) {
            if (results[1] == 1) s.append("1 cow");
            else s.append(results[1] + " cows");
        }
        return "Grade: " + (s.isEmpty() ? "None" : s.toString());

    }
}
