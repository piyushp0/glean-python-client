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
from openapi_client.models.operator_scope import OperatorScope
from typing import Optional, Set
from typing_extensions import Self

class OperatorMetadata(BaseModel):
    """
    OperatorMetadata
    """ # noqa: E501
    name: StrictStr
    is_custom: Optional[StrictBool] = Field(default=None, description="Whether this operator is supported by default or something that was created within a workplace app (e.g. custom jira field).", alias="isCustom")
    operator_type: Optional[StrictStr] = Field(default=None, alias="operatorType")
    help_text: Optional[StrictStr] = Field(default=None, alias="helpText")
    scopes: Optional[List[OperatorScope]] = None
    value: Optional[StrictStr] = Field(default=None, description="Raw/canonical value of the operator. Only applies when result is an operator value.")
    display_value: Optional[StrictStr] = Field(default=None, description="Human readable value of the operator that can be shown to the user. Only applies when result is an operator value.", alias="displayValue")
    __properties: ClassVar[List[str]] = ["name", "isCustom", "operatorType", "helpText", "scopes", "value", "displayValue"]

    @field_validator('operator_type')
    def operator_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TEXT', 'DOUBLE', 'DATE', 'USER']):
            raise ValueError("must be one of enum values ('TEXT', 'DOUBLE', 'DATE', 'USER')")
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
        """Create an instance of OperatorMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in scopes (list)
        _items = []
        if self.scopes:
            for _item in self.scopes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scopes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OperatorMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "isCustom": obj.get("isCustom"),
            "operatorType": obj.get("operatorType"),
            "helpText": obj.get("helpText"),
            "scopes": [OperatorScope.from_dict(_item) for _item in obj["scopes"]] if obj.get("scopes") is not None else None,
            "value": obj.get("value"),
            "displayValue": obj.get("displayValue")
        })
        return _obj


