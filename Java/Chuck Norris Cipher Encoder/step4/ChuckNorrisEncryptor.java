package chucknorris;

import java.lang.reflect.Array;
import java.util.Arrays;

public class ChuckNorrisEncryptor {

    public static String encrypt(String rawString) {
        StringBuilder s = new StringBuilder();
        for (char c : rawString.toCharArray()) {
            String binaryRepresentation = Integer.toBinaryString(c);
            s.append(binaryToNorris(binaryRepresentation));
        }
        return s.toString().trim();
    }

    public static String decrypt(String norrisString) {
        StringBuilder tempBinary = new StringBuilder();
        String joinedBinary = norrisToBinary(norrisString);
        for (int i = 0; i < joinedBinary.length(); i += 7) {
            tempBinary.append(joinedBinary, i, i + 7);
            tempBinary.append(" ");
        }
        String[] splitBinary = tempBinary.toString().split(" ");
        String decryptedString = binaryStringArrayToString(splitBinary);
        return decryptedString;
    }

    private static String binaryToNorris(String binString) {
        if (binString.length() == 6) binString = "0" + binString;

        StringBuilder s = new StringBuilder();
        int leftPointer = 0;
        while (leftPointer < binString.length()) {
            int tempPointer = leftPointer;
            int sameDigitCount = 0;

            while (tempPointer < binString.length() && (binString.charAt(tempPointer) == binString.charAt(leftPointer))) {
                sameDigitCount++;
                tempPointer++;
            }

            if (binString.charAt(leftPointer) == '1') s.append("0 ");
            else s.append("00 ");

            for (int i = 0; i < sameDigitCount; i++) {
                s.append("0");
            }

            leftPointer = tempPointer;
            s.append(" ");

        }
        return s.toString();
    }

    public static String norrisToBinary(String norrisString) {
        StringBuilder s = new StringBuilder();
        String[] splitItems = norrisString.split(" ");

        for (int i = 0; i < splitItems.length - 1; i += 2) {
            String currentChar = splitItems[i].equals("0") ? "1" : "0";
            for (int j = 0; j < splitItems[i + 1].length(); j++) {
                s.append(currentChar);
            }
        }
        return s.toString();
    }

    private static String binaryStringArrayToString(String[] binStrings) {
        StringBuilder s = new StringBuilder();
        for (int i = 0; i < binStrings.length; i++) {
            int charCode = Integer.parseInt(binStrings[i], 2);
            s.append((char) charCode);
        }
        return s.toString();
    }
}
