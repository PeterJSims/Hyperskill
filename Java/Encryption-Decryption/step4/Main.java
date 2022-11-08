package encryptdecrypt;

import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        String[] parsedArgs = parseArgs(args);
        start(parsedArgs);
    }

    private static void start(String[] args) {
        String mode = args[0];
        int offset = Integer.valueOf(args[1]);
        String plainString = args[2];

        if (mode.equalsIgnoreCase("dec")) offset = -offset;

        if (plainString.isBlank()) System.out.println("");
        else System.out.println(Encryptor.encrypt(plainString, offset));
    }


    private static String[] parseArgs(String[] args) {
        HashMap<String, String> argsMap = argsToMap(args);
        String[] parsedArgs = new String[3];

        parsedArgs[0] = argsMap.getOrDefault("-mode", "enc");
        parsedArgs[1] = argsMap.getOrDefault("-key", "0");
        parsedArgs[2] = argsMap.getOrDefault("-data", "");

        return parsedArgs;
    }

    private static HashMap<String, String> argsToMap(String[] args) {
        HashMap<String, String> argsMap = new HashMap<>();
        for (int i = 0; i < args.length; i += 2) {
            argsMap.put(args[i], args[i + 1]);
        }
        return argsMap;
    }
}
