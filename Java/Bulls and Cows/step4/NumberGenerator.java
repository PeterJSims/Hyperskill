package bullscows;

public class NumberGenerator {
    final static String FIXED_NUMBER = "9305";
    private static final String ONE_TO_TEN = "0123456789";


    public static String generateSecretNumber(int n) {
        char[] nums = ONE_TO_TEN.toCharArray();
        shuffle(nums);
        String randomizedNumber = String.valueOf(nums);
        return randomizedNumber.substring(0, n);

    }

    private static void shuffle(char[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int r = i + (int) (Math.random() * (n - i));
            char swap = arr[r];
            arr[r] = arr[i];
            arr[i] = swap;
        }
        if(arr[0] == '0'){ // random numbers should not start with 0
            char temp = arr[0];
            int r = (int) (Math.random() * (n));
            arr[0] = arr[r];
            arr[r] = temp;
        }
    }
}
