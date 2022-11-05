package bullscows;

public class InputValidator {

    protected static boolean isValidInput(String inputString) {
        try {
            int num = Integer.valueOf(inputString);
            return true;
        } catch (Exception e) {
            System.out.println("Error: \"" + inputString + "\" isn't a valid number.");
            return false;
        }
    }


    protected static boolean isValidLength(int length) {
        if (length > NumberGenerator.MAX_LENGTH) {
            System.out.println("Error: can't generate a secret number with a length of " + length +
                    " because there aren't enough unique characters.");
            return false;
        } else if (length <= 0) {
            System.out.println("Error: the secret code's length must be longer than 0.");
            return false;
        }
        return true;
    }

    protected static boolean isValidSymbolAmount(int symbolCount, int length) {

        if (symbolCount < length) {
            System.out.println("Error: can't generate a secret number with less unique characters than the length.");
            return false;
        } else if (symbolCount > NumberGenerator.MAX_LENGTH) {
            System.out.println("Error: can't generate a secret number with more than " + NumberGenerator.MAX_LENGTH + " different characters.");
            return false;
        }
        return true;
    }
}
