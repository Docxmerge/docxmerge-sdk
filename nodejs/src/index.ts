import qs = require("querystring")
import request = require("request")
import { Stream } from "stream"

import { ApiApi, ApiKeyAuth, TemplatesApi } from "./swagger/api"

interface KeyValue {
  [key: string]: string
}
interface ReportResponse {
  url: string
  reportId: string
  content: Stream
}
class Docxmerge {
  private templatesApi: TemplatesApi
  private apiApi: ApiApi
  private readonly basePath = "https://api.docxmerge.com"

  constructor(private apiKey: string) {
    const auth = new ApiKeyAuth("header", "ApiKey")
    auth.apiKey = apiKey

    const templatesApi = new TemplatesApi(this.basePath)
    const apiApi = new ApiApi(this.basePath)

    templatesApi.setDefaultAuthentication(auth)
    apiApi.setDefaultAuthentication(auth)
    this.templatesApi = templatesApi
    this.apiApi = apiApi
  }
  getTemplates(tenant: string, page: number, size: number) {
    return this.templatesApi.apiByTenantTemplatesGet(tenant, size, page)
  }
  getReportById(tenant: string, id: string) {
    return this.templatesApi.apiByTenantReportsByIdGet(id, tenant)
  }
  renderFile(file: Buffer, data: any) {
    return new Promise<Buffer>((resolve, reject) => {
      this.getRequestApi().post(
        "/print",
        {
          encoding: null,
          formData: {
            document: {
              value: file,
              options: {
                filename: "diploma.docx",
                contentType:
                  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
              },
            },
            data: {
              value: Buffer.from(JSON.stringify(data)),
              options: {
                filename: "data.json",
                contentType: "application/json",
              },
            },
          },
        },
        (err, res) => {
          if (err) {
            return reject(err)
          }
          resolve(res.body)
        },
      )
    })
  }
  renderTemplate(
    tenant: string,
    templateName: string,
    data: object,
    attributes: KeyValue = {},
    env?: string,
    version?: number,
  ): Promise<ReportResponse> {
    return new Promise<ReportResponse>((resolve, reject) => {
      const query = {
        version,
        env,
        ...attributes,
      }

      this.getRequestApi().post(
        `/${tenant}/templates/${templateName}/render?${qs.stringify(query)}`,
        {
          json: true,
          body: data,
          headers: {
            ApiKey: this.apiKey,
          },
        },
        async (err, res) => {
          if (err) {
            return reject(err)
          }
          if (res.statusCode !== 201) {
            return reject(new Error(`Bad status code${res.statusCode}`))
          }
          const url = res.headers.location
          resolve({
            reportId: res.body.id,
            url,
            content: this.getRequestApi().get(url),
          })
        },
      )
    })
  }
  getRequestApi() {
    return request.defaults({
      json: true,
      headers: { ApiKey: this.apiKey },
      baseUrl: `${this.basePath}/api`,
    })
  }
}
export = Docxmerge
