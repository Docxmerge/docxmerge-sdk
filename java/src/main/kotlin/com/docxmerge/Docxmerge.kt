package com.docxmerge

import com.fasterxml.jackson.databind.ObjectMapper
import io.swagger.client.ApiClient
import io.swagger.client.api.ApiApi
import io.swagger.client.api.TemplatesApi
import io.swagger.client.auth.ApiKeyAuth
import io.swagger.client.model.Report
import io.swagger.client.model.TemplateListResponseModel
import java.io.File


open class Docxmerge(apiKey: String, private var tenant: String, url: String = "https://api.docxmerge.com") {
    private var templatesApi: TemplatesApi
    private var apiApi: ApiApi
    private var apiClient: ApiClient = ApiClient()
    private val mapper = ObjectMapper()

    init {
        val auth = apiClient.getAuthentication("ApiKey") as ApiKeyAuth
        auth.apiKey = apiKey
        apiClient.addDefaultHeader("ApiKey", apiKey)
        apiClient.setApiKey(apiKey)
        apiClient.basePath = url
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

    fun convertFile(document: File): File? {
        return templatesApi.apiByTenantConvertPost(tenant, document)
    }

    fun convertTemplate(
        templateName: String, version: Int,
        env: String,
        attributes: Any
    ): File? {
        return templatesApi.apiByTenantTemplatesByTemplateNameConvertPost(
            templateName,
            tenant,
            version,
            false,
            attributes,
            env
        )
    }

    fun renderTemplate(
        templateName: String,
        data: Map<String, Any>,
        version: Int,
        env: String,
        attributes: Any
    ): File? {
        val report = templatesApi.apiByTenantTemplatesByTemplateNameRenderPost(
            data,
            templateName,
            tenant,
            version,
            false,
            attributes,
            env
        )

        return templatesApi.apiByTenantReportsByIdGet(report.id,tenant)
    }

    fun mergeDocx(document: File, data: Map<String, Any>): File? {
        val dataFile = File.createTempFile("prefix-", "-json")

        val text = mapper.writeValueAsString(data)
        dataFile.writeText(text)
        dataFile.deleteOnExit()
        return templatesApi.apiByTenantMergePost(tenant, document, dataFile)
    }
}
