# coding: utf-8

"""
    Glean Client API

    # Introduction These are the public APIs to enable implementing a custom client interface to the Glean system.  # Usage guidelines This API is evolving fast. Glean will provide advance notice of any planned backwards incompatible changes along with a 6-month sunset period for anything that requires developers to adopt the new versions.  # SDK Client bindings for the API can be generated for most popular languages (Python, Java, NodeJS, etc). To do so:  Download the OpenAPI specification for the API, by clicking on one of the following options: 1. [Download JSON specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.json?branch=main&download=true) 2. [Download YAML specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.yaml?branch=main&download=true)  Use [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) to generate bindings for your language of choice, for example: ```bash shell $ npx @openapitools/openapi-generator-cli@latest generate -i client_api.yaml -g go ```  To see available languages: ```bash shell $ npx @openapitools/openapi-generator-cli@latest list ```  Determine the host you need to connect to. This will be the URL of the backend for your Glean deployment, for example, customer-be.glean.com 

    The version of the OpenAPI document: 0.9.0
    Contact: support@glean.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.auth_token import AuthToken
from openapi_client.models.session_info import SessionInfo
from typing import Optional, Set
from typing_extensions import Self

class AutocompleteRequest(BaseModel):
    """
    AutocompleteRequest
    """ # noqa: E501
    tracking_token: Optional[StrictStr] = Field(default=None, alias="trackingToken")
    session_info: Optional[SessionInfo] = Field(default=None, alias="sessionInfo")
    query: Optional[StrictStr] = Field(default=None, description="Partially typed query.")
    datasources_filter: Optional[List[StrictStr]] = Field(default=None, description="Filter results to only those relevant to one or more datasources (e.g. jira, gdrive). Results are unfiltered if missing.", alias="datasourcesFilter")
    datasource: Optional[StrictStr] = Field(default=None, description="Filter to only return results relevant to the given datasource.")
    result_types: Optional[List[StrictStr]] = Field(default=None, description="Filter to only return results of the given type(s). All types may be returned if omitted.", alias="resultTypes")
    result_size: Optional[StrictInt] = Field(default=None, description="Maximum number of results to be returned. If no value is provided, the backend will cap at 200. ", alias="resultSize")
    auth_tokens: Optional[List[AuthToken]] = Field(default=None, description="Auth tokens which may be used for federated results.", alias="authTokens")
    __properties: ClassVar[List[str]] = ["trackingToken", "sessionInfo", "query", "datasourcesFilter", "datasource", "resultTypes", "resultSize", "authTokens"]

    @field_validator('result_types')
    def result_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ADDITIONAL_DOCUMENT', 'APP', 'BROWSER_HISTORY', 'DATASOURCE', 'DOCUMENT', 'ENTITY', 'GOLINK', 'HISTORY', 'NEW_CHAT', 'OPERATOR', 'OPERATOR_VALUE', 'QUICKLINK', 'SUGGESTION']):
                raise ValueError("each list item must be one of ('ADDITIONAL_DOCUMENT', 'APP', 'BROWSER_HISTORY', 'DATASOURCE', 'DOCUMENT', 'ENTITY', 'GOLINK', 'HISTORY', 'NEW_CHAT', 'OPERATOR', 'OPERATOR_VALUE', 'QUICKLINK', 'SUGGESTION')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AutocompleteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of session_info
        if self.session_info:
            _dict['sessionInfo'] = self.session_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in auth_tokens (list)
        _items = []
        if self.auth_tokens:
            for _item_auth_tokens in self.auth_tokens:
                if _item_auth_tokens:
                    _items.append(_item_auth_tokens.to_dict())
            _dict['authTokens'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutocompleteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "trackingToken": obj.get("trackingToken"),
            "sessionInfo": SessionInfo.from_dict(obj["sessionInfo"]) if obj.get("sessionInfo") is not None else None,
            "query": obj.get("query"),
            "datasourcesFilter": obj.get("datasourcesFilter"),
            "datasource": obj.get("datasource"),
            "resultTypes": obj.get("resultTypes"),
            "resultSize": obj.get("resultSize"),
            "authTokens": [AuthToken.from_dict(_item) for _item in obj["authTokens"]] if obj.get("authTokens") is not None else None
        })
        return _obj


