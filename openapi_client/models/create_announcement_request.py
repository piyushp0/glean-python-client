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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.facet_filter import FacetFilter
from openapi_client.models.structured_text import StructuredText
from openapi_client.models.thumbnail import Thumbnail
from typing import Optional, Set
from typing_extensions import Self

class CreateAnnouncementRequest(BaseModel):
    """
    CreateAnnouncementRequest
    """ # noqa: E501
    start_time: datetime = Field(description="The date and time at which the announcement becomes active.", alias="startTime")
    end_time: datetime = Field(description="The date and time at which the announcement expires.", alias="endTime")
    title: StrictStr = Field(description="The headline of the announcement.")
    body: Optional[StructuredText] = None
    emoji: Optional[StrictStr] = Field(default=None, description="An emoji used to indicate the nature of the announcement.")
    thumbnail: Optional[Thumbnail] = None
    banner: Optional[Thumbnail] = None
    audience_filters: Optional[List[FacetFilter]] = Field(default=None, description="Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search.", alias="audienceFilters")
    source_document_id: Optional[StrictStr] = Field(default=None, description="The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread).", alias="sourceDocumentId")
    hide_attribution: Optional[StrictBool] = Field(default=None, description="Whether or not to hide an author attribution.", alias="hideAttribution")
    channel: Optional[StrictStr] = Field(default=None, description="This determines whether this is a Social Feed post or a regular announcement.")
    post_type: Optional[StrictStr] = Field(default=None, description="This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site.", alias="postType")
    is_prioritized: Optional[StrictBool] = Field(default=None, description="Used by the Social Feed to pin posts to the front of the feed.", alias="isPrioritized")
    view_url: Optional[StrictStr] = Field(default=None, description="URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel=\"SOCIAL_FEED\".", alias="viewUrl")
    __properties: ClassVar[List[str]] = ["startTime", "endTime", "title", "body", "emoji", "thumbnail", "banner", "audienceFilters", "sourceDocumentId", "hideAttribution", "channel", "postType", "isPrioritized", "viewUrl"]

    @field_validator('channel')
    def channel_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MAIN', 'SOCIAL_FEED']):
            raise ValueError("must be one of enum values ('MAIN', 'SOCIAL_FEED')")
        return value

    @field_validator('post_type')
    def post_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TEXT', 'LINK']):
            raise ValueError("must be one of enum values ('TEXT', 'LINK')")
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
        """Create an instance of CreateAnnouncementRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of body
        if self.body:
            _dict['body'] = self.body.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thumbnail
        if self.thumbnail:
            _dict['thumbnail'] = self.thumbnail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of banner
        if self.banner:
            _dict['banner'] = self.banner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in audience_filters (list)
        _items = []
        if self.audience_filters:
            for _item_audience_filters in self.audience_filters:
                if _item_audience_filters:
                    _items.append(_item_audience_filters.to_dict())
            _dict['audienceFilters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateAnnouncementRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "title": obj.get("title"),
            "body": StructuredText.from_dict(obj["body"]) if obj.get("body") is not None else None,
            "emoji": obj.get("emoji"),
            "thumbnail": Thumbnail.from_dict(obj["thumbnail"]) if obj.get("thumbnail") is not None else None,
            "banner": Thumbnail.from_dict(obj["banner"]) if obj.get("banner") is not None else None,
            "audienceFilters": [FacetFilter.from_dict(_item) for _item in obj["audienceFilters"]] if obj.get("audienceFilters") is not None else None,
            "sourceDocumentId": obj.get("sourceDocumentId"),
            "hideAttribution": obj.get("hideAttribution"),
            "channel": obj.get("channel"),
            "postType": obj.get("postType"),
            "isPrioritized": obj.get("isPrioritized"),
            "viewUrl": obj.get("viewUrl")
        })
        return _obj


