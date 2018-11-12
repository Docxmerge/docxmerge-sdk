using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Security.Principal;
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
        private static readonly string basePath = "https://api.docxmerge.com";
        private readonly DocxmergeApi _apiClient;


        public Docxmerge(string apikey)
        {
            _apiClient = new DocxmergeApi(basePath, apikey);
        }

        public async Task<System.IO.Stream> RenderTemplate<T>(string tenantId, string templateName,
            T data,
            int version,
            Dictionary<string, string> attributes = null, Env? env = null)
        {
            var dict = ObjectToDictionary(data);
            var report = await _apiClient.ApiByTenantTemplatesByTemplateNameRenderPostAsync(templateName, tenantId,
                version,
                false, dict, attributes, env);
            var reportResponse = await _apiClient.ApiByTenantReportsByIdGetAsync(report.Id, tenantId);
            return reportResponse.Stream;
        }

        public Task<TemplateListResponseModel> GetTemplates(string tenantId, int page, int size)
        {
            return _apiClient.ApiByTenantTemplatesGetAsync(tenantId, page, size);
        }

        private Dictionary<string, object> ObjectToDictionary<T>(T model)
        {
            var json = JsonConvert.SerializeObject(model);
            return JsonConvert.DeserializeObject<Dictionary<string, object>>(json);
        }
    }
}