using System.IO;
using NSwag;
using NSwag.CodeGeneration.CSharp;

namespace Docxmerge.Tools
{
    class Program
    {
        static void Main(string[] args)
        {
//            var document = SwaggerDocument.FromUrlAsync("https://api.docxmerge.com/api/swagger/v1/swagger.json").Result;
            var document = SwaggerDocument.FromUrlAsync("http://localhost:5101/swagger/v1/swagger.json").Result;

            var clientSettings = new SwaggerToCSharpClientGeneratorSettings
            {
                ClassName = "DocxmergeApi",
                CSharpGeneratorSettings =
                {
                    Namespace = "Docxmerge"
                }
            };
            var clientGenerator = new SwaggerToCSharpClientGenerator(document, clientSettings);

            var code = clientGenerator.GenerateFile();
            File.WriteAllText("../Docxmerge/Api.cs", code);
        }
    }
}