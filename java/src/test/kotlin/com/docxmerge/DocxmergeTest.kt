package com.docxmerge

import org.junit.Test
import java.io.File

class DocxmergeTest {
    @Test
    fun renderTemplate() {
        val docxmerge = getDocxmerge()
        val map = hashMapOf("hello_world" to "Hello")
        val pdf = docxmerge.renderTemplate("hello_world2", map, "PDF", "latest")
        val bytes = pdf
        saveFile(bytes, "helloworld1.pdf")
    }

    @Test
    fun renderUrl() {
        val docxmerge = getDocxmerge()
        val url =
            "https://api.docxmerge.com/api/v1/File/GetContenido?id=cdb9842d-5e38-4149-a06b-e1079a208fc3&download=true";

        val map = hashMapOf("hello_world" to "Hello")
        val pdf = docxmerge.renderUrl(url, map, "PDF")
        val bytes = pdf
        saveFile(bytes, "helloworld1.pdf")
    }

    @Test
    fun renderFile() {
        val docxmerge = getDocxmerge()
        val map = hashMapOf("hello_world" to "Hello")
        val pdf = docxmerge.renderFile(getHelloWorldBytes(), map, "PDF")
        val bytes = pdf
        saveFile(bytes, "helloworld2.pdf")
    }


    companion object {
        val apiKey = "26JZ5iPpD4U3b9z7lqkXeB2OGsbdF7"
    }

    private fun getDocxmerge(): Docxmerge {
        return Docxmerge(apiKey, "default", "http://localhost:5101")
    }

    private fun saveFile(bytes: ByteArray, path: String) {
        val dir = File("tmp")
        dir.mkdirs()
        val file = File(dir, path)

        file.writeBytes(bytes)
    }

    private fun getHelloWorld(): File {
        return getFile("helloworld.docx")
    }

    private fun getHelloWorldBytes(): ByteArray {
        return getFile("helloworld.docx").readBytes()
    }

    private fun getFile(fileName: String): File {
        val resource = javaClass.classLoader.getResource(fileName)
        return File(resource.file)
    }

    private fun getFileBytes(fileName: String): ByteArray {
        val resource = javaClass.classLoader.getResource(fileName)
        return File(resource.file).readBytes()
    }
}