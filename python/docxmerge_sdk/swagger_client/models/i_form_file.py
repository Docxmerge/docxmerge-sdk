# coding: utf-8

"""
    DocxMerge

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class IFormFile(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'content_type': 'str',
        'content_disposition': 'str',
        'headers': 'dict(str, list[str])',
        'length': 'int',
        'name': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'content_type': 'contentType',
        'content_disposition': 'contentDisposition',
        'headers': 'headers',
        'length': 'length',
        'name': 'name',
        'file_name': 'fileName'
    }

    def __init__(self, content_type=None, content_disposition=None, headers=None, length=None, name=None, file_name=None):  # noqa: E501
        """IFormFile - a model defined in OpenAPI"""  # noqa: E501

        self._content_type = None
        self._content_disposition = None
        self._headers = None
        self._length = None
        self._name = None
        self._file_name = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type
        if content_disposition is not None:
            self.content_disposition = content_disposition
        if headers is not None:
            self.headers = headers
        if length is not None:
            self.length = length
        if name is not None:
            self.name = name
        if file_name is not None:
            self.file_name = file_name

    @property
    def content_type(self):
        """Gets the content_type of this IFormFile.  # noqa: E501


        :return: The content_type of this IFormFile.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this IFormFile.


        :param content_type: The content_type of this IFormFile.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def content_disposition(self):
        """Gets the content_disposition of this IFormFile.  # noqa: E501


        :return: The content_disposition of this IFormFile.  # noqa: E501
        :rtype: str
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition):
        """Sets the content_disposition of this IFormFile.


        :param content_disposition: The content_disposition of this IFormFile.  # noqa: E501
        :type: str
        """

        self._content_disposition = content_disposition

    @property
    def headers(self):
        """Gets the headers of this IFormFile.  # noqa: E501


        :return: The headers of this IFormFile.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this IFormFile.


        :param headers: The headers of this IFormFile.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._headers = headers

    @property
    def length(self):
        """Gets the length of this IFormFile.  # noqa: E501


        :return: The length of this IFormFile.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this IFormFile.


        :param length: The length of this IFormFile.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def name(self):
        """Gets the name of this IFormFile.  # noqa: E501


        :return: The name of this IFormFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IFormFile.


        :param name: The name of this IFormFile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file_name(self):
        """Gets the file_name of this IFormFile.  # noqa: E501


        :return: The file_name of this IFormFile.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this IFormFile.


        :param file_name: The file_name of this IFormFile.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IFormFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
