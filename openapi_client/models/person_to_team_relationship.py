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
from typing import Optional, Set
from typing_extensions import Self

class PersonToTeamRelationship(BaseModel):
    """
    Metadata about the relationship of a person to a team.
    """ # noqa: E501
    person: Person
    relationship: Optional[StrictStr] = Field(default='MEMBER', description="The team member's relationship to the team. This defaults to MEMBER if not set.")
    custom_relationship_str: Optional[StrictStr] = Field(default=None, description="Displayed name for the relationship if relationship is set to `OTHER`.", alias="customRelationshipStr")
    join_date: Optional[datetime] = Field(default=None, description="The team member's start date", alias="joinDate")
    __properties: ClassVar[List[str]] = ["person", "relationship", "customRelationshipStr", "joinDate"]

    @field_validator('relationship')
    def relationship_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MEMBER', 'MANAGER', 'LEAD', 'POINT_OF_CONTACT', 'OTHER']):
            raise ValueError("must be one of enum values ('MEMBER', 'MANAGER', 'LEAD', 'POINT_OF_CONTACT', 'OTHER')")
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
        """Create an instance of PersonToTeamRelationship from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PersonToTeamRelationship from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "person": Person.from_dict(obj["person"]) if obj.get("person") is not None else None,
            "relationship": obj.get("relationship") if obj.get("relationship") is not None else 'MEMBER',
            "customRelationshipStr": obj.get("customRelationshipStr"),
            "joinDate": obj.get("joinDate")
        })
        return _obj

from openapi_client.models.person import Person
# TODO: Rewrite to not use raise_errors
PersonToTeamRelationship.model_rebuild(raise_errors=False)
