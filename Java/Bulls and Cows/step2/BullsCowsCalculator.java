package bullscows;

public class BullsCowsCalculator {
    protected static int bullsCalculator(String numOne, String numTwo) {
        assert numOne.length() == numTwo.length();

        int bullsCount = 0;
        char[] splitNumOne = numOne.toCharArray();
        char[] splitNumTwo = numTwo.toCharArray();
        for (int i = 0; i < splitNumOne.length; i++) {
            if (splitNumOne[i] == splitNumTwo[i]) bullsCount++;
        }
        return bullsCount;
    }

    protected static int cowsCalculator(String numOne, String numTwo) {
        assert numOne.length() == numTwo.length();

        int cowsCount = 0;
        char[] splitNumOne = numOne.toCharArray();
        for (char c : splitNumOne) {
            if (numTwo.indexOf(c) != -1) cowsCount++;
        }
        cowsCount = cowsCount - bullsCalculator(numOne, numTwo); // Cows count is dependent on bulls count
        return cowsCount;
    }


    protected static int[] generateCounts(String numOne, String numTwo) {
        return new int[]{bullsCalculator(numOne, numTwo), cowsCalculator(numOne, numTwo)};
    }

}
