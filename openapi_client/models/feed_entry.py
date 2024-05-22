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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.announcement import Announcement
from openapi_client.models.app_result import AppResult
from openapi_client.models.calendar_event import CalendarEvent
from openapi_client.models.client_action import ClientAction
from openapi_client.models.collection import Collection
from openapi_client.models.collection_item import CollectionItem
from openapi_client.models.count_info import CountInfo
from openapi_client.models.document import Document
from openapi_client.models.feed_entry_ui_config import FeedEntryUiConfig
from openapi_client.models.person import Person
from openapi_client.models.thumbnail import Thumbnail
from openapi_client.models.user_activity import UserActivity
from typing import Optional, Set
from typing_extensions import Self

class FeedEntry(BaseModel):
    """
    FeedEntry
    """ # noqa: E501
    entry_id: Optional[StrictStr] = Field(default=None, description="optional ID associated with a single feed entry (displayable_list_id)", alias="entryId")
    title: StrictStr = Field(description="Title for the result. Can be document title, event title and so on.")
    thumbnail: Optional[Thumbnail] = None
    created_by: Optional[Person] = Field(default=None, alias="createdBy")
    ui_config: Optional[FeedEntryUiConfig] = Field(default=None, alias="uiConfig")
    snippet: Optional[StrictStr] = Field(default=None, description="A textual snippet representing this entry, dependent on type. For example, for USER_MENTION, it may contain the sentence in which the mention occurred.")
    justification_type: Optional[StrictStr] = Field(default=None, description="Type of the justification.", alias="justificationType")
    justification: Optional[StrictStr] = Field(default=None, description="Server side generated justification string if server provides one.")
    tracking_token: Optional[StrictStr] = Field(default=None, description="An opaque token that represents this particular feed entry in this particular response. To be used for /feedback reporting.", alias="trackingToken")
    document: Optional[Document] = None
    event: Optional[CalendarEvent] = None
    announcement: Optional[Announcement] = None
    collection: Optional[Collection] = None
    collection_item: Optional[CollectionItem] = Field(default=None, alias="collectionItem")
    person: Optional[Person] = None
    app: Optional[AppResult] = None
    activities: Optional[List[UserActivity]] = Field(default=None, description="List of activity where each activity has user, action, timestamp.")
    document_visitor_count: Optional[CountInfo] = Field(default=None, alias="documentVisitorCount")
    view_url: Optional[StrictStr] = Field(default=None, description="View URL for the entry if based on links that are not documents in Glean.", alias="viewUrl")
    additional_client_actions: Optional[List[ClientAction]] = Field(default=None, description="List of client actions suggested by the backend to be included for entry.", alias="additionalClientActions")
    __properties: ClassVar[List[str]] = ["entryId", "title", "thumbnail", "createdBy", "uiConfig", "snippet", "justificationType", "justification", "trackingToken", "document", "event", "announcement", "collection", "collectionItem", "person", "app", "activities", "documentVisitorCount", "viewUrl", "additionalClientActions"]

    @field_validator('justification_type')
    def justification_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['FREQUENTLY_ACCESSED', 'RECENTLY_ACCESSED', 'TRENDING_DOCUMENT', 'VERIFICATION_REMINDER', 'SUGGESTED_DOCUMENT', 'EMPTY_STATE_SUGGESTION', 'FRECENCY_SCORED', 'SERVER_GENERATED', 'USE_CASE', 'UPDATE_SINCE_LAST_VIEW', 'RECENTLY_STARTED', 'EVENT', 'USER_MENTION', 'ANNOUNCEMENT', 'EXTERNAL_ANNOUNCEMENT', 'POPULARITY_BASED_TRENDING', 'COMPANY_RESOURCE', 'EVENT_DOCUMENT_FROM_CONTENT', 'EVENT_DOCUMENT_FROM_SEARCH', 'VISIT_AFFINITY_SCORED', 'SUGGESTED_APP', 'SUGGESTED_PERSON', 'ACTIVITY_HIGHLIGHT', 'SAVED_SEARCH', 'SUGGESTED_CHANNEL', 'PEOPLE_CELEBRATIONS', 'SOCIAL_LINK', 'ZERO_STATE_CHAT_SUGGESTION', 'ZERO_STATE_CHAT_TOOL_SUGGESTION']):
            raise ValueError("must be one of enum values ('FREQUENTLY_ACCESSED', 'RECENTLY_ACCESSED', 'TRENDING_DOCUMENT', 'VERIFICATION_REMINDER', 'SUGGESTED_DOCUMENT', 'EMPTY_STATE_SUGGESTION', 'FRECENCY_SCORED', 'SERVER_GENERATED', 'USE_CASE', 'UPDATE_SINCE_LAST_VIEW', 'RECENTLY_STARTED', 'EVENT', 'USER_MENTION', 'ANNOUNCEMENT', 'EXTERNAL_ANNOUNCEMENT', 'POPULARITY_BASED_TRENDING', 'COMPANY_RESOURCE', 'EVENT_DOCUMENT_FROM_CONTENT', 'EVENT_DOCUMENT_FROM_SEARCH', 'VISIT_AFFINITY_SCORED', 'SUGGESTED_APP', 'SUGGESTED_PERSON', 'ACTIVITY_HIGHLIGHT', 'SAVED_SEARCH', 'SUGGESTED_CHANNEL', 'PEOPLE_CELEBRATIONS', 'SOCIAL_LINK', 'ZERO_STATE_CHAT_SUGGESTION', 'ZERO_STATE_CHAT_TOOL_SUGGESTION')")
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
        """Create an instance of FeedEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of thumbnail
        if self.thumbnail:
            _dict['thumbnail'] = self.thumbnail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ui_config
        if self.ui_config:
            _dict['uiConfig'] = self.ui_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict['document'] = self.document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of announcement
        if self.announcement:
            _dict['announcement'] = self.announcement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of collection
        if self.collection:
            _dict['collection'] = self.collection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of collection_item
        if self.collection_item:
            _dict['collectionItem'] = self.collection_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app
        if self.app:
            _dict['app'] = self.app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in activities (list)
        _items = []
        if self.activities:
            for _item in self.activities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['activities'] = _items
        # override the default output from pydantic by calling `to_dict()` of document_visitor_count
        if self.document_visitor_count:
            _dict['documentVisitorCount'] = self.document_visitor_count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_client_actions (list)
        _items = []
        if self.additional_client_actions:
            for _item in self.additional_client_actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalClientActions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FeedEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entryId": obj.get("entryId"),
            "title": obj.get("title"),
            "thumbnail": Thumbnail.from_dict(obj["thumbnail"]) if obj.get("thumbnail") is not None else None,
            "createdBy": Person.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "uiConfig": FeedEntryUiConfig.from_dict(obj["uiConfig"]) if obj.get("uiConfig") is not None else None,
            "snippet": obj.get("snippet"),
            "justificationType": obj.get("justificationType"),
            "justification": obj.get("justification"),
            "trackingToken": obj.get("trackingToken"),
            "document": Document.from_dict(obj["document"]) if obj.get("document") is not None else None,
            "event": CalendarEvent.from_dict(obj["event"]) if obj.get("event") is not None else None,
            "announcement": Announcement.from_dict(obj["announcement"]) if obj.get("announcement") is not None else None,
            "collection": Collection.from_dict(obj["collection"]) if obj.get("collection") is not None else None,
            "collectionItem": CollectionItem.from_dict(obj["collectionItem"]) if obj.get("collectionItem") is not None else None,
            "person": Person.from_dict(obj["person"]) if obj.get("person") is not None else None,
            "app": AppResult.from_dict(obj["app"]) if obj.get("app") is not None else None,
            "activities": [UserActivity.from_dict(_item) for _item in obj["activities"]] if obj.get("activities") is not None else None,
            "documentVisitorCount": CountInfo.from_dict(obj["documentVisitorCount"]) if obj.get("documentVisitorCount") is not None else None,
            "viewUrl": obj.get("viewUrl"),
            "additionalClientActions": [ClientAction.from_dict(_item) for _item in obj["additionalClientActions"]] if obj.get("additionalClientActions") is not None else None
        })
        return _obj

