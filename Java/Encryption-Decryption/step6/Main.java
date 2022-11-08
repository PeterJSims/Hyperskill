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
        String inPath = args[3];
        String outPath = args[4];
        String alg = args[5];
        String result;

        if (data.isEmpty() && !inPath.isEmpty()) {
            byte[] encoded = Files.readAllBytes(Paths.get(inPath));
            data = new String(encoded);
        }

        // Below is all that is needed to avoid specific decode methods
        if (mode.equalsIgnoreCase("dec")) offset = -offset;


        if (alg.equalsIgnoreCase("shift")) {
            result = EncryptorDecryptor.caesar(data, offset);
        } else {
            result = EncryptorDecryptor.unicode(data, offset);
        }

        if (!outPath.isEmpty()) {
            try (FileWriter f = new FileWriter(outPath)) {
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
        String[] parsedArgs = new String[6];

        parsedArgs[0] = argsMap.getOrDefault("-mode", "enc");
        parsedArgs[1] = argsMap.getOrDefault("-key", "0");
        parsedArgs[2] = argsMap.getOrDefault("-data", "");
        parsedArgs[3] = argsMap.getOrDefault("-in", "");
        parsedArgs[4] = argsMap.getOrDefault("-out", "");
        parsedArgs[5] = argsMap.getOrDefault("-alg", "shift");

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
