package bullscows;

public class ResultsGenerator {

    public static String getResultsString(String userString, String answerString) {
        int[] results = BullsCowsCalculator.generateCounts(userString, answerString);

        return generateResultsString(results);
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
