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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AuthConfig(BaseModel):
    """
    Config for tool's authentication method.
    """ # noqa: E501
    is_on_prem: Optional[StrictBool] = Field(default=None, description="Whether or not this tool is hosted on-premise.", alias="isOnPrem")
    type: Optional[StrictStr] = Field(default=None, description="The type of authentication being used. Use 'OAUTH_*' when Glean calls an external API (e.g., Jira) on behalf of a user to obtain an OAuth token. 'OAUTH_ADMIN' utilizes an admin token for external API calls on behalf all users. 'OAUTH_USER' uses individual user tokens for external API calls.")
    status: Optional[StrictStr] = Field(default=None, description="Auth status of the tool.")
    client_url: Optional[StrictStr] = Field(default=None, description="The URL where users will be directed to start the OAuth flow.")
    scopes: Optional[List[StrictStr]] = Field(default=None, description="A list of strings denoting the different scopes or access levels required by the tool.")
    authorization_url: Optional[StrictStr] = Field(default=None, description="The OAuth provider's endpoint, where access tokens are requested.")
    __properties: ClassVar[List[str]] = ["isOnPrem", "type", "status", "client_url", "scopes", "authorization_url"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NONE', 'OAUTH_USER', 'OAUTH_ADMIN', 'API_KEY', 'BASIC_AUTH']):
            raise ValueError("must be one of enum values ('NONE', 'OAUTH_USER', 'OAUTH_ADMIN', 'API_KEY', 'BASIC_AUTH')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AWAITING_AUTH', 'AUTHORIZED']):
            raise ValueError("must be one of enum values ('AWAITING_AUTH', 'AUTHORIZED')")
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
        """Create an instance of AuthConfig from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isOnPrem": obj.get("isOnPrem"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "client_url": obj.get("client_url"),
            "scopes": obj.get("scopes"),
            "authorization_url": obj.get("authorization_url")
        })
        return _obj


