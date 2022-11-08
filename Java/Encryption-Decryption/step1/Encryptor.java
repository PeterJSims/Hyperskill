package encryptdecrypt;

public class Encryptor {
    private static final int MIN = 97;
    private static final int MAX = 122;

    public static String encrypt(String originalString) {
        StringBuilder s = new StringBuilder();

        for (char c : originalString.toCharArray()) {
            if (c == ' ') {
                s.append(" ");
            } else if (Character.isAlphabetic(c)) {
                s.append(encodeChar(c));
            } else {
                s.append(c);
            }
        }
        return s.toString();
    }

    private static char encodeChar(char c) {
        char newChar = (char) (MAX - c + MIN);
        return newChar;
    }
}
