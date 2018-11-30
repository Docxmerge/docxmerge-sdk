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


export class StringSegment {
    'buffer'?: string;
    'offset'?: number;
    'length'?: number;
    'value'?: string;
    'hasValue'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "buffer",
            "baseName": "buffer",
            "type": "string"
        },
        {
            "name": "offset",
            "baseName": "offset",
            "type": "number"
        },
        {
            "name": "length",
            "baseName": "length",
            "type": "number"
        },
        {
            "name": "value",
            "baseName": "value",
            "type": "string"
        },
        {
            "name": "hasValue",
            "baseName": "hasValue",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return StringSegment.attributeTypeMap;
    }
}
