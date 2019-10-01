using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using Xunit;

namespace Docxmerge.Tests
{
    public class UnitTest1
    {
        private const string apikey = "26JZ5iPpD4U3b9z7lqkXeB2OGsbdF7";

        #region RenderTest

        [Fact]
        public async Task TestRenderTemplate()
        {
            var docxmerge = GetDocxmerge();
            var stream = await docxmerge.RenderTemplate("example-hello-world",
                new Dictionary<string, object>
                {
                    {"Enter Your name:", "Your name"}
                }, "PDF", "latest");
            var destFile = File.OpenWrite("./helloworld_merged.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        [Fact]
        public async Task TestRenderUrl()
        {
            var url =
                "https://api.docxmerge.com/api/v1/File/GetContenido?id=cdb9842d-5e38-4149-a06b-e1079a208fc3&download=true";
            var docxmerge = GetDocxmerge();
            var stream = await docxmerge.RenderUrl(url,
                new Dictionary<string, object>
                {
                    {"logo", "https://docxmerge.com/assets/android-chrome-512x512.png"},
                    {"name", "James Bond"},
                }, "PDF", "latest");
            var destFile = File.OpenWrite("./helloworld_merged.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }


        [Fact]
        public async Task TestRenderFile()
        {
            var docxmerge = GetDocxmerge();
            var fileStream = GetFile("./helloworld.docx");
            var stream = await docxmerge.RenderFile(fileStream,
                new Dictionary<string, object>
                {
                    {"hello_world", "Hello world"}
                }, "PDF");
            var destFile = File.OpenWrite("./helloworld_merged.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        #endregion

        private MemoryStream GetFile(string path)
        {
            return new MemoryStream(File.ReadAllBytes(path));
        }

        private Docxmerge GetDocxmerge()
        {
            return new Docxmerge(apikey, baseUrl: "http://localhost:5101");
        }
    }
}