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
        private const string apikey = "BUl4qf5pKZZpaSWL9bIuz6bgjJ5ka0";

        #region MergeTest

        [Fact]
        public async Task TestMergeTemplate()
        {
            var docxmerge = GetDocxmerge();
            var stream = await docxmerge.Merge("carta-pago", new Dictionary<string, object>
            {
                {"Enter Your name:", "Your name"}
            });
            var destFile = File.OpenWrite("./helloworld_merged.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        private MemoryStream GetFile(string path)
        {
            return new MemoryStream(File.ReadAllBytes(path));
        }
        [Fact]
        public async Task TestMergeFile()
        {
            var docxmerge = GetDocxmerge();
            var fileStream = GetFile("./helloworld.docx");
            var stream = await docxmerge.Merge(fileStream, new Dictionary<string, object>
            {
                {"Enter Your name:", "Your name"}
            });
            var destFile = File.OpenWrite("./helloworld_merged.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        #endregion

        #region TransformTests

        [Fact]
        public async Task TestTransformTemplate()
        {
            var docxmerge = GetDocxmerge();
            var stream = await docxmerge.Transform("carta-pago");
            var destFile = File.OpenWrite("./helloworld_convert.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        [Fact]
        public async Task TestTransformFile()
        {
            var docxmerge = GetDocxmerge();
            var fileStream = GetFile("./helloworld.docx");
            var stream =
                await docxmerge.Transform(fileStream);
            var destFile = File.OpenWrite("./helloworld_convert_2.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        #endregion

        #region RenderAndTransform

        [Fact]
        public async Task TestMergeAndTransformFile()
        {
            var docxmerge = GetDocxmerge();
            var fileStream = GetFile("./helloworld.docx");
            var stream = await docxmerge.MergeAndTransform(fileStream, new Dictionary<string, object>
            {
                {"hello_world", "Hello world1111"}
            });
            var destFile = File.OpenWrite("./helloworld.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        [Fact]
        public async Task TestMergeAndTransformTemplate()
        {
            var docxmerge = GetDocxmerge();
            var stream = await docxmerge.MergeAndTransform("carta-pago", new Dictionary<string, object>
            {
                {"hello_world", "Hello world2222"}
            });
            var destFile = File.OpenWrite("./helloworld.pdf");
            await stream.CopyToAsync(destFile);
            destFile.Close();
        }

        #endregion

        private Docxmerge GetDocxmerge()
        {
            return new Docxmerge(apikey, "https://localhost:5100");
        }
    }
}