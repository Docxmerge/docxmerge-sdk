package com.docxmerge

import com.fasterxml.jackson.databind.ObjectMapper
import io.swagger.client.ApiClient
import io.swagger.client.api.ApiApi
import io.swagger.client.api.TemplatesApi
import io.swagger.client.auth.ApiKeyAuth
import io.swagger.client.model.Report
import io.swagger.client.model.TemplateListResponseModel
import java.io.File


open class Docxmerge(apiKey: String, private var tenant: String) {
    private var templatesApi: TemplatesApi
    private var apiApi: ApiApi
    private var apiClient: ApiClient = ApiClient()
    val mapper = ObjectMapper()

    init {
        val auth = apiClient.getAuthentication("ApiKey") as ApiKeyAuth
        auth.apiKey = apiKey
        apiClient.addDefaultHeader("ApiKey", apiKey)
        apiClient.setApiKey(apiKey)
        apiClient.basePath = "https://api.docxmerge.com"
        templatesApi = TemplatesApi(apiClient)
        apiApi = ApiApi(apiClient)
    }

    fun getTemplates(page: Int, size: Int): TemplateListResponseModel? {
        return templatesApi.apiByTenantTemplatesGet(tenant, size, page)
    }

    fun renderFile(document: File, data: Map<String, Any>): File? {
        val dataFile = File.createTempFile("prefix-", "-json")

        val text = mapper.writeValueAsString(data)
        dataFile.writeText(text)
        dataFile.deleteOnExit()
        return apiApi.apiPrintPost(document, dataFile)
    }

    fun renderTemplate(
        templateName: String,
        data: Map<String, Any>,
        version: Int,
        env: String,
        attributes: Any
    ): Report? {
        return templatesApi.apiByTenantTemplatesByTemplateNameRenderPost(
            data,
            templateName,
            tenant,
            version,
            false,
            attributes,
            env
        )
    }
}
