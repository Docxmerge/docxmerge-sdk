using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Docxmerge.Demo
{
    class Program
    {
        static void Main(string[] args)
        {
            Imprimir().Wait();
        }

        private static async Task Imprimir()
        {
            var apikey = "ba7c4d265341489395b1c14d403c2285";
            var tenantId = "9bb27cc8-a2f4-4aac-864a-cdc054b71137";
            var docxmerge = new Docxmerge(apikey);
            var s1 = JsonConvert.DeserializeObject<Dictionary<string, object>>(File.ReadAllText("datos.json"));
            var s = await docxmerge.RenderTemplate(tenantId, "CPLIDNOT", s1, 1, null, Env2.DRAFT);
            var destFile = File.OpenWrite("f.pdf");
            s.CopyTo(destFile);
        }
    }
}