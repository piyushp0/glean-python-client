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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.auth_config import AuthConfig
from openapi_client.models.person_object import PersonObject
from typing import Optional, Set
from typing_extensions import Self

class ToolMetadata(BaseModel):
    """
    The manifest for a tool that can be used to augment Glean Assistant.
    """ # noqa: E501
    type: StrictStr = Field(description="The type of tool.")
    name: StrictStr = Field(description="Unique identifier for the tool. Name should be understandable by the LLM, and will be used to invoke a tool.")
    display_name: StrictStr = Field(description="Human understandable name of the tool. Max 50 characters.", alias="displayName")
    tool_id: Optional[StrictStr] = Field(default=None, description="An opaque id which is unique identifier for the tool.", alias="toolId")
    display_description: StrictStr = Field(description="Description of the tool meant for a human.", alias="displayDescription")
    logo_url: Optional[StrictStr] = Field(default=None, description="URL used to fetch the logo.", alias="logoUrl")
    object_name: Optional[StrictStr] = Field(default=None, description="Name of the generated object. This will be used to indicate to the end user what the generated object contains.", alias="objectName")
    created_by: Optional[PersonObject] = Field(default=None, alias="createdBy")
    last_updated_by: Optional[PersonObject] = Field(default=None, alias="lastUpdatedBy")
    created_at: Optional[datetime] = Field(default=None, description="The time the tool was created in ISO format (ISO 8601)", alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, description="The time the tool was last updated in ISO format (ISO 8601)", alias="lastUpdatedAt")
    auth: Optional[AuthConfig] = None
    __properties: ClassVar[List[str]] = ["type", "name", "displayName", "toolId", "displayDescription", "logoUrl", "objectName", "createdBy", "lastUpdatedBy", "createdAt", "lastUpdatedAt", "auth"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RETRIEVAL', 'ACTION']):
            raise ValueError("must be one of enum values ('RETRIEVAL', 'ACTION')")
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
        """Create an instance of ToolMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_updated_by
        if self.last_updated_by:
            _dict['lastUpdatedBy'] = self.last_updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auth
        if self.auth:
            _dict['auth'] = self.auth.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ToolMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "displayName": obj.get("displayName"),
            "toolId": obj.get("toolId"),
            "displayDescription": obj.get("displayDescription"),
            "logoUrl": obj.get("logoUrl"),
            "objectName": obj.get("objectName"),
            "createdBy": PersonObject.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "lastUpdatedBy": PersonObject.from_dict(obj["lastUpdatedBy"]) if obj.get("lastUpdatedBy") is not None else None,
            "createdAt": obj.get("createdAt"),
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "auth": AuthConfig.from_dict(obj["auth"]) if obj.get("auth") is not None else None
        })
        return _obj

