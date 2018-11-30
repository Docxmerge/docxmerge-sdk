# coding: utf-8

"""
    DocxMerge

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from docxmerge_sdk.swagger_client.api_client import ApiClient


class PaymentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_by_tenant_payments_by_id_get(self, id, tenant, **kwargs):  # noqa: E501
        """Get payment by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_by_tenant_payments_by_id_get(id, tenant, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Payment id (required)
        :param str tenant: Tenant id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_by_tenant_payments_by_id_get_with_http_info(id, tenant, **kwargs)  # noqa: E501
        else:
            (data) = self.api_by_tenant_payments_by_id_get_with_http_info(id, tenant, **kwargs)  # noqa: E501
            return data

    def api_by_tenant_payments_by_id_get_with_http_info(self, id, tenant, **kwargs):  # noqa: E501
        """Get payment by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_by_tenant_payments_by_id_get_with_http_info(id, tenant, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Payment id (required)
        :param str tenant: Tenant id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'tenant']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_by_tenant_payments_by_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_by_tenant_payments_by_id_get`")  # noqa: E501
        # verify the required parameter 'tenant' is set
        if ('tenant' not in local_var_params or
                local_var_params['tenant'] is None):
            raise ValueError("Missing the required parameter `tenant` when calling `api_by_tenant_payments_by_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'tenant' in local_var_params:
            path_params['tenant'] = local_var_params['tenant']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/{tenant}/payments/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_by_tenant_payments_get(self, tenant, **kwargs):  # noqa: E501
        """Get all the payments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_by_tenant_payments_get(tenant, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant: Tenant id (required)
        :return: list[PaymentTransaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_by_tenant_payments_get_with_http_info(tenant, **kwargs)  # noqa: E501
        else:
            (data) = self.api_by_tenant_payments_get_with_http_info(tenant, **kwargs)  # noqa: E501
            return data

    def api_by_tenant_payments_get_with_http_info(self, tenant, **kwargs):  # noqa: E501
        """Get all the payments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_by_tenant_payments_get_with_http_info(tenant, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant: Tenant id (required)
        :return: list[PaymentTransaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tenant']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_by_tenant_payments_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tenant' is set
        if ('tenant' not in local_var_params or
                local_var_params['tenant'] is None):
            raise ValueError("Missing the required parameter `tenant` when calling `api_by_tenant_payments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant' in local_var_params:
            path_params['tenant'] = local_var_params['tenant']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/{tenant}/payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PaymentTransaction]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_by_tenant_payments_post(self, tenant, token, payment_request_model, **kwargs):  # noqa: E501
        """Add credits to the tenant using stripe  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_by_tenant_payments_post(tenant, token, payment_request_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant: Tenant id (required)
        :param str token: Stripe token (required)
        :param PaymentRequestModel payment_request_model: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_by_tenant_payments_post_with_http_info(tenant, token, payment_request_model, **kwargs)  # noqa: E501
        else:
            (data) = self.api_by_tenant_payments_post_with_http_info(tenant, token, payment_request_model, **kwargs)  # noqa: E501
            return data

    def api_by_tenant_payments_post_with_http_info(self, tenant, token, payment_request_model, **kwargs):  # noqa: E501
        """Add credits to the tenant using stripe  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_by_tenant_payments_post_with_http_info(tenant, token, payment_request_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant: Tenant id (required)
        :param str token: Stripe token (required)
        :param PaymentRequestModel payment_request_model: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tenant', 'token', 'payment_request_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_by_tenant_payments_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tenant' is set
        if ('tenant' not in local_var_params or
                local_var_params['tenant'] is None):
            raise ValueError("Missing the required parameter `tenant` when calling `api_by_tenant_payments_post`")  # noqa: E501
        # verify the required parameter 'token' is set
        if ('token' not in local_var_params or
                local_var_params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `api_by_tenant_payments_post`")  # noqa: E501
        # verify the required parameter 'payment_request_model' is set
        if ('payment_request_model' not in local_var_params or
                local_var_params['payment_request_model'] is None):
            raise ValueError("Missing the required parameter `payment_request_model` when calling `api_by_tenant_payments_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant' in local_var_params:
            path_params['tenant'] = local_var_params['tenant']  # noqa: E501

        query_params = []
        if 'token' in local_var_params:
            query_params.append(('token', local_var_params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_request_model' in local_var_params:
            body_params = local_var_params['payment_request_model']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/{tenant}/payments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
