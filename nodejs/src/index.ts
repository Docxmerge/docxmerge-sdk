import qs = require("querystring")
import request = require("request")
import { Stream } from "stream"

import { ApiApi, ApiKeyAuth, TemplatesApi } from "./swagger/api"
type EnvType = "DRAFT" | "TESTING" | "PRODUCTION"
interface KeyValue {
  [key: string]: string
}
interface ReportResponse {
  url: string
  reportId: string
  content: Stream
}
const wordContentType =
  "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
const jsonContentType = "application/json"
class Docxmerge {
  private templatesApi: TemplatesApi
  private apiApi: ApiApi

  constructor(private apiKey: string, private readonly basePath) {
    this.basePath = this.basePath || "https://api.docxmerge.com"
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
  async renderFile(tenantId: string, file: Buffer, data: KeyValue) {
    const { body } = await this.templatesApi.apiByTenantPrintPost(
      tenantId,
      this.getDocxFormFile(file),
      this.getJsonFormFile(data),
    )
    return body
  }
  renderTemplate(
    tenant: string,
    templateName: string,
    data: object,
    attributes: KeyValue = {},
    env?: EnvType,
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
            content: this.getRequestApi().get(url, { baseUrl: "" }),
          })
        },
      )
    })
  }
  async renderUrl(tenant: string, url: string, data: any) {
    return new Promise<Buffer>((resolve, reject) => {
      this.getRequestApi().post(
        `/${tenant}/print`,
        {
          headers: {
            ApiKey: this.apiKey,
          },
          encoding: null,
          formData: {
            document: {
              value: request(url),
              options: {
                filename: "file.docx",
                contentType: wordContentType,
              },
            },
            data: {
              value: JSON.stringify(data),
              options: {
                filename: "file.json",
                contentType: "application/json",
              },
            },
          },
        },
        (err, res, body) => {
          if (err) return reject(err)
          resolve(res.body)
        },
      )
    })
  }
  async convertTemplate(
    tenant: string,
    templateName: string,
    attributes: KeyValue = {},
    env?: EnvType,
    version?: number,
  ) {
    return new Promise<Buffer>((resolve, reject) => {
      const query = {
        version,
        env,
        ...attributes,
      }

      this.getRequestApi().post(
        `/${tenant}/templates/${templateName}/convert?${qs.stringify(query)}`,
        {
          json: true,
          body: {},
          encoding: null,
          headers: {
            ApiKey: this.apiKey,
          },
        },
        async (err, res, body) => {
          if (err) {
            return reject(err)
          }
          resolve(res.body)
        },
      )
    })
  }
  async convertFile(tenant: string, file: Buffer) {
    const { body, response } = await this.templatesApi.apiByTenantConvertPost(
      tenant,
      this.getDocxFormFile(file),
    )
    return body
  }
  async mergeTemplate(
    tenant: string,
    templateName: string,
    data: KeyValue,
    attributes: KeyValue = {},
    env?: EnvType,
    version?: number,
  ) {
    return new Promise<Buffer>((resolve, reject) => {
      const query = {
        version,
        env,
        ...attributes,
      }

      this.getRequestApi().post(
        `/${tenant}/templates/${templateName}/merge?${qs.stringify(query)}`,
        {
          json: true,
          body: data,
          encoding: null,
          headers: {
            ApiKey: this.apiKey,
          },
        },
        async (err, res, body) => {
          if (err) {
            return reject(err)
          }
          resolve(res.body)
        },
      )
    })
  }
  async mergeFile(tenant: string, file: Buffer, data: KeyValue = {}) {
    const { body } = await this.templatesApi.apiByTenantMergePost(
      tenant,
      this.getDocxFormFile(file),
      this.getJsonFormFile(data),
    )
    return body
  }
  private getDocxFormFile(file: Buffer) {
    return this.getFormFile(file, "file.docx", wordContentType)
  }
  private getJsonFormFile(data: KeyValue) {
    return this.getFormFile(
      Buffer.from(JSON.stringify(data)),
      "file.json",
      jsonContentType,
    )
  }
  private getFormFile(
    file: Buffer,
    filename: string = "file",
    contentType: string = "application/octet-stream",
  ): any {
    return {
      value: file,
      options: {
        filename,
        contentType,
      },
    }
  }
  private getRequestApi() {
    return request.defaults({
      json: true,
      headers: { ApiKey: this.apiKey },
      baseUrl: `${this.basePath}/api`,
    })
  }
}
export = Docxmerge
