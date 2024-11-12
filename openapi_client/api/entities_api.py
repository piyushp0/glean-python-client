# coding: utf-8

"""
    Glean Client API

    # Introduction These are the public APIs to enable implementing a custom client interface to the Glean system.  # Usage guidelines This API is evolving fast. Glean will provide advance notice of any planned backwards incompatible changes along with a 6-month sunset period for anything that requires developers to adopt the new versions.  # SDK Client bindings for the API can be generated for most popular languages (Python, Java, NodeJS, etc). To do so:  Download the OpenAPI specification for the API, by clicking on one of the following options: 1. [Download JSON specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.json?branch=main&download=true) 2. [Download YAML specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.yaml?branch=main&download=true)  Use [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) to generate bindings for your language of choice, for example: ```bash shell $ npx @openapitools/openapi-generator-cli@latest generate -i client_api.yaml -g go ```  To see available languages: ```bash shell $ npx @openapitools/openapi-generator-cli@latest list ```  Determine the host you need to connect to. This will be the URL of the backend for your Glean deployment, for example, customer-be.glean.com 

    The version of the OpenAPI document: 0.9.0
    Contact: support@glean.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_client.models.list_entities_request import ListEntitiesRequest
from openapi_client.models.list_entities_response import ListEntitiesResponse
from openapi_client.models.people_request import PeopleRequest
from openapi_client.models.people_response import PeopleResponse

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class EntitiesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def listentities(
        self,
        payload: Annotated[ListEntitiesRequest, Field(description="List people request")],
        x_scio_actas: Annotated[Optional[StrictStr], Field(description="Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).")] = None,
        x_glean_auth_type: Annotated[Optional[StrictStr], Field(description="Auth type being used to access the endpoint (should be non-empty only for global tokens).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ListEntitiesResponse:
        """List entities

        List some set of details for all entities that fit the given criteria and return in the requested order. Does not support negation in filters, assumes relation type EQUALS. There is a limit of 10000 entities that can be retrieved via this endpoint.

        :param payload: List people request (required)
        :type payload: ListEntitiesRequest
        :param x_scio_actas: Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).
        :type x_scio_actas: str
        :param x_glean_auth_type: Auth type being used to access the endpoint (should be non-empty only for global tokens).
        :type x_glean_auth_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._listentities_serialize(
            payload=payload,
            x_scio_actas=x_scio_actas,
            x_glean_auth_type=x_glean_auth_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListEntitiesResponse",
            '400': None,
            '401': None,
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def listentities_with_http_info(
        self,
        payload: Annotated[ListEntitiesRequest, Field(description="List people request")],
        x_scio_actas: Annotated[Optional[StrictStr], Field(description="Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).")] = None,
        x_glean_auth_type: Annotated[Optional[StrictStr], Field(description="Auth type being used to access the endpoint (should be non-empty only for global tokens).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ListEntitiesResponse]:
        """List entities

        List some set of details for all entities that fit the given criteria and return in the requested order. Does not support negation in filters, assumes relation type EQUALS. There is a limit of 10000 entities that can be retrieved via this endpoint.

        :param payload: List people request (required)
        :type payload: ListEntitiesRequest
        :param x_scio_actas: Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).
        :type x_scio_actas: str
        :param x_glean_auth_type: Auth type being used to access the endpoint (should be non-empty only for global tokens).
        :type x_glean_auth_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._listentities_serialize(
            payload=payload,
            x_scio_actas=x_scio_actas,
            x_glean_auth_type=x_glean_auth_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListEntitiesResponse",
            '400': None,
            '401': None,
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def listentities_without_preload_content(
        self,
        payload: Annotated[ListEntitiesRequest, Field(description="List people request")],
        x_scio_actas: Annotated[Optional[StrictStr], Field(description="Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).")] = None,
        x_glean_auth_type: Annotated[Optional[StrictStr], Field(description="Auth type being used to access the endpoint (should be non-empty only for global tokens).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List entities

        List some set of details for all entities that fit the given criteria and return in the requested order. Does not support negation in filters, assumes relation type EQUALS. There is a limit of 10000 entities that can be retrieved via this endpoint.

        :param payload: List people request (required)
        :type payload: ListEntitiesRequest
        :param x_scio_actas: Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).
        :type x_scio_actas: str
        :param x_glean_auth_type: Auth type being used to access the endpoint (should be non-empty only for global tokens).
        :type x_glean_auth_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._listentities_serialize(
            payload=payload,
            x_scio_actas=x_scio_actas,
            x_glean_auth_type=x_glean_auth_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListEntitiesResponse",
            '400': None,
            '401': None,
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _listentities_serialize(
        self,
        payload,
        x_scio_actas,
        x_glean_auth_type,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_scio_actas is not None:
            _header_params['X-Scio-Actas'] = x_scio_actas
        if x_glean_auth_type is not None:
            _header_params['X-Glean-Auth-Type'] = x_glean_auth_type
        # process the form parameters
        # process the body parameter
        if payload is not None:
            _body_params = payload


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/listentities',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def people(
        self,
        payload: Annotated[PeopleRequest, Field(description="People request")],
        x_scio_actas: Annotated[Optional[StrictStr], Field(description="Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).")] = None,
        x_glean_auth_type: Annotated[Optional[StrictStr], Field(description="Auth type being used to access the endpoint (should be non-empty only for global tokens).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PeopleResponse:
        """Read people

        Read people details for the given IDs.

        :param payload: People request (required)
        :type payload: PeopleRequest
        :param x_scio_actas: Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).
        :type x_scio_actas: str
        :param x_glean_auth_type: Auth type being used to access the endpoint (should be non-empty only for global tokens).
        :type x_glean_auth_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._people_serialize(
            payload=payload,
            x_scio_actas=x_scio_actas,
            x_glean_auth_type=x_glean_auth_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PeopleResponse",
            '400': None,
            '401': None,
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def people_with_http_info(
        self,
        payload: Annotated[PeopleRequest, Field(description="People request")],
        x_scio_actas: Annotated[Optional[StrictStr], Field(description="Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).")] = None,
        x_glean_auth_type: Annotated[Optional[StrictStr], Field(description="Auth type being used to access the endpoint (should be non-empty only for global tokens).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PeopleResponse]:
        """Read people

        Read people details for the given IDs.

        :param payload: People request (required)
        :type payload: PeopleRequest
        :param x_scio_actas: Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).
        :type x_scio_actas: str
        :param x_glean_auth_type: Auth type being used to access the endpoint (should be non-empty only for global tokens).
        :type x_glean_auth_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._people_serialize(
            payload=payload,
            x_scio_actas=x_scio_actas,
            x_glean_auth_type=x_glean_auth_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PeopleResponse",
            '400': None,
            '401': None,
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def people_without_preload_content(
        self,
        payload: Annotated[PeopleRequest, Field(description="People request")],
        x_scio_actas: Annotated[Optional[StrictStr], Field(description="Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).")] = None,
        x_glean_auth_type: Annotated[Optional[StrictStr], Field(description="Auth type being used to access the endpoint (should be non-empty only for global tokens).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Read people

        Read people details for the given IDs.

        :param payload: People request (required)
        :type payload: PeopleRequest
        :param x_scio_actas: Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).
        :type x_scio_actas: str
        :param x_glean_auth_type: Auth type being used to access the endpoint (should be non-empty only for global tokens).
        :type x_glean_auth_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._people_serialize(
            payload=payload,
            x_scio_actas=x_scio_actas,
            x_glean_auth_type=x_glean_auth_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PeopleResponse",
            '400': None,
            '401': None,
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _people_serialize(
        self,
        payload,
        x_scio_actas,
        x_glean_auth_type,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_scio_actas is not None:
            _header_params['X-Scio-Actas'] = x_scio_actas
        if x_glean_auth_type is not None:
            _header_params['X-Glean-Auth-Type'] = x_glean_auth_type
        # process the form parameters
        # process the body parameter
        if payload is not None:
            _body_params = payload


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/people',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


