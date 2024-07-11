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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.count_info import CountInfo
from openapi_client.models.custom_data_value import CustomDataValue
from openapi_client.models.document_visibility import DocumentVisibility
from openapi_client.models.index_status import IndexStatus
from openapi_client.models.object_permissions import ObjectPermissions
from openapi_client.models.thumbnail import Thumbnail
from openapi_client.models.viewer_info import ViewerInfo
from typing import Optional, Set
from typing_extensions import Self

class DocumentMetadata(BaseModel):
    """
    DocumentMetadata
    """ # noqa: E501
    datasource: Optional[StrictStr] = None
    datasource_instance: Optional[StrictStr] = Field(default=None, description="The datasource instance from which the document was extracted.", alias="datasourceInstance")
    object_type: Optional[StrictStr] = Field(default=None, description="The type of the result. Interpretation is specific to each datasource. (e.g. for Jira issues, this is the issue type such as Bug or Feature Request).", alias="objectType")
    container: Optional[StrictStr] = Field(default=None, description="The name of the container (higher level parent, not direct parent) of the result. Interpretation is specific to each datasource (e.g. Channels for Slack, Project for Jira). cf. parentId")
    container_id: Optional[StrictStr] = Field(default=None, description="The Glean Document ID of the container. Uniquely identifies the container.", alias="containerId")
    super_container_id: Optional[StrictStr] = Field(default=None, description="The Glean Document ID of the super container. Super container represents a broader abstraction that contains many containers. For example, whereas container might refer to a folder, super container would refer to a drive.", alias="superContainerId")
    parent_id: Optional[StrictStr] = Field(default=None, description="The id of the direct parent of the result. Interpretation is specific to each datasource (e.g. parent issue for Jira). cf. container", alias="parentId")
    mime_type: Optional[StrictStr] = Field(default=None, alias="mimeType")
    document_id: Optional[StrictStr] = Field(default=None, description="The index-wide unique identifier.", alias="documentId")
    logging_id: Optional[StrictStr] = Field(default=None, description="A unique identifier used to represent the document in any logging or feedback requests in place of documentId.", alias="loggingId")
    document_id_hash: Optional[StrictStr] = Field(default=None, description="Hash of the Glean Document ID.", alias="documentIdHash")
    create_time: Optional[datetime] = Field(default=None, alias="createTime")
    update_time: Optional[datetime] = Field(default=None, alias="updateTime")
    author: Optional[Person] = None
    owner: Optional[Person] = None
    visibility: Optional[DocumentVisibility] = None
    components: Optional[List[StrictStr]] = Field(default=None, description="A list of components this result is associated with. Interpretation is specific to each datasource. (e.g. for Jira issues, these are [components](https://confluence.atlassian.com/jirasoftwarecloud/organizing-work-with-components-764478279.html).)")
    status: Optional[StrictStr] = Field(default=None, description="The status or disposition of the result. Interpretation is specific to each datasource. (e.g. for Jira issues, this is the issue status such as Done, In Progress or Will Not Fix).")
    status_category: Optional[StrictStr] = Field(default=None, description="The status category of the result. Meant to be more general than status. Interpretation is specific to each datasource.", alias="statusCategory")
    pins: Optional[List[PinDocument]] = Field(default=None, description="A list of stars associated with this result.  \"Pin\" is an older name.")
    priority: Optional[StrictStr] = Field(default=None, description="The document priority. Interpretation is datasource specific.")
    assigned_to: Optional[Person] = Field(default=None, alias="assignedTo")
    updated_by: Optional[Person] = Field(default=None, alias="updatedBy")
    labels: Optional[List[StrictStr]] = Field(default=None, description="A list of tags for the document. Interpretation is datasource specific.")
    collections: Optional[List[Collection]] = Field(default=None, description="A list of collections that the document belongs to.")
    datasource_id: Optional[StrictStr] = Field(default=None, description="The user-visible datasource specific id (e.g. Salesforce case number for example, GitHub PR number).", alias="datasourceId")
    interactions: Optional[DocumentInteractions] = None
    verification: Optional[Verification] = None
    viewer_info: Optional[ViewerInfo] = Field(default=None, alias="viewerInfo")
    permissions: Optional[ObjectPermissions] = None
    visit_count: Optional[CountInfo] = Field(default=None, alias="visitCount")
    shortcuts: Optional[List[Shortcut]] = Field(default=None, description="A list of shortcuts of which destination URL is for the document.")
    path: Optional[StrictStr] = Field(default=None, description="For file datasources like onedrive/github etc this has the path to the file")
    custom_data: Optional[Dict[str, CustomDataValue]] = Field(default=None, description="Custom fields specific to individual datasources", alias="customData")
    document_category: Optional[StrictStr] = Field(default=None, description="The document's document_category(.proto).", alias="documentCategory")
    contact_person: Optional[Person] = Field(default=None, alias="contactPerson")
    thumbnail: Optional[Thumbnail] = None
    index_status: Optional[IndexStatus] = Field(default=None, alias="indexStatus")
    ancestors: Optional[List[Document]] = Field(default=None, description="A list of documents that are ancestors of this document in the hierarchy of the document's datasource, for example parent folders or containers. Ancestors can be of different types and some may not be indexed. Higher level ancestors appear earlier in the list.")
    __properties: ClassVar[List[str]] = ["datasource", "datasourceInstance", "objectType", "container", "containerId", "superContainerId", "parentId", "mimeType", "documentId", "loggingId", "documentIdHash", "createTime", "updateTime", "author", "owner", "visibility", "components", "status", "statusCategory", "pins", "priority", "assignedTo", "updatedBy", "labels", "collections", "datasourceId", "interactions", "verification", "viewerInfo", "permissions", "visitCount", "shortcuts", "path", "customData", "documentCategory", "contactPerson", "thumbnail", "indexStatus", "ancestors"]

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
        """Create an instance of DocumentMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pins (list)
        _items = []
        if self.pins:
            for _item in self.pins:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pins'] = _items
        # override the default output from pydantic by calling `to_dict()` of assigned_to
        if self.assigned_to:
            _dict['assignedTo'] = self.assigned_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in collections (list)
        _items = []
        if self.collections:
            for _item in self.collections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['collections'] = _items
        # override the default output from pydantic by calling `to_dict()` of interactions
        if self.interactions:
            _dict['interactions'] = self.interactions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verification
        if self.verification:
            _dict['verification'] = self.verification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of viewer_info
        if self.viewer_info:
            _dict['viewerInfo'] = self.viewer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of visit_count
        if self.visit_count:
            _dict['visitCount'] = self.visit_count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shortcuts (list)
        _items = []
        if self.shortcuts:
            for _item in self.shortcuts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shortcuts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in custom_data (dict)
        _field_dict = {}
        if self.custom_data:
            for _key in self.custom_data:
                if self.custom_data[_key]:
                    _field_dict[_key] = self.custom_data[_key].to_dict()
            _dict['customData'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of contact_person
        if self.contact_person:
            _dict['contactPerson'] = self.contact_person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thumbnail
        if self.thumbnail:
            _dict['thumbnail'] = self.thumbnail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of index_status
        if self.index_status:
            _dict['indexStatus'] = self.index_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ancestors (list)
        _items = []
        if self.ancestors:
            for _item in self.ancestors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ancestors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "datasource": obj.get("datasource"),
            "datasourceInstance": obj.get("datasourceInstance"),
            "objectType": obj.get("objectType"),
            "container": obj.get("container"),
            "containerId": obj.get("containerId"),
            "superContainerId": obj.get("superContainerId"),
            "parentId": obj.get("parentId"),
            "mimeType": obj.get("mimeType"),
            "documentId": obj.get("documentId"),
            "loggingId": obj.get("loggingId"),
            "documentIdHash": obj.get("documentIdHash"),
            "createTime": obj.get("createTime"),
            "updateTime": obj.get("updateTime"),
            "author": Person.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "owner": Person.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "visibility": obj.get("visibility"),
            "components": obj.get("components"),
            "status": obj.get("status"),
            "statusCategory": obj.get("statusCategory"),
            "pins": [PinDocument.from_dict(_item) for _item in obj["pins"]] if obj.get("pins") is not None else None,
            "priority": obj.get("priority"),
            "assignedTo": Person.from_dict(obj["assignedTo"]) if obj.get("assignedTo") is not None else None,
            "updatedBy": Person.from_dict(obj["updatedBy"]) if obj.get("updatedBy") is not None else None,
            "labels": obj.get("labels"),
            "collections": [Collection.from_dict(_item) for _item in obj["collections"]] if obj.get("collections") is not None else None,
            "datasourceId": obj.get("datasourceId"),
            "interactions": DocumentInteractions.from_dict(obj["interactions"]) if obj.get("interactions") is not None else None,
            "verification": Verification.from_dict(obj["verification"]) if obj.get("verification") is not None else None,
            "viewerInfo": ViewerInfo.from_dict(obj["viewerInfo"]) if obj.get("viewerInfo") is not None else None,
            "permissions": ObjectPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "visitCount": CountInfo.from_dict(obj["visitCount"]) if obj.get("visitCount") is not None else None,
            "shortcuts": [Shortcut.from_dict(_item) for _item in obj["shortcuts"]] if obj.get("shortcuts") is not None else None,
            "path": obj.get("path"),
            "customData": dict(
                (_k, CustomDataValue.from_dict(_v))
                for _k, _v in obj["customData"].items()
            )
            if obj.get("customData") is not None
            else None,
            "documentCategory": obj.get("documentCategory"),
            "contactPerson": Person.from_dict(obj["contactPerson"]) if obj.get("contactPerson") is not None else None,
            "thumbnail": Thumbnail.from_dict(obj["thumbnail"]) if obj.get("thumbnail") is not None else None,
            "indexStatus": IndexStatus.from_dict(obj["indexStatus"]) if obj.get("indexStatus") is not None else None,
            "ancestors": [Document.from_dict(_item) for _item in obj["ancestors"]] if obj.get("ancestors") is not None else None
        })
        return _obj

from openapi_client.models.collection import Collection
from openapi_client.models.document import Document
from openapi_client.models.document_interactions import DocumentInteractions
from openapi_client.models.person import Person
from openapi_client.models.pin_document import PinDocument
from openapi_client.models.shortcut import Shortcut
from openapi_client.models.verification import Verification
# TODO: Rewrite to not use raise_errors
DocumentMetadata.model_rebuild(raise_errors=False)

