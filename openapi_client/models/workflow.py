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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.object_permissions import ObjectPermissions
from openapi_client.models.person import Person
from openapi_client.models.user_role_specification import UserRoleSpecification
from openapi_client.models.workflow_input_field import WorkflowInputField
from openapi_client.models.workflow_schema import WorkflowSchema
from openapi_client.models.workflow_step import WorkflowStep
from typing import Optional, Set
from typing_extensions import Self

class Workflow(BaseModel):
    """
    Workflow
    """ # noqa: E501
    permissions: Optional[ObjectPermissions] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of the workflow.")
    var_schema: Optional[WorkflowSchema] = Field(default=None, alias="schema")
    application_id: Optional[StrictStr] = Field(default=None, description="The Application Id the workflow should be created under. Empty for default assistant.", alias="applicationId")
    added_roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of added user roles for the Workflow.", alias="addedRoles")
    removed_roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of removed user roles for the Workflow.", alias="removedRoles")
    fields: Optional[List[WorkflowInputField]] = Field(default=None, description="Use schema instead.")
    steps: Optional[List[WorkflowStep]] = Field(default=None, description="Use schema instead.")
    author: Optional[Person] = None
    create_timestamp: Optional[StrictInt] = Field(default=None, description="Server Unix timestamp of the creation time.", alias="createTimestamp")
    last_update_timestamp: Optional[StrictInt] = Field(default=None, description="Server Unix timestamp of the last update time.", alias="lastUpdateTimestamp")
    last_updated_by: Optional[Person] = Field(default=None, alias="lastUpdatedBy")
    roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of roles for this prompt template explicitly granted.")
    id: Optional[StrictStr] = Field(default=None, description="The ID of the workflow.")
    __properties: ClassVar[List[str]] = ["permissions", "name", "schema", "applicationId", "addedRoles", "removedRoles", "fields", "steps", "author", "createTimestamp", "lastUpdateTimestamp", "lastUpdatedBy", "roles", "id"]

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
        """Create an instance of Workflow from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in added_roles (list)
        _items = []
        if self.added_roles:
            for _item_added_roles in self.added_roles:
                if _item_added_roles:
                    _items.append(_item_added_roles.to_dict())
            _dict['addedRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in removed_roles (list)
        _items = []
        if self.removed_roles:
            for _item_removed_roles in self.removed_roles:
                if _item_removed_roles:
                    _items.append(_item_removed_roles.to_dict())
            _dict['removedRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_updated_by
        if self.last_updated_by:
            _dict['lastUpdatedBy'] = self.last_updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item_roles in self.roles:
                if _item_roles:
                    _items.append(_item_roles.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Workflow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "permissions": ObjectPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "name": obj.get("name"),
            "schema": WorkflowSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "applicationId": obj.get("applicationId"),
            "addedRoles": [UserRoleSpecification.from_dict(_item) for _item in obj["addedRoles"]] if obj.get("addedRoles") is not None else None,
            "removedRoles": [UserRoleSpecification.from_dict(_item) for _item in obj["removedRoles"]] if obj.get("removedRoles") is not None else None,
            "fields": [WorkflowInputField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "steps": [WorkflowStep.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "author": Person.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "createTimestamp": obj.get("createTimestamp"),
            "lastUpdateTimestamp": obj.get("lastUpdateTimestamp"),
            "lastUpdatedBy": Person.from_dict(obj["lastUpdatedBy"]) if obj.get("lastUpdatedBy") is not None else None,
            "roles": [UserRoleSpecification.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "id": obj.get("id")
        })
        return _obj


