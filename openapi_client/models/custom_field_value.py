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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.custom_field_value_hyperlink import CustomFieldValueHyperlink
from openapi_client.models.custom_field_value_str import CustomFieldValueStr
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CUSTOMFIELDVALUE_ONE_OF_SCHEMAS = ["CustomFieldValueHyperlink", "CustomFieldValuePerson", "CustomFieldValueStr"]

class CustomFieldValue(BaseModel):
    """
    CustomFieldValue
    """
    # data type: CustomFieldValueStr
    oneof_schema_1_validator: Optional[CustomFieldValueStr] = None
    # data type: CustomFieldValueHyperlink
    oneof_schema_2_validator: Optional[CustomFieldValueHyperlink] = None
    # data type: CustomFieldValuePerson
    oneof_schema_3_validator: Optional[CustomFieldValuePerson] = None
    actual_instance: Optional[Union[CustomFieldValueHyperlink, CustomFieldValuePerson, CustomFieldValueStr]] = None
    one_of_schemas: Set[str] = { "CustomFieldValueHyperlink", "CustomFieldValuePerson", "CustomFieldValueStr" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = CustomFieldValue.model_construct()
        error_messages = []
        match = 0
        # validate data type: CustomFieldValueStr
        if not isinstance(v, CustomFieldValueStr):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CustomFieldValueStr`")
        else:
            match += 1
        # validate data type: CustomFieldValueHyperlink
        if not isinstance(v, CustomFieldValueHyperlink):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CustomFieldValueHyperlink`")
        else:
            match += 1
        # validate data type: CustomFieldValuePerson
        if not isinstance(v, CustomFieldValuePerson):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CustomFieldValuePerson`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CustomFieldValue with oneOf schemas: CustomFieldValueHyperlink, CustomFieldValuePerson, CustomFieldValueStr. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CustomFieldValue with oneOf schemas: CustomFieldValueHyperlink, CustomFieldValuePerson, CustomFieldValueStr. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into CustomFieldValueStr
        try:
            instance.actual_instance = CustomFieldValueStr.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CustomFieldValueHyperlink
        try:
            instance.actual_instance = CustomFieldValueHyperlink.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CustomFieldValuePerson
        try:
            instance.actual_instance = CustomFieldValuePerson.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CustomFieldValue with oneOf schemas: CustomFieldValueHyperlink, CustomFieldValuePerson, CustomFieldValueStr. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CustomFieldValue with oneOf schemas: CustomFieldValueHyperlink, CustomFieldValuePerson, CustomFieldValueStr. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CustomFieldValueHyperlink, CustomFieldValuePerson, CustomFieldValueStr]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

from openapi_client.models.custom_field_value_person import CustomFieldValuePerson
# TODO: Rewrite to not use raise_errors
CustomFieldValue.model_rebuild(raise_errors=False)

