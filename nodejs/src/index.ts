import { Stream } from 'stream';
import request = require('request');
type KeyValue = { [key: string]: string };
class Docxmerge {
  api: request.RequestAPI<
    request.Request,
    request.CoreOptions,
    request.RequiredUriUrl
  >;

  constructor(apiKey: string, baseUrl: string) {
    this.api = request.defaults({
      baseUrl: baseUrl,
      headers: { 'api-key': apiKey }
    });
  }
  async transformTemplate(templateName: string): Promise<Stream> {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.get(
        `/api/v1/Admin/TransformTemplate?template=${templateName}`
      );
      this.handleReq(req, resolve, reject);
    });
  }
  transformFile(file: Stream): Promise<Stream> {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.post(`/api/v1/Admin/TransformFile`, {
        formData: { file }
      });
      this.handleReq(req, resolve, reject);
    });
  }
  mergeTemplate(templateName: string, data: KeyValue): Promise<Stream> {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.post(
        `/api/v1/Admin/MergeTemplate?template=${templateName}`,
        {
          json: true,
          body: data
        }
      );
      this.handleReq(req, resolve, reject);
    });
  }
  mergeFile(file: Stream, data: KeyValue): Promise<Stream> {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.post(`/api/v1/Admin/MergeFile`, {
        formData: {
          file,
          data: JSON.stringify(data)
        }
      });
      this.handleReq(req, resolve, reject);
    });
  }
  mergeAndTransformTemplate(
    templateName: string,
    data: KeyValue
  ): Promise<Stream> {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.post(
        `/api/v1/Admin/MergeAndTransformTemplatePost?template=${templateName}`,
        {
          json: true,
          body: data
        }
      );
      this.handleReq(req, resolve, reject);
    });
  }
  mergeAndTransformFile(file: Stream, data: KeyValue): Promise<Stream> {
    return new Promise<Stream>((resolve, reject) => {
      const req = this.api.post(`/api/v1/Admin/MergeAndTransform`, {
        formData: {
          file,
          data: JSON.stringify(data)
        }
      });
      this.handleReq(req, resolve, reject);
    });
  }
  private handleReq(
    req: request.Request,
    resolve: (value?: Stream | PromiseLike<Stream>) => void,
    reject: (reason?: any) => void
  ) {
    req.on('response', res => {
      res.pause();
      res.statusCode === 200
        ? resolve(res)
        : reject(`Bad status code ${res.statusCode}`);
    });
    req.on('error', res => reject(res));
  }
}

export = Docxmerge;
