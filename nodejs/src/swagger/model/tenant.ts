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

import { Invitation } from './invitation';
import { TenantUser } from './tenantUser';

export class Tenant {
    'id'?: string;
    'created'?: Date;
    'modified'?: Date;
    'name'?: string;
    'apiKey'?: string;
    'users'?: Array<TenantUser>;
    'invitations'?: Array<Invitation>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
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
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "apiKey",
            "baseName": "apiKey",
            "type": "string"
        },
        {
            "name": "users",
            "baseName": "users",
            "type": "Array<TenantUser>"
        },
        {
            "name": "invitations",
            "baseName": "invitations",
            "type": "Array<Invitation>"
        }    ];

    static getAttributeTypeMap() {
        return Tenant.attributeTypeMap;
    }
}

