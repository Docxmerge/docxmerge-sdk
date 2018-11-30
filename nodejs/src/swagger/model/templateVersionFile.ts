/**
 * DocxMerge
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * OpenAPI spec version: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { AppFile } from './appFile';
import { Report } from './report';
import { Template } from './template';
import { Tenant } from './tenant';

export class TemplateVersionFile {
    'template'?: Template;
    'templateId'?: string;
    'appFileId'?: string;
    'appFile'?: AppFile;
    'status'?: TemplateVersionFile.StatusEnum;
    'version'?: number;
    'attributes'?: Array<string>;
    'example'?: { [key: string]: any; };
    'reports'?: Array<Report>;
    'id'?: string;
    'created'?: Date;
    'modified'?: Date;
    'tenant'?: Tenant;
    'tenantId'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "template",
            "baseName": "template",
            "type": "Template"
        },
        {
            "name": "templateId",
            "baseName": "templateId",
            "type": "string"
        },
        {
            "name": "appFileId",
            "baseName": "appFileId",
            "type": "string"
        },
        {
            "name": "appFile",
            "baseName": "appFile",
            "type": "AppFile"
        },
        {
            "name": "status",
            "baseName": "status",
            "type": "TemplateVersionFile.StatusEnum"
        },
        {
            "name": "version",
            "baseName": "version",
            "type": "number"
        },
        {
            "name": "attributes",
            "baseName": "attributes",
            "type": "Array<string>"
        },
        {
            "name": "example",
            "baseName": "example",
            "type": "{ [key: string]: any; }"
        },
        {
            "name": "reports",
            "baseName": "reports",
            "type": "Array<Report>"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "created",
            "baseName": "created",
            "type": "Date"
        },
        {
            "name": "modified",
            "baseName": "modified",
            "type": "Date"
        },
        {
            "name": "tenant",
            "baseName": "tenant",
            "type": "Tenant"
        },
        {
            "name": "tenantId",
            "baseName": "tenantId",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return TemplateVersionFile.attributeTypeMap;
    }
}

export namespace TemplateVersionFile {
    export enum StatusEnum {
        DRAFT = <any> 'DRAFT',
        TESTING = <any> 'TESTING',
        PRODUCTION = <any> 'PRODUCTION'
    }
}