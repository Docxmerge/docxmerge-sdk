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


class TemplateVersionFile(object):
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
        'template': 'Template',
        'template_id': 'str',
        'app_file_id': 'str',
        'app_file': 'AppFile',
        'status': 'str',
        'version': 'int',
        'attributes': 'list[str]',
        'example': 'dict(str, object)',
        'reports': 'list[Report]',
        'id': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'tenant': 'Tenant',
        'tenant_id': 'str'
    }

    attribute_map = {
        'template': 'template',
        'template_id': 'templateId',
        'app_file_id': 'appFileId',
        'app_file': 'appFile',
        'status': 'status',
        'version': 'version',
        'attributes': 'attributes',
        'example': 'example',
        'reports': 'reports',
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'tenant': 'tenant',
        'tenant_id': 'tenantId'
    }

    def __init__(self, template=None, template_id=None, app_file_id=None, app_file=None, status=None, version=None, attributes=None, example=None, reports=None, id=None, created=None, modified=None, tenant=None, tenant_id=None):  # noqa: E501
        """TemplateVersionFile - a model defined in OpenAPI"""  # noqa: E501

        self._template = None
        self._template_id = None
        self._app_file_id = None
        self._app_file = None
        self._status = None
        self._version = None
        self._attributes = None
        self._example = None
        self._reports = None
        self._id = None
        self._created = None
        self._modified = None
        self._tenant = None
        self._tenant_id = None
        self.discriminator = None

        if template is not None:
            self.template = template
        if template_id is not None:
            self.template_id = template_id
        if app_file_id is not None:
            self.app_file_id = app_file_id
        if app_file is not None:
            self.app_file = app_file
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if attributes is not None:
            self.attributes = attributes
        if example is not None:
            self.example = example
        if reports is not None:
            self.reports = reports
        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if tenant is not None:
            self.tenant = tenant
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def template(self):
        """Gets the template of this TemplateVersionFile.  # noqa: E501


        :return: The template of this TemplateVersionFile.  # noqa: E501
        :rtype: Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this TemplateVersionFile.


        :param template: The template of this TemplateVersionFile.  # noqa: E501
        :type: Template
        """

        self._template = template

    @property
    def template_id(self):
        """Gets the template_id of this TemplateVersionFile.  # noqa: E501


        :return: The template_id of this TemplateVersionFile.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TemplateVersionFile.


        :param template_id: The template_id of this TemplateVersionFile.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def app_file_id(self):
        """Gets the app_file_id of this TemplateVersionFile.  # noqa: E501


        :return: The app_file_id of this TemplateVersionFile.  # noqa: E501
        :rtype: str
        """
        return self._app_file_id

    @app_file_id.setter
    def app_file_id(self, app_file_id):
        """Sets the app_file_id of this TemplateVersionFile.


        :param app_file_id: The app_file_id of this TemplateVersionFile.  # noqa: E501
        :type: str
        """

        self._app_file_id = app_file_id

    @property
    def app_file(self):
        """Gets the app_file of this TemplateVersionFile.  # noqa: E501


        :return: The app_file of this TemplateVersionFile.  # noqa: E501
        :rtype: AppFile
        """
        return self._app_file

    @app_file.setter
    def app_file(self, app_file):
        """Sets the app_file of this TemplateVersionFile.


        :param app_file: The app_file of this TemplateVersionFile.  # noqa: E501
        :type: AppFile
        """

        self._app_file = app_file

    @property
    def status(self):
        """Gets the status of this TemplateVersionFile.  # noqa: E501


        :return: The status of this TemplateVersionFile.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TemplateVersionFile.


        :param status: The status of this TemplateVersionFile.  # noqa: E501
        :type: str
        """
        allowed_values = ["DRAFT", "TESTING", "PRODUCTION"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def version(self):
        """Gets the version of this TemplateVersionFile.  # noqa: E501


        :return: The version of this TemplateVersionFile.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TemplateVersionFile.


        :param version: The version of this TemplateVersionFile.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def attributes(self):
        """Gets the attributes of this TemplateVersionFile.  # noqa: E501


        :return: The attributes of this TemplateVersionFile.  # noqa: E501
        :rtype: list[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TemplateVersionFile.


        :param attributes: The attributes of this TemplateVersionFile.  # noqa: E501
        :type: list[str]
        """

        self._attributes = attributes

    @property
    def example(self):
        """Gets the example of this TemplateVersionFile.  # noqa: E501


        :return: The example of this TemplateVersionFile.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this TemplateVersionFile.


        :param example: The example of this TemplateVersionFile.  # noqa: E501
        :type: dict(str, object)
        """

        self._example = example

    @property
    def reports(self):
        """Gets the reports of this TemplateVersionFile.  # noqa: E501


        :return: The reports of this TemplateVersionFile.  # noqa: E501
        :rtype: list[Report]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this TemplateVersionFile.


        :param reports: The reports of this TemplateVersionFile.  # noqa: E501
        :type: list[Report]
        """

        self._reports = reports

    @property
    def id(self):
        """Gets the id of this TemplateVersionFile.  # noqa: E501


        :return: The id of this TemplateVersionFile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateVersionFile.


        :param id: The id of this TemplateVersionFile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this TemplateVersionFile.  # noqa: E501


        :return: The created of this TemplateVersionFile.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TemplateVersionFile.


        :param created: The created of this TemplateVersionFile.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this TemplateVersionFile.  # noqa: E501


        :return: The modified of this TemplateVersionFile.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this TemplateVersionFile.


        :param modified: The modified of this TemplateVersionFile.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def tenant(self):
        """Gets the tenant of this TemplateVersionFile.  # noqa: E501


        :return: The tenant of this TemplateVersionFile.  # noqa: E501
        :rtype: Tenant
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this TemplateVersionFile.


        :param tenant: The tenant of this TemplateVersionFile.  # noqa: E501
        :type: Tenant
        """

        self._tenant = tenant

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TemplateVersionFile.  # noqa: E501


        :return: The tenant_id of this TemplateVersionFile.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TemplateVersionFile.


        :param tenant_id: The tenant_id of this TemplateVersionFile.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

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
        if not isinstance(other, TemplateVersionFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other