package com.docxmerge

import org.junit.Test
import java.io.File

class DocxmergeTest {
    @Test
    fun transformTemplate() {
        val docxmerge = getDocxmerge()
        val pdf = docxmerge.transformTemplate("hello-world")
        val bytes = pdf
        saveFile(bytes, "helloworld1.pdf")
    }

    @Test
    fun transformFile() {
        val docxmerge = getDocxmerge()
        val pdf = docxmerge.transformFile(getHelloWorldBytes())
        val bytes = pdf
        saveFile(bytes, "helloworld2.pdf")
    }

    @Test
    fun mergeTemplate() {
        val docxmerge = getDocxmerge()
        val map = hashMapOf("hello_world" to "Hello")
        val pdf = docxmerge.mergeTemplate("hello-world", map)
        val bytes = pdf
        saveFile(bytes, "helloworld1.docx")
    }

    @Test
    fun mergeFile() {
        val docxmerge = getDocxmerge()
        val map = hashMapOf("hello_world" to "Hello")
        val pdf = docxmerge.mergeFile(getHelloWorldBytes(), map)
        val bytes = pdf
        saveFile(bytes, "helloworld2.docx")
    }
    @Test
    fun mergeAndTransformTemplate() {
        val docxmerge = getDocxmerge()
        val map = hashMapOf("hello_world" to "Hello")
        val pdf = docxmerge.mergeAndTransformTemplate("hello-world", map)
        val bytes = pdf
        saveFile(bytes, "helloworld1.docx")
    }

    @Test
    fun mergeAndTransformFile() {
        val docxmerge = getDocxmerge()
        val map = hashMapOf("hello_world" to "Hello")
        val pdf = docxmerge.mergeAndTransformFile(getHelloWorldBytes(), map)
        val bytes = pdf
        saveFile(bytes, "helloworld2.docx")
    }

    companion object {
        val apiKey = "QTTSbTSii840rl4JdLP0xiJGJJmfE5"
    }

    private fun getDocxmerge(): Docxmerge {
        return Docxmerge(apiKey, "http://localhost:5101")
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