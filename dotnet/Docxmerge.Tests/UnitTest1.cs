using System;
using System.Threading.Tasks;
using Xunit;

namespace Docxmerge.Tests
{
    public class UnitTest1
    {
        [Fact]
        public async Task Test1()
        {
            var docxmerge = new Docxmerge("");
            var templates = await docxmerge.GetTemplates("", 0, 10);
        }
    }
}