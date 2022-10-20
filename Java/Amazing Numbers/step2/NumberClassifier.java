package numbers;

public class NumberClassifier {

    public static String returnEvenOddString(int n){
        return n % 2 == 0 ? "Even" : "Odd";
    }
    public static boolean isEven(int n){
        return n % 2 == 0;
    }

    public static boolean isNatural(int n){
        return n > 0;
    }

    public static boolean isBuzz(int n){
        return n % 7 == 0 || n % 10 == 7;
    }

    public static boolean isDuck(int n){
        String numString = String.valueOf(n);
        return numString.contains("0");
    }

    protected static String buzzExplanation(int n){
        if(!isBuzz(n)) return "is neither divisible by 7 nor does it end with 7";

        final String CONDITION_ONE = "is divisible by 7";
        final String CONDITION_TWO = "ends with 7";
        int lastDigit = n % 10;
        if(lastDigit == 7 && lastDigit % 7 == 0){
            return CONDITION_ONE + " and " + CONDITION_TWO;
        } else if(n % 7 == 0){
            return CONDITION_ONE;
        } else {
            return CONDITION_TWO;
        }
    }

}
