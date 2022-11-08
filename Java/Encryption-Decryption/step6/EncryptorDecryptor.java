package encryptdecrypt;

public class EncryptorDecryptor {
    public static String unicode(String originalString, int offset) {
        StringBuilder s = new StringBuilder();

        for (char c : originalString.toCharArray()) {
            s.append(unicodeEncodeChar(c, offset));
        }

        return s.toString();
    }

    public static String caesar(String originalString, int offset) {
        if (offset < 0) offset = 26 + offset; // adjust offset for decoding

        StringBuilder s = new StringBuilder();

        for (char c : originalString.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                s.append(caesarEncodeChar(c, offset));
            } else {
                s.append(c);
            }
        }
        return s.toString();
    }


    private static char unicodeEncodeChar(char c, int offset) {
        return (char) (c + offset);
    }


    private static char caesarEncodeChar(char c, int offset) {
        int MIN = Character.isUpperCase(c) ? 65 : 97; // Respective char codes for 'A' and 'a'
        int alphabetPosition = c - MIN; // 0-indexed alphabet position
        int charInt = ((alphabetPosition + offset) % 26) + MIN;
        char newChar = (char) charInt;
        return newChar;
    }


}
