using System;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Docxmerge
{
    public class Docxmerge
    {
        private readonly HttpClient _httpClient;

        public Docxmerge(string apikey, string tenant = "default", string baseUrl = "https://api.docxmerge.com")
        {
            _httpClient = new HttpClient
            {
                BaseAddress = new Uri(baseUrl)
            };
            _httpClient.DefaultRequestHeaders.Add("api-key", apikey);
            _httpClient.DefaultRequestHeaders.Add("x-tenant", tenant);
        }


        #region Render

        public async Task<Stream> RenderTemplate<T>(string template, T data, string conversionType, string version = "")
            where T : class
        {
            var response = await _httpClient.PostAsync(
                $"/api/v1/Admin/RenderTemplate",
                GetJsonContent(new
                {
                    data,
                    version,
                    conversionType,
                    template
                }));
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }
        public async Task<Stream> RenderUrl<T>(string url, T data, string conversionType, string version = "")
            where T : class
        {
            var response = await _httpClient.PostAsync(
                $"/api/v1/Admin/RenderUrl",
                GetJsonContent(new
                {
                    data,
                    version,
                    conversionType,
                    url
                }));
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        public async Task<Stream> RenderFile<T>(Stream fileStream, T data, string conversionType) where T : class
        {
            var response = await _httpClient.PostAsync(
                $"/api/v1/Admin/RenderFile",
                GetMultipart(fileStream, data, conversionType)
            );
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        #endregion

        private static MultipartFormDataContent GetMultipart<T>(Stream file, T data, string conversionType)
            where T : class
        {
            return new MultipartFormDataContent
            {
                {new StreamContent(file), "file", "file.docx"},
                {GetJsonContent(data), "data"},
                {new StringContent(conversionType), "conversionType"},
            };
        }


        private static StringContent GetJsonContent<T>(T data) where T : class
        {
            return new StringContent(JsonConvert.SerializeObject(data), Encoding.UTF8,
                "application/json");
        }
    }
}