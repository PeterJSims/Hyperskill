package bullscows;

public class ResultsGenerator {

    protected static void generateResultsString(String userString, String answerString){
        int[] results = BullsCowsCalculator.generateCounts(userString, answerString);

        System.out.println("Grade: " + generateResultsString(generateResults(results)) + ". The secret code is " + answerString + ".");

    }


    private static String generateResults(int[] results){
        StringBuilder s = new StringBuilder();
        if(results[0] > 0) {
            s.append(results[0] + " bull(s)");
        }
        if(results[0] > 0 && results[1] > 0){
            s.append(" and ");
        }
        if(results[1] > 0){
            s.append(results[1] + " cow(s)");
        }
        return "Grade: " + (s.isEmpty() ? "None" : s.toString());

    }
}
