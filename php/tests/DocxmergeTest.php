<?php

use Docxmerge\Docxmerge;

class DocxmergeTest extends \PHPUnit\Framework\TestCase
{
    /**
     * @test
     */
    public function testTransformTemplate()
    {
        self::assertTrue(true);
        $docxmerge = $this->getDocxmerge();
        $fp = fopen("../tmp/helloworld-transform.pdf", "w");
        try {
            $docxmerge->transformTemplate($fp, "helloworld");
        } catch (Exception $e) {
            $this->fail($e->getMessage());
        }
    }

    public function testTransformDocument()
    {
        self::assertTrue(true);
        $docxmerge = $this->getDocxmerge();
        $fp = fopen("../tmp/helloworld-transform-doc.pdf", "w");
        try {
            $docxmerge->transformDocument($fp, "../fixtures/helloworld.docx");
        } catch (Exception $e) {
            $this->fail($e->getMessage());
        }
    }

    public function testMergeTemplate()
    {
        self::assertTrue(true);
        $docxmerge = $this->getDocxmerge();
        $fp = fopen("../tmp/helloworld-merge.docx", "w");
        $data = array(
            'hello_world' => 'Hola mundo',
        );
        try {
            $docxmerge->mergeTemplate($fp, "helloworld", $data);
        } catch (Exception $e) {
            $this->fail($e->getMessage());
        }
    }

    public function testMergeDocument()
    {
        self::assertTrue(true);
        $docxmerge = $this->getDocxmerge();
        $fp = fopen("../tmp/helloworld-merge-doc.docx", "w");
        $data = array(
            'hello_world' => 'Hola mundo',
        );
        try {
            $docxmerge->mergeDocument($fp, "../fixtures/helloworld.docx", $data);
        } catch (Exception $e) {
            $this->fail($e->getMessage());
        }
    }
    public function testMergeAndTransformTemplate()
    {
        self::assertTrue(true);
        $docxmerge = $this->getDocxmerge();
        $fp = fopen("../tmp/helloworld-merge.docx", "w");
        $data = array(
            'hello_world' => 'Hola mundo',
        );
        try {
            $docxmerge->mergeAndTransformTemplate($fp, "helloworld", $data);
        } catch (Exception $e) {
            $this->fail($e->getMessage());
        }
    }

    public function testMergeAndTransformDocument()
    {
        self::assertTrue(true);
        $docxmerge = $this->getDocxmerge();
        $fp = fopen("../tmp/helloworld-merge-doc.pdf", "w");
        $data = array(
            'hello_world' => 'Hola mundo',
        );
        try {
            $docxmerge->mergeAndTransformDocument($fp, "../fixtures/helloworld.docx", $data);
        } catch (Exception $e) {
            $this->fail($e->getMessage());
        }
    }

    private function getDocxmerge()
    {
        $apiKey = 'vdnpUV4ZTLeYYrcyvF3XcKe4ZuToY5';
        $baseUrl = "http://localhost:5101";
        $tenant = "default";
        return new Docxmerge($apiKey, $baseUrl, $tenant);
    }
}
