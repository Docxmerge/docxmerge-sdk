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


class Invitation(object):
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
        'consumed_time': 'datetime',
        'email': 'str',
        'metadata': 'InvitationMetadata',
        'id': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'tenant': 'Tenant',
        'tenant_id': 'str'
    }

    attribute_map = {
        'consumed_time': 'consumedTime',
        'email': 'email',
        'metadata': 'metadata',
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'tenant': 'tenant',
        'tenant_id': 'tenantId'
    }

    def __init__(self, consumed_time=None, email=None, metadata=None, id=None, created=None, modified=None, tenant=None, tenant_id=None):  # noqa: E501
        """Invitation - a model defined in OpenAPI"""  # noqa: E501

        self._consumed_time = None
        self._email = None
        self._metadata = None
        self._id = None
        self._created = None
        self._modified = None
        self._tenant = None
        self._tenant_id = None
        self.discriminator = None

        if consumed_time is not None:
            self.consumed_time = consumed_time
        if email is not None:
            self.email = email
        if metadata is not None:
            self.metadata = metadata
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
    def consumed_time(self):
        """Gets the consumed_time of this Invitation.  # noqa: E501


        :return: The consumed_time of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._consumed_time

    @consumed_time.setter
    def consumed_time(self, consumed_time):
        """Sets the consumed_time of this Invitation.


        :param consumed_time: The consumed_time of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._consumed_time = consumed_time

    @property
    def email(self):
        """Gets the email of this Invitation.  # noqa: E501


        :return: The email of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Invitation.


        :param email: The email of this Invitation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def metadata(self):
        """Gets the metadata of this Invitation.  # noqa: E501


        :return: The metadata of this Invitation.  # noqa: E501
        :rtype: InvitationMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Invitation.


        :param metadata: The metadata of this Invitation.  # noqa: E501
        :type: InvitationMetadata
        """

        self._metadata = metadata

    @property
    def id(self):
        """Gets the id of this Invitation.  # noqa: E501


        :return: The id of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invitation.


        :param id: The id of this Invitation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this Invitation.  # noqa: E501


        :return: The created of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Invitation.


        :param created: The created of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Invitation.  # noqa: E501


        :return: The modified of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Invitation.


        :param modified: The modified of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def tenant(self):
        """Gets the tenant of this Invitation.  # noqa: E501


        :return: The tenant of this Invitation.  # noqa: E501
        :rtype: Tenant
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this Invitation.


        :param tenant: The tenant of this Invitation.  # noqa: E501
        :type: Tenant
        """

        self._tenant = tenant

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Invitation.  # noqa: E501


        :return: The tenant_id of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Invitation.


        :param tenant_id: The tenant_id of this Invitation.  # noqa: E501
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
        if not isinstance(other, Invitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other