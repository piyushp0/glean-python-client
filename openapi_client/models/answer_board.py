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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.facet_filter import FacetFilter
from openapi_client.models.object_permissions import ObjectPermissions
from typing import Optional, Set
from typing_extensions import Self

class AnswerBoard(BaseModel):
    """
    AnswerBoard
    """ # noqa: E501
    name: StrictStr = Field(description="The unique name of the Collection.")
    description: StrictStr = Field(description="A brief summary of the Collection's contents.")
    added_roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of added user roles for the Collection.", alias="addedRoles")
    removed_roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of removed user roles for the Collection.", alias="removedRoles")
    audience_filters: Optional[List[FacetFilter]] = Field(default=None, description="Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search.", alias="audienceFilters")
    permissions: Optional[ObjectPermissions] = None
    id: StrictInt = Field(description="The unique ID of the Answer Board.")
    create_time: Optional[datetime] = Field(default=None, alias="createTime")
    update_time: Optional[datetime] = Field(default=None, alias="updateTime")
    creator: Optional[Person] = None
    updated_by: Optional[Person] = Field(default=None, alias="updatedBy")
    item_count: Optional[StrictInt] = Field(default=None, description="The number of items currently in the Answer Board. Separated from the actual items so we can grab the count without items.", alias="itemCount")
    roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of user roles for the Answer Board.")
    __properties: ClassVar[List[str]] = ["name", "description", "addedRoles", "removedRoles", "audienceFilters", "permissions", "id", "createTime", "updateTime", "creator", "updatedBy", "itemCount", "roles"]

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
        """Create an instance of AnswerBoard from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in added_roles (list)
        _items = []
        if self.added_roles:
            for _item in self.added_roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addedRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in removed_roles (list)
        _items = []
        if self.removed_roles:
            for _item in self.removed_roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['removedRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in audience_filters (list)
        _items = []
        if self.audience_filters:
            for _item in self.audience_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['audienceFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnswerBoard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "addedRoles": [UserRoleSpecification.from_dict(_item) for _item in obj["addedRoles"]] if obj.get("addedRoles") is not None else None,
            "removedRoles": [UserRoleSpecification.from_dict(_item) for _item in obj["removedRoles"]] if obj.get("removedRoles") is not None else None,
            "audienceFilters": [FacetFilter.from_dict(_item) for _item in obj["audienceFilters"]] if obj.get("audienceFilters") is not None else None,
            "permissions": ObjectPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "id": obj.get("id"),
            "createTime": obj.get("createTime"),
            "updateTime": obj.get("updateTime"),
            "creator": Person.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "updatedBy": Person.from_dict(obj["updatedBy"]) if obj.get("updatedBy") is not None else None,
            "itemCount": obj.get("itemCount"),
            "roles": [UserRoleSpecification.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None
        })
        return _obj

from openapi_client.models.person import Person
from openapi_client.models.user_role_specification import UserRoleSpecification
# TODO: Rewrite to not use raise_errors
AnswerBoard.model_rebuild(raise_errors=False)

