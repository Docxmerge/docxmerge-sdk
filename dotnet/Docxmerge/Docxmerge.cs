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

        public Docxmerge(string apikey, string baseUrl, string tenant = "default")
        {
            _httpClient = new HttpClient
            {
                BaseAddress = new Uri(baseUrl)
            };
            _httpClient.DefaultRequestHeaders.Add("api-key", apikey);
            _httpClient.DefaultRequestHeaders.Add("x-tenant", tenant);
        }


      

        #region Transform

        public async Task<Stream> Transform(Stream fileStream)
        {
            var form = new MultipartFormDataContent
            {
                {new StreamContent(fileStream), "file", "file.docx"}
            };
            var response = await _httpClient.PostAsync("/api/v1/Admin/TransformFile", form);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        public async Task<Stream> Transform(byte[] bytes)
        {
            var form = new MultipartFormDataContent
            {
                {new ByteArrayContent(bytes), "file", "file.docx"}
            };
            var response = await _httpClient.PostAsync("/api/v1/Admin/TransformFile", form);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        public async Task<Stream> Transform(string template)
        {
            var response = await _httpClient.GetAsync($"/api/v1/Admin/TransformTemplate?template={template}");
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        #endregion

        #region Merge

        public async Task<Stream> Merge<T>(string template, T data) where T : class
        {
            var response = await _httpClient.PostAsync($"/api/v1/Admin/MergeTemplate?template={template}",
                GetJsonContent(data));
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        public async Task<Stream> Merge<T>(Stream fileStream, T data) where T : class
        {
            var response = await _httpClient.PostAsync($"/api/v1/Admin/MergeFile",
                GetMultipart(fileStream, data));
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        public async Task<Stream> Merge<T>(byte[] bytes, T data) where T : class
        {
            var response = await _httpClient.PostAsync($"/api/v1/Admin/MergeFile",
                GetMultipart(bytes, data));
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        #endregion

        #region MergeAndTransform

        public async Task<Stream> MergeAndTransform<T>(string template, T data) where T : class
        {
            var response = await _httpClient.PostAsync(
                $"/api/v1/Admin/MergeAndTransformTemplatePost?template={template}",
                GetJsonContent(data));
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        public async Task<Stream> MergeAndTransform<T>(Stream fileStream, T data) where T : class
        {
            var response = await _httpClient.PostAsync($"/api/v1/Admin/MergeAndTransform",
                GetMultipart(fileStream, data));
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        public async Task<Stream> MergeAndTransform<T>(byte[] bytes, T data) where T : class
        {
            var response = await _httpClient.PostAsync($"/api/v1/Admin/MergeAndTransform",
                GetMultipart(bytes, data));
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStreamAsync();
        }

        #endregion


        private MultipartFormDataContent GetMultipart<T>(Stream file, T data) where T : class
        {
            return new MultipartFormDataContent
            {
                {new StreamContent(file), "file", "file.docx"}, {GetJsonContent(data), "data"}
            };
        }

        private MultipartFormDataContent GetMultipart<T>(byte[] file, T data) where T : class
        {
            return new MultipartFormDataContent
            {
                {new ByteArrayContent(file), "file", "file.docx"}, {GetJsonContent(data), "data"}
            };
        }
        private StringContent GetJsonContent<T>(T data) where T : class
        {
            return new StringContent(JsonConvert.SerializeObject(data), Encoding.UTF8,
                "application/json");
        }
    }
}