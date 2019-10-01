require "docxmerge/version"
require 'net/https'
require 'uri'
require 'json'
require 'rest-client'

class BadRequestError < StandardError
end
module Docxmerge
  # Your code goes here...
  class Docxmerge
    def initialize(api_key, tenant, base_uri)
      @api_key = api_key
      @tenant = tenant || "default"
      @base_uri = base_uri || "https://api.docxmerge.com"
    end

    def render_template(template_name, data, conversion_type, version = "")
      uri = "#{@base_uri}/api/v1/Admin/RenderTemplate"
      headers = get_headers
      headers["content-type"] = "application/json"
      response = RestClient.post(uri,
                                 {
                                     template: template_name,
                                     data: data,
                                     version: version,
                                     conversionType: conversion_type,
                                 }.to_json,
                                 headers,
      )
      raise BadRequestError.new unless response.code == 200
      response.body
    end

    def render_file(file_param, data, conversion_type)
      uri = "#{@base_uri}/api/v1/Admin/RenderFile"
      response = RestClient.post(uri,
                                 {
                                     :multipart => true,
                                     :file => file_param,
                                     :data => data.to_json,
                                     :conversionType => conversion_type,
                                 },
                                 get_headers,
      )
      raise BadRequestError.new unless response.code == 200
      response.body
    end

    def render_url(url, data, conversion_type, version = "")
      uri = "#{@base_uri}/api/v1/Admin/RenderUrl"
      headers = get_headers
      headers["content-type"] = "application/json"
      response = RestClient.post(uri,
                                 {
                                     url: url,
                                     data: data,
                                     version: version,
                                     conversionType: conversion_type,
                                 }.to_json,
                                 headers,
      )
      raise BadRequestError.new unless response.code == 200
      response.body
    end

    private

    def get_headers
      {
          "api-key" => @api_key,
          "x-tenant" => @tenant,
      }
    end
  end
end
