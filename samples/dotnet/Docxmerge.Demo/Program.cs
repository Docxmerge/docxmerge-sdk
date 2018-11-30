using System;
using System.Collections.Generic;
using System.IO;

namespace Docxmerge.Demo
{
    class Program
    {
        static void Main(string[] args)
        {
            var apikey = "75387ac868534e3d87060aed01167741";
            var tenantId = "ebc068c6-d817-499b-aea1-c04354b23d04";
            var docxmerge = new Docxmerge(apikey);
            var fileStream = File.Open("./helloworld.docx", FileMode.Open);
            var stream = docxmerge.RenderFile(tenantId, fileStream, new Dictionary<string, object>
            {
                {"hello_world", "Hello world"}
            }).Result;
            var destFile = File.OpenWrite("./helloworld.pdf");
            stream.CopyTo(destFile);
            destFile.Close();
        }
    }
}