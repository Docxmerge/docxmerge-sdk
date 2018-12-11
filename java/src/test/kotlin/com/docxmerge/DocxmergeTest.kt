package com.docxmerge

import org.junit.Test
import java.io.File
import java.net.URL

class DocxmergeTest {
    @Test
    fun convertFile() {
        val docxmerge = getDocxmerge()
        val template = getHelloWorld();
        val pdf = docxmerge.convertFile(template)
        val bytes = pdf!!.readBytes()
        saveFile(bytes, "helloworld.pdf")
    }

    @Test
    fun renderFile() {
        val docxmerge = getDocxmerge()
        val template = getHelloWorld();
        val pdf = docxmerge.renderFile(template, hashMapOf<String, String>("hello_world" to "Hello world."))
        val bytes = pdf!!.readBytes()
        saveFile(bytes, "helloworld_merged.pdf")
    }


    @Test
    fun renderTemplate() {
        val docxmerge = getDocxmerge()
        val template = getHelloWorld();
        val pdf = docxmerge.renderTemplate(
            "Hello world",
            hashMapOf("hello_world" to "Hello world.."),
            1,
            "DRAFT",
            HashMap<String, String>()
        )
        val bytes = pdf!!.readBytes()
        saveFile(bytes, "helloworld_merged2.pdf")
    }

    @Test
    fun convertTemplate() {
        val docxmerge = getDocxmerge()
        val pdf = docxmerge.convertTemplate("Hello world", 1, "DRAFT", HashMap<String, String>())
        val bytes = pdf!!.readBytes()
        saveFile(bytes, "helloworld1.pdf")
    }

    companion object {
        val apiKey = "8f22c304d0b44af2b03c2ad3d1aa5471"
        val tenantId = "f60b0638-2f2e-4f92-b027-39cedfa06d4d"
    }

    private fun getDocxmerge(): Docxmerge {
        return Docxmerge(apiKey, tenantId, "http://localhost:5030")
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

    private fun getFile(fileName: String): File {
        val resource = javaClass.classLoader.getResource(fileName)
        return File(resource.file)
    }
}