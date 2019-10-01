package com.docxmerge

import com.google.gson.Gson
import org.apache.http.client.fluent.Request
import org.apache.http.entity.ContentType
import org.apache.http.entity.mime.MultipartEntityBuilder
import java.io.Serializable
import com.google.gson.GsonBuilder
import java.util.HashMap


open class Docxmerge(
    private var apiKey: String,
    private var tenant: String = "default",
    private var baseUrl: String = "https://api.docxmerge.com"
) {
    fun <T : Serializable> renderTemplate(
        templateName: String,
        data: T,
        conversionType: String,
        version: String
    ): ByteArray {
        val map = HashMap<String, Any>()
        map["version"] = version
        map["data"] = data
        map["template"] = templateName
        map["conversionType"] = conversionType

        return Request.Post("${baseUrl}/api/v1/Admin/RenderTemplate")
            .addHeader("api-key", apiKey)
            .addHeader("x-tenant", tenant)
            .addHeader("Content-type", "application/json")
            .bodyString(gson.toJson(map), ContentType.APPLICATION_JSON)
            .execute().returnContent().asBytes()
    }

    fun <T : Serializable> renderUrl(
        url: String,
        data: T,
        conversionType: String
    ): ByteArray {
        val map = HashMap<String, Any>()
        map["data"] = data
        map["url"] = url
        map["conversionType"] = conversionType

        return Request.Post("${baseUrl}/api/v1/Admin/RenderUrl")
            .addHeader("api-key", apiKey)
            .addHeader("x-tenant", tenant)
            .addHeader("Content-type", "application/json")
            .bodyString(gson.toJson(map), ContentType.APPLICATION_JSON)
            .execute().returnContent().asBytes()
    }

    fun <T : Serializable> renderFile(
        file: ByteArray,
        data: T,
        conversionType: String
    ): ByteArray {
        val multipart = MultipartEntityBuilder.create()
            .addBinaryBody("file", file, ContentType.APPLICATION_OCTET_STREAM, "file.docx")
            .addTextBody("data", gson.toJson(data), ContentType.APPLICATION_JSON)
            .addTextBody("conversionType", conversionType, ContentType.TEXT_PLAIN)

        return Request.Post("${baseUrl}/api/v1/Admin/RenderFile")
            .addHeader("api-key", apiKey)
            .addHeader("x-tenant", tenant)
            .body(multipart.build())
            .execute().returnContent().asBytes()
    }

    companion object {
        private val gson = Gson()
    }

}
