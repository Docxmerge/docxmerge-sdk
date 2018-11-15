import com.docxmerge.Docxmerge;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.nio.channels.FileChannel;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Utils {
    public static Docxmerge getDocxmerge(String[] args) throws Exception {
        String apiKey = args[0];
        String tenantId = args[1];
        if (apiKey.isEmpty()) {
            throw new Exception("Api key is null");
        }
        if (tenantId.isEmpty()) {
            throw new Exception("Tenant id is null");
        }
        return new Docxmerge(apiKey, tenantId);
    }

    public static String getPathFile(String path) {
        Path filePath = Paths.get("src", "main", "resources", path);
        return filePath.toString();
    }

    public static File getFile(String file) {
        return new File(getPathFile(file));
    }

    public static File saveFile(File file, String output) throws Exception {
        File dest = new File(getPathFile(output));
        FileChannel sourceChannel = null;
        FileChannel destChannel = null;
        try {
            sourceChannel = new FileInputStream(file).getChannel();
            destChannel = new FileOutputStream(dest).getChannel();
            destChannel.transferFrom(sourceChannel, 0, sourceChannel.size());
        } finally {
            sourceChannel.close();
            destChannel.close();
        }
        return dest;
    }
}
