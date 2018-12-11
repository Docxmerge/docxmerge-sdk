using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Security.Principal;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Docxmerge
{
    public partial class DocxmergeApi
    {
        private readonly string _apiKey;

        public DocxmergeApi(string baseUrl, string apiKey)
        {
            _apiKey = apiKey;

            // from Api.cs
            BaseUrl = baseUrl;
            _settings = new Lazy<JsonSerializerSettings>(() =>
            {
                var settings = new JsonSerializerSettings();
                UpdateJsonSerializerSettings(settings);
                return settings;
            });
        }

        partial void PrepareRequest(HttpClient client, HttpRequestMessage request, string url)
        {
            request.Headers.Add("ApiKey", _apiKey);
        }
    }

    public class Docxmerge
    {
        private readonly DocxmergeApi _apiClient;


        public Docxmerge(string apikey, string basePath = "https://api.docxmerge.com")
        {
            _apiClient = new DocxmergeApi(basePath, apikey);
        }

        public async Task<System.IO.Stream> RenderFile<T>(string tenant, System.IO.Stream document, T data)
        {
            var renderFile = await _apiClient.ApiByTenantPrintPostAsync(tenant, new FileParameter(document),
                new FileParameter(ObjectToStream(data)));
            return renderFile.Stream;
        }

        public async Task<System.IO.Stream> RenderTemplate<T>(string tenantId, string templateName,
            T data,
            int version,
            Dictionary<string, string> attributes = null, Env2? env = null)
        {
            var dict = ObjectToDictionary(data);
            var report = await _apiClient.ApiByTenantTemplatesByTemplateNameRenderPostAsync(templateName, tenantId,
                version,
                false, dict, attributes, env);
            var reportResponse = await _apiClient.ApiByTenantReportsByIdGetAsync(report.Id, tenantId);
            return reportResponse.Stream;
        }

        public async Task<System.IO.Stream> MergeTemplate<T>(string tenant, System.IO.Stream document, T data)
        {
            var fileResponse = await _apiClient.ApiByTenantMergePostAsync(tenant, new FileParameter(document),
                new FileParameter(ObjectToStream(data)));
            return fileResponse.Stream;
        }

        public async Task<System.IO.Stream> ConvertFile(string tenant, System.IO.Stream document)
        {
            var fileResponse = await _apiClient.ApiByTenantConvertPostAsync(new FileParameter(document), tenant);
            return fileResponse.Stream;
        }

        public async Task<System.IO.Stream> ConvertTemplate(string tenant, string templateName, int version,
            Dictionary<string, string> attributes = null, Env? env = null)
        {
            var fileResponse =
                await _apiClient.ApiByTenantTemplatesByTemplateNameConvertPostAsync(templateName,tenant, version,
                    false, attributes, env);
            return fileResponse.Stream;
        }

        public Task<TemplateListResponseModel> GetTemplates(string tenantId, int page, int size)
        {
            return _apiClient.ApiByTenantTemplatesGetAsync(tenantId, page, size);
        }

        private MemoryStream ObjectToStream<T>(T model)
        {
            var ms = new MemoryStream();
            var json = JsonConvert.SerializeObject(model);
            ms.Write(Encoding.UTF8.GetBytes(json));
            ms.Seek(0, SeekOrigin.Begin);
            return ms;
        }

        private Dictionary<string, object> ObjectToDictionary<T>(T model)
        {
            var json = JsonConvert.SerializeObject(model);
            return JsonConvert.DeserializeObject<Dictionary<string, object>>(json);
        }
    }
}