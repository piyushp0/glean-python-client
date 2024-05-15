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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.alert_data import AlertData
from openapi_client.models.communication_template import CommunicationTemplate
from openapi_client.models.document import Document
from openapi_client.models.email_request_chat_feedback_payload import EmailRequestChatFeedbackPayload
from openapi_client.models.email_request_feedback_payload import EmailRequestFeedbackPayload
from openapi_client.models.people_filters import PeopleFilters
from openapi_client.models.person import Person
from typing import Optional, Set
from typing_extensions import Self

class EmailRequest(BaseModel):
    """
    A request to send email[s] to the specified users
    """ # noqa: E501
    email_template: CommunicationTemplate = Field(alias="emailTemplate")
    alert_data: Optional[AlertData] = Field(default=None, alias="alertData")
    recipients: Optional[List[Person]] = Field(default=None, description="The people to send emails to")
    recipient_filters: Optional[PeopleFilters] = Field(default=None, alias="recipientFilters")
    company_name: Optional[StrictStr] = Field(default=None, description="Name of the company.", alias="companyName")
    datasource_instance: Optional[StrictStr] = Field(default=None, description="The instance ID of the datasource (if any)", alias="datasourceInstance")
    senders: Optional[List[Person]] = Field(default=None, description="The people who triggered this email")
    web_app_url: Optional[StrictStr] = Field(default=None, description="The URL of the client triggering the request, as received in the ClientConfig", alias="webAppUrl")
    server_url: Optional[StrictStr] = Field(default=None, description="The URL of the QE instance the email request is processed by.", alias="serverUrl")
    unsubscribe_url: Optional[StrictStr] = Field(default=None, description="The URL to unsubscribe from emails.", alias="unsubscribeUrl")
    documents: Optional[List[Document]] = Field(default=None, description="The documents this email request refers to")
    reasons: Optional[List[StrictStr]] = Field(default=None, description="Reasons this email request was sent. Will be shown directly to end user.")
    blocks: Optional[Dict[str, List[Dict[str, Any]]]] = Field(default=None, description="For building complex email UIs, we use a block structure that dictates what we create in the UI")
    subjects: Optional[Dict[str, StrictStr]] = Field(default=None, description="Mapping of recipientIds to the email subject they are to receive. Optional and only meant for templates with Sendgrid subject set to {{subject}}")
    feedback_payload: Optional[EmailRequestFeedbackPayload] = Field(default=None, alias="feedbackPayload")
    chat_feedback_payload: Optional[EmailRequestChatFeedbackPayload] = Field(default=None, alias="chatFeedbackPayload")
    __properties: ClassVar[List[str]] = ["emailTemplate", "alertData", "recipients", "recipientFilters", "companyName", "datasourceInstance", "senders", "webAppUrl", "serverUrl", "unsubscribeUrl", "documents", "reasons", "blocks", "subjects", "feedbackPayload", "chatFeedbackPayload"]

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
        """Create an instance of EmailRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of alert_data
        if self.alert_data:
            _dict['alertData'] = self.alert_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recipients (list)
        _items = []
        if self.recipients:
            for _item in self.recipients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipients'] = _items
        # override the default output from pydantic by calling `to_dict()` of recipient_filters
        if self.recipient_filters:
            _dict['recipientFilters'] = self.recipient_filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in senders (list)
        _items = []
        if self.senders:
            for _item in self.senders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['senders'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item in self.documents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of feedback_payload
        if self.feedback_payload:
            _dict['feedbackPayload'] = self.feedback_payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat_feedback_payload
        if self.chat_feedback_payload:
            _dict['chatFeedbackPayload'] = self.chat_feedback_payload.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmailRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "emailTemplate": obj.get("emailTemplate"),
            "alertData": AlertData.from_dict(obj["alertData"]) if obj.get("alertData") is not None else None,
            "recipients": [Person.from_dict(_item) for _item in obj["recipients"]] if obj.get("recipients") is not None else None,
            "recipientFilters": PeopleFilters.from_dict(obj["recipientFilters"]) if obj.get("recipientFilters") is not None else None,
            "companyName": obj.get("companyName"),
            "datasourceInstance": obj.get("datasourceInstance"),
            "senders": [Person.from_dict(_item) for _item in obj["senders"]] if obj.get("senders") is not None else None,
            "webAppUrl": obj.get("webAppUrl"),
            "serverUrl": obj.get("serverUrl"),
            "unsubscribeUrl": obj.get("unsubscribeUrl"),
            "documents": [Document.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None,
            "reasons": obj.get("reasons"),
            "blocks": obj.get("blocks"),
            "subjects": obj.get("subjects"),
            "feedbackPayload": EmailRequestFeedbackPayload.from_dict(obj["feedbackPayload"]) if obj.get("feedbackPayload") is not None else None,
            "chatFeedbackPayload": EmailRequestChatFeedbackPayload.from_dict(obj["chatFeedbackPayload"]) if obj.get("chatFeedbackPayload") is not None else None
        })
        return _obj


