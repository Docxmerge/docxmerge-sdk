import { Stream } from "stream"
import request = require("request")
type KeyValue = { [key: string]: string }
class Docxmerge {
  api: request.RequestAPI<
    request.Request,
    request.CoreOptions,
    request.RequiredUriUrl
  >

  constructor(
    apiKey: string,
    tenant: string = "default",
    baseUrl: string = "https://api.docxmerge.com",
  ) {
    this.api = request.defaults({
      baseUrl: baseUrl,
      headers: { "api-key": apiKey, "x-tenant": tenant },
    })
  }
  renderTemplate(
    templateName: string,
    data: any,
    conversionType: string,
    version: string = "",
  ) {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.post(`/api/v1/Admin/RenderTemplate`, {
        json: true,
        body: {
          data,
          version,
          conversionType,
          template: templateName,
        },
      })
      this.handleReq(req, resolve, reject)
    })
  }
  renderUrl(url: string, data: any, conversionType: string) {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.post(`/api/v1/Admin/RenderUrl`, {
        json: true,
        body: {
          data,
          url,
          conversionType,
        },
      })
      this.handleReq(req, resolve, reject)
    })
  }

  renderFile(file: Stream, data: any, conversion: string) {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.post(`/api/v1/Admin/RenderFile`, {
        formData: {
          file,
          data: JSON.stringify(data),
          tipoConversion: conversion,
        },
      })
      this.handleReq(req, resolve, reject)
    })
  }

  private handleReq(
    req: request.Request,
    resolve: (value?: Stream | PromiseLike<Stream>) => void,
    reject: (reason?: any) => void,
  ) {
    req.on("response", res => {
      res.pause()
      res.statusCode === 200 ? resolve(res) : reject(res)
    })
    req.on("error", res => reject(res))
  }
}

export = Docxmerge
