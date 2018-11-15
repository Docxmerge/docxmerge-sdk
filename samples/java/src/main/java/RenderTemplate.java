import com.docxmerge.Docxmerge;

import java.io.File;
import java.util.HashMap;
import java.util.logging.Logger;

public class RenderTemplate {
    private static Logger logger = Logger.getLogger(RenderTemplate.class.getName());

    public static void main(String[] args) throws Exception {
        // get instance
        Docxmerge docxmerge = Utils.getDocxmerge(args);

        // get docx to render
        File templateToRender = Utils.getFile("helloworld.docx");
        // prepare data
        HashMap<String, Object> data = new HashMap<String, Object>();
        data.put("hello_world", "Hello world!");

        // render file
        File resultFile = docxmerge.renderFile(templateToRender, data);

        // save file
        File savedFile = Utils.saveFile(resultFile, "helloworld.pdf");
        logger.info(String.format("File saved to %s", savedFile.getAbsolutePath()));
    }
}
