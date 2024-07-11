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
from openapi_client.models.feed_request_options import FeedRequestOptions
from openapi_client.models.session_info import SessionInfo
from typing import Optional, Set
from typing_extensions import Self

class FeedRequest(BaseModel):
    """
    FeedRequest
    """ # noqa: E501
    categories: Optional[List[StrictStr]] = Field(default=None, description="Categories of content requested. An allowlist gives flexibility to request content separately or together.")
    request_options: Optional[FeedRequestOptions] = Field(default=None, alias="requestOptions")
    timeout_millis: Optional[StrictInt] = Field(default=None, description="Timeout in milliseconds for the request. A `408` error will be returned if handling the request takes longer.", alias="timeoutMillis")
    session_info: Optional[SessionInfo] = Field(default=None, alias="sessionInfo")
    __properties: ClassVar[List[str]] = ["categories", "requestOptions", "timeoutMillis", "sessionInfo"]

    @field_validator('categories')
    def categories_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['DOCUMENT_SUGGESTION', 'DOCUMENT_SUGGESTION_SCENARIO', 'TRENDING_DOCUMENT', 'VERIFICATION_REMINDER', 'EVENT', 'ANNOUNCEMENT', 'MENTION', 'DATASOURCE_AFFINITY', 'RECENT', 'COMPANY_RESOURCE', 'EXPERIMENTAL', 'PEOPLE_CELEBRATIONS', 'DISPLAYABLE_LIST', 'SOCIAL_LINK', 'EXTERNAL_TASKS', 'ZERO_STATE_CHAT_SUGGESTION', 'ZERO_STATE_CHAT_TOOL_SUGGESTION']):
                raise ValueError("each list item must be one of ('DOCUMENT_SUGGESTION', 'DOCUMENT_SUGGESTION_SCENARIO', 'TRENDING_DOCUMENT', 'VERIFICATION_REMINDER', 'EVENT', 'ANNOUNCEMENT', 'MENTION', 'DATASOURCE_AFFINITY', 'RECENT', 'COMPANY_RESOURCE', 'EXPERIMENTAL', 'PEOPLE_CELEBRATIONS', 'DISPLAYABLE_LIST', 'SOCIAL_LINK', 'EXTERNAL_TASKS', 'ZERO_STATE_CHAT_SUGGESTION', 'ZERO_STATE_CHAT_TOOL_SUGGESTION')")
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
        """Create an instance of FeedRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of request_options
        if self.request_options:
            _dict['requestOptions'] = self.request_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session_info
        if self.session_info:
            _dict['sessionInfo'] = self.session_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FeedRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "categories": obj.get("categories"),
            "requestOptions": FeedRequestOptions.from_dict(obj["requestOptions"]) if obj.get("requestOptions") is not None else None,
            "timeoutMillis": obj.get("timeoutMillis"),
            "sessionInfo": SessionInfo.from_dict(obj["sessionInfo"]) if obj.get("sessionInfo") is not None else None
        })
        return _obj


