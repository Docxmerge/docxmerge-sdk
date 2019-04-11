package com.docxmerge

import com.google.gson.Gson
import org.apache.http.client.fluent.Request
import org.apache.http.entity.ContentType
import org.apache.http.entity.mime.MultipartEntityBuilder
import java.io.Serializable

open class Docxmerge(private var apiKey: String, private var url: String = "https://api.docxmerge.com") {
    fun transformTemplate(templateName: String): ByteArray {
        return Request.Post("${url}/api/v1/Admin/TransformTemplate?template=$templateName")
            .addHeader("api-key", apiKey)
            .execute().returnContent().asBytes()
    }

    fun transformFile(file: ByteArray): ByteArray {
        val multipart = MultipartEntityBuilder.create()
            .addBinaryBody("file", file, ContentType.APPLICATION_OCTET_STREAM, "file.docx")
        return Request.Post("${url}/api/v1/Admin/TransformFile")
            .addHeader("api-key", apiKey)
            .body(multipart.build())
            .execute().returnContent().asBytes()
    }

    fun <T : Serializable> mergeTemplate(templateName: String, data: T): ByteArray {
        return Request.Post("${url}/api/v1/Admin/MergeTemplate?template=$templateName")
            .addHeader("api-key", apiKey)
            .addHeader("Content-type", "application/json")
            .bodyString(Companion.gson.toJson(data), ContentType.APPLICATION_JSON)
            .execute().returnContent().asBytes()
    }

    fun <T : Serializable> mergeFile(file: ByteArray, data: T): ByteArray {
        val multipart = MultipartEntityBuilder.create()
            .addBinaryBody("file", file, ContentType.APPLICATION_OCTET_STREAM, "file.docx")
            .addTextBody("data", Companion.gson.toJson(data), ContentType.APPLICATION_JSON)

        return Request.Post("${url}/api/v1/Admin/TransformFile")
            .addHeader("api-key", apiKey)
            .body(multipart.build())
            .execute().returnContent().asBytes()
    }

    fun <T : Serializable> mergeAndTransformTemplate(templateName: String, data: T): ByteArray {
        return Request.Post("${url}/api/v1/Admin/MergeAndTransformTemplatePost?template=$templateName")
            .addHeader("api-key", apiKey)
            .addHeader("Content-type", "application/json")
            .bodyString(Companion.gson.toJson(data), ContentType.APPLICATION_JSON)
            .execute().returnContent().asBytes()
    }

    fun <T : Serializable> mergeAndTransformFile(file: ByteArray, data: T): ByteArray {
        val multipart = MultipartEntityBuilder.create()
            .addBinaryBody("file", file, ContentType.APPLICATION_OCTET_STREAM, "file.docx")
            .addTextBody("data", Companion.gson.toJson(data), ContentType.APPLICATION_JSON)

        return Request.Post("${url}/api/v1/Admin/MergeAndTransform")
            .addHeader("api-key", apiKey)
            .body(multipart.build())
            .execute().returnContent().asBytes()
    }

    companion object {
        private val gson = Gson()
    }

}
