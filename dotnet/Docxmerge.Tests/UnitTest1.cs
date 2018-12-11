using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Threading.Tasks;
using Xunit;

namespace Docxmerge.Tests
{
    public class UnitTest1
    {
        private const string tenantId = "f60b0638-2f2e-4f92-b027-39cedfa06d4d";
        private const string apikey = "8f22c304d0b44af2b03c2ad3d1aa5471";

        [Fact]
        public async Task TestMerge()
        {
            var docxmerge = GetDocxmerge();
            var fileStream = File.Open("./helloworld.docx", FileMode.Open);
            var stream = await docxmerge.MergeTemplate(tenantId, fileStream, new Dictionary<string, object>
            {
                {"hello_world", "Hello world"}
            });
            var destFile = File.OpenWrite("./helloworld_merged.docx");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        [Fact]
        public async Task TestConversion()
        {
            var docxmerge = GetDocxmerge();
            var fileStream = File.Open("./helloworld.docx", FileMode.Open);
            var stream = await docxmerge.ConvertFile(tenantId, fileStream);
            var destFile = File.OpenWrite("./helloworld_convert.docx");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        [Fact]
        public async Task TestTemplateConversion()
        {
            var docxmerge = GetDocxmerge();
            var stream =
                await docxmerge.ConvertTemplate(tenantId, "Hello world", 1, new Dictionary<string, string> { });
            var destFile = File.OpenWrite("./helloworld_convert_2.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        [Fact]
        public async Task TestPrint()
        {
            var docxmerge = GetDocxmerge();
            var fileStream = File.Open("./helloworld.docx", FileMode.Open);
            var stream = await docxmerge.RenderFile(tenantId, fileStream, new Dictionary<string, object>
            {
                {"hello_world", "Hello world"}
            });
            var destFile = File.OpenWrite("./helloworld.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        private Docxmerge GetDocxmerge()
        {
            return new Docxmerge(apikey, "http://localhost:5030");
        }
    }
}