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


class ReportListResponseModel(object):
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
        'reports': 'list[Report]',
        'total': 'int'
    }

    attribute_map = {
        'reports': 'reports',
        'total': 'total'
    }

    def __init__(self, reports=None, total=None):  # noqa: E501
        """ReportListResponseModel - a model defined in OpenAPI"""  # noqa: E501

        self._reports = None
        self._total = None
        self.discriminator = None

        if reports is not None:
            self.reports = reports
        if total is not None:
            self.total = total

    @property
    def reports(self):
        """Gets the reports of this ReportListResponseModel.  # noqa: E501


        :return: The reports of this ReportListResponseModel.  # noqa: E501
        :rtype: list[Report]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this ReportListResponseModel.


        :param reports: The reports of this ReportListResponseModel.  # noqa: E501
        :type: list[Report]
        """

        self._reports = reports

    @property
    def total(self):
        """Gets the total of this ReportListResponseModel.  # noqa: E501


        :return: The total of this ReportListResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ReportListResponseModel.


        :param total: The total of this ReportListResponseModel.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, ReportListResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other