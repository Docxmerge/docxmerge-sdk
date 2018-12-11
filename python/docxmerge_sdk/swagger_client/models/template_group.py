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


class TemplateGroup(object):
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
        'group': 'Group',
        'group_id': 'str',
        'id': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'tenant': 'Tenant',
        'tenant_id': 'str'
    }

    attribute_map = {
        'template': 'template',
        'template_id': 'templateId',
        'group': 'group',
        'group_id': 'groupId',
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'tenant': 'tenant',
        'tenant_id': 'tenantId'
    }

    def __init__(self, template=None, template_id=None, group=None, group_id=None, id=None, created=None, modified=None, tenant=None, tenant_id=None):  # noqa: E501
        """TemplateGroup - a model defined in OpenAPI"""  # noqa: E501

        self._template = None
        self._template_id = None
        self._group = None
        self._group_id = None
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
        if group is not None:
            self.group = group
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if tenant is not None:
            self.tenant = tenant
        self.tenant_id = tenant_id

    @property
    def template(self):
        """Gets the template of this TemplateGroup.  # noqa: E501


        :return: The template of this TemplateGroup.  # noqa: E501
        :rtype: Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this TemplateGroup.


        :param template: The template of this TemplateGroup.  # noqa: E501
        :type: Template
        """

        self._template = template

    @property
    def template_id(self):
        """Gets the template_id of this TemplateGroup.  # noqa: E501


        :return: The template_id of this TemplateGroup.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TemplateGroup.


        :param template_id: The template_id of this TemplateGroup.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def group(self):
        """Gets the group of this TemplateGroup.  # noqa: E501


        :return: The group of this TemplateGroup.  # noqa: E501
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this TemplateGroup.


        :param group: The group of this TemplateGroup.  # noqa: E501
        :type: Group
        """

        self._group = group

    @property
    def group_id(self):
        """Gets the group_id of this TemplateGroup.  # noqa: E501


        :return: The group_id of this TemplateGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TemplateGroup.


        :param group_id: The group_id of this TemplateGroup.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this TemplateGroup.  # noqa: E501


        :return: The id of this TemplateGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateGroup.


        :param id: The id of this TemplateGroup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this TemplateGroup.  # noqa: E501


        :return: The created of this TemplateGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TemplateGroup.


        :param created: The created of this TemplateGroup.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this TemplateGroup.  # noqa: E501


        :return: The modified of this TemplateGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this TemplateGroup.


        :param modified: The modified of this TemplateGroup.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def tenant(self):
        """Gets the tenant of this TemplateGroup.  # noqa: E501


        :return: The tenant of this TemplateGroup.  # noqa: E501
        :rtype: Tenant
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this TemplateGroup.


        :param tenant: The tenant of this TemplateGroup.  # noqa: E501
        :type: Tenant
        """

        self._tenant = tenant

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TemplateGroup.  # noqa: E501


        :return: The tenant_id of this TemplateGroup.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TemplateGroup.


        :param tenant_id: The tenant_id of this TemplateGroup.  # noqa: E501
        :type: str
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, TemplateGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
