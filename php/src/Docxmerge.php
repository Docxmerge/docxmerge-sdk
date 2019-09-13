<?php

namespace Docxmerge;


class Docxmerge
{
    private $apiKey;
    private $baseUrl;
    private $tenant;

    public function __construct($apiKey, $baseUrl, $tenant = "default")
    {
        $this->apiKey = $apiKey;
        $this->baseUrl = $baseUrl;
        $this->tenant = $tenant;
    }

    public function transformTemplate($fp, $templateName)
    {
        $baseUrl = $this->baseUrl;
        $ch = curl_init("$baseUrl/api/v1/Admin/TransformTemplate?template=$templateName");
        curl_setopt($ch, CURLOPT_FILE, $fp);
        $this->hydrateCurl($ch);

        curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if ($http_code != "200") throw new \Exception("Unexpected status code $http_code");
    }

    public function transformDocument($fp, $docxPath)
    {
        $baseUrl = $this->baseUrl;
        $ch = curl_init("$baseUrl/api/v1/Admin/TransformFile");
        curl_setopt($ch, CURLOPT_FILE, $fp);
        $this->hydrateCurl($ch);
        $fields = [
            'file' => new \CurlFile($docxPath, '', 'file.docx'),
        ];
        curl_setopt($ch, CURLOPT_POSTFIELDS, $fields);
        curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if ($http_code != "200") throw new \Exception("Unexpected status code $http_code");
    }

    public function mergeTemplate($fp, $templateName, $data)
    {
        $baseUrl = $this->baseUrl;
        $apiKey = $this->apiKey;
        $tenant = $this->tenant;

        $ch = curl_init("$baseUrl/api/v1/Admin/MergeTemplate?template=$templateName");

        $payload = json_encode($data);

        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
        curl_setopt($ch, CURLOPT_FILE, $fp);
        curl_setopt($ch, CURLOPT_POST, 1);
        $body_len = strlen($payload);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
                'Content-Type: application/json',
                "Content-Length:$body_len",
                "api-key: $apiKey",
                "x-tenant: $tenant",
            )
        );
        curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

        curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if ($http_code != "200") throw new \Exception("Unexpected status code $http_code");
    }

    public function mergeDocument($fp, $docxPath, $data)
    {
        $baseUrl = $this->baseUrl;
        $apiKey = $this->apiKey;
        $tenant = $this->tenant;

        $ch = curl_init("$baseUrl/api/v1/Admin/MergeFile");

        $payload = json_encode($data);

        $options = array(
            CURLOPT_POST => true,
            CURLOPT_HTTPHEADER => array(
                "api-key: $apiKey",
                "x-tenant: $tenant",
            ),
            CURLOPT_POSTFIELDS => array(
                'file' => new \CurlFile("$docxPath", '', 'file'),
                'data' => $payload,
            ),
            CURLOPT_FILE => $fp,
        );
        curl_setopt_array($ch, $options);
        curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if ($http_code != "200") throw new \Exception("Unexpected status code $http_code");
    }

    public function mergeAndTransformTemplate($fp, $templateName, $data)
    {
        $baseUrl = $this->baseUrl;
        $apiKey = $this->apiKey;
        $tenant = $this->tenant;

        $ch = curl_init("$baseUrl/api/v1/Admin/MergeAndTransformTemplatePost?template=$templateName");

        $payload = json_encode($data);

        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
        curl_setopt($ch, CURLOPT_FILE, $fp);
        curl_setopt($ch, CURLOPT_POST, 1);
        $body_len = strlen($payload);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
                'Content-Type: application/json',
                "Content-Length:$body_len",
                "api-key: $apiKey",
                "x-tenant: $tenant",
            )
        );
        curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

        curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if ($http_code != "200") throw new \Exception("Unexpected status code $http_code");
    }

    public function mergeAndTransformDocument($fp, $docxPath, $data)
    {
        $baseUrl = $this->baseUrl;
        $apiKey = $this->apiKey;
        $tenant = $this->tenant;

        $ch = curl_init("$baseUrl/api/v1/Admin/MergeAndTransform");

        $payload = json_encode($data);

        $options = array(
            CURLOPT_POST => true,
            CURLOPT_HTTPHEADER => array(
                "api-key: $apiKey",
                "x-tenant: $tenant",
            ),
            CURLOPT_POSTFIELDS => array(
                'file' => new \CurlFile("$docxPath", '', 'file'),
                'data' => $payload,
            ),
            CURLOPT_FILE => $fp,
        );
        curl_setopt_array($ch, $options);
        curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if ($http_code != "200") throw new \Exception("Unexpected status code $http_code");
    }


    private function hydrateCurl($ch)
    {
        $apiKey = $this->apiKey;
        $tenant = $this->tenant;
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
            "api-key: $apiKey",
            "x-tenant: $tenant",
        ));
    }

    /**
     * @return mixed
     */
    public function getBaseUrl()
    {
        return $this->baseUrl;
    }

    /**
     * @return mixed
     */
    public function getApiKey()
    {
        return $this->apiKey;
    }

    /**
     * @return string
     */
    public function getTenant(): string
    {
        return $this->tenant;
    }
}