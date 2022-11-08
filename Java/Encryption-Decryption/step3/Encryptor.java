package encryptdecrypt;

public class Encryptor {
    private static final int MIN = 97;
    private static final int MAX = 122;

    public static String encrypt(String originalString, int offset) {
        StringBuilder s = new StringBuilder();

        for (char c : originalString.toCharArray()) {
            s.append(encodeChar(c, offset));
        }
        return s.toString();
    }

    private static char encodeChar(char c, int offset) {
        return (char) (c + offset);
    }


//    public static String encrypt(String originalString, int offset) {
//        StringBuilder s = new StringBuilder();
//
//        for (char c : originalString.toCharArray()) {
//            if (c == ' ') {
//                s.append(" ");
//            } else if (Character.isAlphabetic(c)) {
//                s.append(encodeChar(c, offset));
//            } else {
//                s.append(c);
//            }
//        }
//        return s.toString();
//    }

//    private static char encodeChar(char c, int offset) {
//        int alphabetPosition = c - MIN; // 0-indexed alphabet position
//        int charInt = ((alphabetPosition + offset) % 26) + MIN;
//        char newChar = (char) charInt;
//        return newChar;
//    }


}
