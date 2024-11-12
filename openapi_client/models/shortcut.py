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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.object_permissions import ObjectPermissions
from typing import Optional, Set
from typing_extensions import Self

class Shortcut(BaseModel):
    """
    Shortcut
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The opaque id of the user generated content.")
    input_alias: StrictStr = Field(description="Link text following go/ prefix as entered by the user.", alias="inputAlias")
    destination_url: Optional[StrictStr] = Field(default=None, description="Destination URL for the shortcut.", alias="destinationUrl")
    destination_document_id: Optional[StrictStr] = Field(default=None, description="Glean Document ID for the URL, if known.", alias="destinationDocumentId")
    description: Optional[StrictStr] = Field(default=None, description="A short, plain text blurb to help people understand the intent of the shortcut.")
    unlisted: Optional[StrictBool] = Field(default=None, description="Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only.")
    url_template: Optional[StrictStr] = Field(default=None, description="For variable shortcuts, contains the URL template; note, `destinationUrl` contains default URL.", alias="urlTemplate")
    added_roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of user roles added for the Shortcut.", alias="addedRoles")
    removed_roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of user roles removed for the Shortcut.", alias="removedRoles")
    permissions: Optional[ObjectPermissions] = None
    created_by: Optional[Person] = Field(default=None, alias="createdBy")
    create_time: Optional[datetime] = Field(default=None, description="The time the shortcut was created in ISO format (ISO 8601).", alias="createTime")
    updated_by: Optional[Person] = Field(default=None, alias="updatedBy")
    update_time: Optional[datetime] = Field(default=None, description="The time the shortcut was updated in ISO format (ISO 8601).", alias="updateTime")
    destination_document: Optional[Document] = Field(default=None, alias="destinationDocument")
    intermediate_url: Optional[StrictStr] = Field(default=None, description="The URL from which the user is then redirected to the destination URL. Full replacement for https://go/<inputAlias>.", alias="intermediateUrl")
    view_prefix: Optional[StrictStr] = Field(default=None, description="The part of the shortcut preceding the input alias when used for showing shortcuts to users. Should end with \"/\". e.g. \"go/\" for native shortcuts.", alias="viewPrefix")
    is_external: Optional[StrictBool] = Field(default=None, description="Indicates whether a shortcut is native or external.", alias="isExternal")
    edit_url: Optional[StrictStr] = Field(default=None, description="The URL using which the user can access the edit page of the shortcut.", alias="editUrl")
    alias: Optional[StrictStr] = Field(default=None, description="canonical link text following go/ prefix where hyphen/underscore is removed.")
    title: Optional[StrictStr] = Field(default=None, description="Title for the Go Link")
    roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of user roles for the Go Link.")
    __properties: ClassVar[List[str]] = ["id", "inputAlias", "destinationUrl", "destinationDocumentId", "description", "unlisted", "urlTemplate", "addedRoles", "removedRoles", "permissions", "createdBy", "createTime", "updatedBy", "updateTime", "destinationDocument", "intermediateUrl", "viewPrefix", "isExternal", "editUrl", "alias", "title", "roles"]

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
        """Create an instance of Shortcut from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_document
        if self.destination_document:
            _dict['destinationDocument'] = self.destination_document.to_dict()
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
        """Create an instance of Shortcut from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "inputAlias": obj.get("inputAlias"),
            "destinationUrl": obj.get("destinationUrl"),
            "destinationDocumentId": obj.get("destinationDocumentId"),
            "description": obj.get("description"),
            "unlisted": obj.get("unlisted"),
            "urlTemplate": obj.get("urlTemplate"),
            "addedRoles": [UserRoleSpecification.from_dict(_item) for _item in obj["addedRoles"]] if obj.get("addedRoles") is not None else None,
            "removedRoles": [UserRoleSpecification.from_dict(_item) for _item in obj["removedRoles"]] if obj.get("removedRoles") is not None else None,
            "permissions": ObjectPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "createdBy": Person.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "createTime": obj.get("createTime"),
            "updatedBy": Person.from_dict(obj["updatedBy"]) if obj.get("updatedBy") is not None else None,
            "updateTime": obj.get("updateTime"),
            "destinationDocument": Document.from_dict(obj["destinationDocument"]) if obj.get("destinationDocument") is not None else None,
            "intermediateUrl": obj.get("intermediateUrl"),
            "viewPrefix": obj.get("viewPrefix"),
            "isExternal": obj.get("isExternal"),
            "editUrl": obj.get("editUrl"),
            "alias": obj.get("alias"),
            "title": obj.get("title"),
            "roles": [UserRoleSpecification.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None
        })
        return _obj

from openapi_client.models.document import Document
from openapi_client.models.person import Person
from openapi_client.models.user_role_specification import UserRoleSpecification
# TODO: Rewrite to not use raise_errors
Shortcut.model_rebuild(raise_errors=False)

