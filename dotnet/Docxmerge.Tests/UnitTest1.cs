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
        [Fact]
        public async Task Test1()
        {
            var apikey = "75387ac868534e3d87060aed01167741";
            var tenantId = "ebc068c6-d817-499b-aea1-c04354b23d04";
            var docxmerge = new Docxmerge(apikey, "http://localhost:5030");
            var fileStream = File.Open("./helloworld.docx", FileMode.Open);
            var stream = await docxmerge.MergeTemplate(tenantId, fileStream, new Dictionary<string, object>
            {
                {"hello_world", "Hello world-111"}
            });
            var destFile = File.OpenWrite("./helloworld_merged.docx");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }
    }
}