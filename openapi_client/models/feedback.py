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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.feedback_debug_info import FeedbackDebugInfo
from openapi_client.models.manual_feedback_info import ManualFeedbackInfo
from openapi_client.models.seen_feedback_info import SeenFeedbackInfo
from openapi_client.models.session_info import SessionInfo
from openapi_client.models.user import User
from openapi_client.models.user_view_info import UserViewInfo
from typing import Optional, Set
from typing_extensions import Self

class Feedback(BaseModel):
    """
    Feedback
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Universally unique identifier of the event. To allow for reliable retransmission, only the earliest received event of a given UUID is considered valid by the server and subsequent are ignored.")
    category: Optional[StrictStr] = Field(default=None, description="The feature category to which the feedback applies. These should be broad product areas such as Announcements, Answers, Search, etc. rather than specific components or UI treatments within those areas.")
    tracking_tokens: List[StrictStr] = Field(description="A list of server-generated trackingTokens to which this event applies.", alias="trackingTokens")
    event: StrictStr = Field(description="The action the user took within a Glean client with respect to the object referred to by the given `trackingToken`.")
    position: Optional[StrictInt] = Field(default=None, description="Position of the element in the case that the client controls order (such as feed and autocomplete).")
    payload: Optional[StrictStr] = Field(default=None, description="For type MANUAL_FEEDBACK, contains string of user feedback. For autocomplete, partial query string. For feed, string of user feedback in addition to manual feedback signals extracted from all suggested content.")
    session_info: Optional[SessionInfo] = Field(default=None, alias="sessionInfo")
    timestamp: Optional[datetime] = Field(default=None, description="The ISO 8601 timestamp when the event occured.")
    user: Optional[User] = None
    pathname: Optional[StrictStr] = Field(default=None, description="The path the client was at when the feedback event triggered.")
    channels: Optional[List[StrictStr]] = Field(default=None, description="Where the feedback will be sent, e.g. to Glean, the user's company, or both. If no channels are specified, feedback will go only to Glean.")
    url: Optional[StrictStr] = Field(default=None, description="The URL the client was at when the feedback event triggered.")
    ui_element: Optional[StrictStr] = Field(default=None, description="The UI element associated with the event, if any.", alias="uiElement")
    manual_feedback_info: Optional[ManualFeedbackInfo] = Field(default=None, alias="manualFeedbackInfo")
    seen_feedback_info: Optional[SeenFeedbackInfo] = Field(default=None, alias="seenFeedbackInfo")
    user_view_info: Optional[UserViewInfo] = Field(default=None, alias="userViewInfo")
    debug_info: Optional[FeedbackDebugInfo] = Field(default=None, alias="debugInfo")
    application_id: Optional[StrictStr] = Field(default=None, description="The application ID of the client that sent the feedback event.", alias="applicationId")
    __properties: ClassVar[List[str]] = ["id", "category", "trackingTokens", "event", "position", "payload", "sessionInfo", "timestamp", "user", "pathname", "channels", "url", "uiElement", "manualFeedbackInfo", "seenFeedbackInfo", "userViewInfo", "debugInfo", "applicationId"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ANNOUNCEMENT', 'AUTOCOMPLETE', 'COLLECTIONS', 'FEED', 'SEARCH', 'CHAT', 'NTP', 'SUMMARY']):
            raise ValueError("must be one of enum values ('ANNOUNCEMENT', 'AUTOCOMPLETE', 'COLLECTIONS', 'FEED', 'SEARCH', 'CHAT', 'NTP', 'SUMMARY')")
        return value

    @field_validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CLICK', 'CONTAINER_CLICK', 'COPY_LINK', 'CREATE', 'DISMISS', 'DOWNVOTE', 'EMAIL', 'FIRST_TOKEN', 'FOCUS_IN', 'LAST_TOKEN', 'MANUAL_FEEDBACK', 'MARK_AS_READ', 'MESSAGE', 'MIDDLE_CLICK', 'PAGE_BLUR', 'PAGE_FOCUS', 'PAGE_LEAVE', 'PREVIEW', 'RELATED_CLICK', 'RIGHT_CLICK', 'SECTION_CLICK', 'SEEN', 'SHARE', 'SHOW_MORE', 'UPVOTE', 'VIEW', 'VISIBLE']):
            raise ValueError("must be one of enum values ('CLICK', 'CONTAINER_CLICK', 'COPY_LINK', 'CREATE', 'DISMISS', 'DOWNVOTE', 'EMAIL', 'FIRST_TOKEN', 'FOCUS_IN', 'LAST_TOKEN', 'MANUAL_FEEDBACK', 'MARK_AS_READ', 'MESSAGE', 'MIDDLE_CLICK', 'PAGE_BLUR', 'PAGE_FOCUS', 'PAGE_LEAVE', 'PREVIEW', 'RELATED_CLICK', 'RIGHT_CLICK', 'SECTION_CLICK', 'SEEN', 'SHARE', 'SHOW_MORE', 'UPVOTE', 'VIEW', 'VISIBLE')")
        return value

    @field_validator('channels')
    def channels_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['COMPANY', 'GLEAN']):
                raise ValueError("each list item must be one of ('COMPANY', 'GLEAN')")
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
        """Create an instance of Feedback from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of session_info
        if self.session_info:
            _dict['sessionInfo'] = self.session_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manual_feedback_info
        if self.manual_feedback_info:
            _dict['manualFeedbackInfo'] = self.manual_feedback_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seen_feedback_info
        if self.seen_feedback_info:
            _dict['seenFeedbackInfo'] = self.seen_feedback_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_view_info
        if self.user_view_info:
            _dict['userViewInfo'] = self.user_view_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of debug_info
        if self.debug_info:
            _dict['debugInfo'] = self.debug_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Feedback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "category": obj.get("category"),
            "trackingTokens": obj.get("trackingTokens"),
            "event": obj.get("event"),
            "position": obj.get("position"),
            "payload": obj.get("payload"),
            "sessionInfo": SessionInfo.from_dict(obj["sessionInfo"]) if obj.get("sessionInfo") is not None else None,
            "timestamp": obj.get("timestamp"),
            "user": User.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "pathname": obj.get("pathname"),
            "channels": obj.get("channels"),
            "url": obj.get("url"),
            "uiElement": obj.get("uiElement"),
            "manualFeedbackInfo": ManualFeedbackInfo.from_dict(obj["manualFeedbackInfo"]) if obj.get("manualFeedbackInfo") is not None else None,
            "seenFeedbackInfo": SeenFeedbackInfo.from_dict(obj["seenFeedbackInfo"]) if obj.get("seenFeedbackInfo") is not None else None,
            "userViewInfo": UserViewInfo.from_dict(obj["userViewInfo"]) if obj.get("userViewInfo") is not None else None,
            "debugInfo": FeedbackDebugInfo.from_dict(obj["debugInfo"]) if obj.get("debugInfo") is not None else None,
            "applicationId": obj.get("applicationId")
        })
        return _obj

