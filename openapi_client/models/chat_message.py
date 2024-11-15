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
from openapi_client.models.agent_config import AgentConfig
from openapi_client.models.chat_message_citation import ChatMessageCitation
from openapi_client.models.chat_message_fragment import ChatMessageFragment
from typing import Optional, Set
from typing_extensions import Self

class ChatMessage(BaseModel):
    """
    A message that is rendered as one coherent unit with one given sender.
    """ # noqa: E501
    agent_config: Optional[AgentConfig] = Field(default=None, alias="agentConfig")
    author: Optional[StrictStr] = 'USER'
    citations: Optional[List[ChatMessageCitation]] = Field(default=None, description="A list of Citations that were used to generate the response.")
    uploaded_file_ids: Optional[List[StrictStr]] = Field(default=None, description="IDs of files uploaded in the message that are referenced to generate the answer.", alias="uploadedFileIds")
    fragments: Optional[List[ChatMessageFragment]] = Field(default=None, description="A list of rich data used to represent the response or formulate a request. These are linearly stitched together to support richer data formats beyond simple text.")
    ts: Optional[StrictStr] = Field(default=None, description="Response timestamp of the message.")
    message_id: Optional[StrictStr] = Field(default=None, description="A unique server-side generated ID used to identify a message, automatically populated for any USER authored messages.", alias="messageId")
    message_tracking_token: Optional[StrictStr] = Field(default=None, description="Opaque tracking token generated server-side.", alias="messageTrackingToken")
    message_type: Optional[StrictStr] = Field(default='CONTENT', description="Semantically groups content of a certain type. It can be used for purposes such as differential UI treatment. USER authored messages should be of type CONTENT and do not need `messageType` specified.", alias="messageType")
    has_more_fragments: Optional[StrictBool] = Field(default=None, description="Signals there are additional response fragments incoming.", alias="hasMoreFragments")
    __properties: ClassVar[List[str]] = ["agentConfig", "author", "citations", "uploadedFileIds", "fragments", "ts", "messageId", "messageTrackingToken", "messageType", "hasMoreFragments"]

    @field_validator('author')
    def author_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['USER', 'GLEAN_AI']):
            raise ValueError("must be one of enum values ('USER', 'GLEAN_AI')")
        return value

    @field_validator('message_type')
    def message_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UPDATE', 'CONTENT', 'CONTEXT', 'DEBUG', 'DEBUG_EXTERNAL', 'ERROR', 'HEADING', 'WARNING']):
            raise ValueError("must be one of enum values ('UPDATE', 'CONTENT', 'CONTEXT', 'DEBUG', 'DEBUG_EXTERNAL', 'ERROR', 'HEADING', 'WARNING')")
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
        """Create an instance of ChatMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agent_config
        if self.agent_config:
            _dict['agentConfig'] = self.agent_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in citations (list)
        _items = []
        if self.citations:
            for _item_citations in self.citations:
                if _item_citations:
                    _items.append(_item_citations.to_dict())
            _dict['citations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fragments (list)
        _items = []
        if self.fragments:
            for _item_fragments in self.fragments:
                if _item_fragments:
                    _items.append(_item_fragments.to_dict())
            _dict['fragments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChatMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentConfig": AgentConfig.from_dict(obj["agentConfig"]) if obj.get("agentConfig") is not None else None,
            "author": obj.get("author") if obj.get("author") is not None else 'USER',
            "citations": [ChatMessageCitation.from_dict(_item) for _item in obj["citations"]] if obj.get("citations") is not None else None,
            "uploadedFileIds": obj.get("uploadedFileIds"),
            "fragments": [ChatMessageFragment.from_dict(_item) for _item in obj["fragments"]] if obj.get("fragments") is not None else None,
            "ts": obj.get("ts"),
            "messageId": obj.get("messageId"),
            "messageTrackingToken": obj.get("messageTrackingToken"),
            "messageType": obj.get("messageType") if obj.get("messageType") is not None else 'CONTENT',
            "hasMoreFragments": obj.get("hasMoreFragments")
        })
        return _obj


