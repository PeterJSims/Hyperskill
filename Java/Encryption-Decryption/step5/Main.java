package encryptdecrypt;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] parsedArgs = parseArgs(args);
        start(parsedArgs);
    }

    private static void start(String[] args) throws IOException {
        String mode = args[0];
        int offset = Integer.valueOf(args[1]);
        String data = args[2];
        String in = args[3];
        String out = args[4];

        if (data.isEmpty() && !in.isEmpty()) {
            byte[] encoded = Files.readAllBytes(Paths.get(in));
            data = new String(encoded);
        }
        if (mode.equalsIgnoreCase("dec")) offset = -offset;

        String result = Encryptor.encrypt(data, offset);

        if (!out.isEmpty()) {
            try (FileWriter f = new FileWriter(out)) {
                f.write(result);
            } catch (Exception e) {
                System.out.println("Error writing to file");
            }
        } else {
            System.out.println(result);
        }
    }


    private static String[] parseArgs(String[] args) {
        HashMap<String, String> argsMap = argsToMap(args);
        String[] parsedArgs = new String[5];

        parsedArgs[0] = argsMap.getOrDefault("-mode", "enc");
        parsedArgs[1] = argsMap.getOrDefault("-key", "0");
        parsedArgs[2] = argsMap.getOrDefault("-data", "");
        parsedArgs[3] = argsMap.getOrDefault("-in", "");
        parsedArgs[4] = argsMap.getOrDefault("-out", "");

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
