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
        private const string tenantId = "de9a2bfd-86be-470d-a549-bd09fb1b1d2b";
        private const string apikey = "06a468217a55439690c4eefbb94791e4";
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