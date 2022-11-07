package chucknorris;

public class ChuckNorrisEncryptor {

    public static String encrypt(String rawString) {
        StringBuilder s = new StringBuilder();
        for (char c : rawString.toCharArray()) {
            String binaryRepresentation = Integer.toBinaryString(c);
            s.append(binaryToNorris(binaryRepresentation));
        }
        return s.toString().trim();
    }



    public static String binaryToNorris(String binString) {
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
}
