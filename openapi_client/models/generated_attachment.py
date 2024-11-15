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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.customer import Customer
from openapi_client.models.document import Document
from openapi_client.models.event_strategy_name import EventStrategyName
from openapi_client.models.generated_attachment_content import GeneratedAttachmentContent
from openapi_client.models.person import Person
from openapi_client.models.structured_link import StructuredLink
from typing import Optional, Set
from typing_extensions import Self

class GeneratedAttachment(BaseModel):
    """
    These are attachments that aren't natively present on the event, and have been smartly suggested.
    """ # noqa: E501
    strategy_name: Optional[EventStrategyName] = Field(default=None, alias="strategyName")
    documents: Optional[List[Document]] = None
    person: Optional[Person] = None
    customer: Optional[Customer] = None
    external_links: Optional[List[StructuredLink]] = Field(default=None, description="A list of links to external sources outside of Glean.", alias="externalLinks")
    content: Optional[List[GeneratedAttachmentContent]] = None
    __properties: ClassVar[List[str]] = ["strategyName", "documents", "person", "customer", "externalLinks", "content"]

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
        """Create an instance of GeneratedAttachment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item_documents in self.documents:
                if _item_documents:
                    _items.append(_item_documents.to_dict())
            _dict['documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in external_links (list)
        _items = []
        if self.external_links:
            for _item_external_links in self.external_links:
                if _item_external_links:
                    _items.append(_item_external_links.to_dict())
            _dict['externalLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in content (list)
        _items = []
        if self.content:
            for _item_content in self.content:
                if _item_content:
                    _items.append(_item_content.to_dict())
            _dict['content'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GeneratedAttachment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "strategyName": obj.get("strategyName"),
            "documents": [Document.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None,
            "person": Person.from_dict(obj["person"]) if obj.get("person") is not None else None,
            "customer": Customer.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "externalLinks": [StructuredLink.from_dict(_item) for _item in obj["externalLinks"]] if obj.get("externalLinks") is not None else None,
            "content": [GeneratedAttachmentContent.from_dict(_item) for _item in obj["content"]] if obj.get("content") is not None else None
        })
        return _obj


