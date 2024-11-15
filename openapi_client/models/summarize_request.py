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
from openapi_client.models.document_spec import DocumentSpec
from typing import Optional, Set
from typing_extensions import Self

class SummarizeRequest(BaseModel):
    """
    Summary of the document
    """ # noqa: E501
    timestamp: Optional[datetime] = Field(default=None, description="The ISO 8601 timestamp associated with the client request.")
    query: Optional[StrictStr] = Field(default=None, description="Optional query that the summary should be about")
    preferred_summary_length: Optional[StrictInt] = Field(default=None, description="Optional length of summary output. If not given, defaults to 500 chars.", alias="preferredSummaryLength")
    document_specs: List[DocumentSpec] = Field(description="Specifications of documents to summarize", alias="documentSpecs")
    tracking_token: Optional[StrictStr] = Field(default=None, description="An opaque token that represents this particular result. To be used for /feedback reporting.", alias="trackingToken")
    __properties: ClassVar[List[str]] = ["timestamp", "query", "preferredSummaryLength", "documentSpecs", "trackingToken"]

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
        """Create an instance of SummarizeRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in document_specs (list)
        _items = []
        if self.document_specs:
            for _item_document_specs in self.document_specs:
                if _item_document_specs:
                    _items.append(_item_document_specs.to_dict())
            _dict['documentSpecs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SummarizeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "query": obj.get("query"),
            "preferredSummaryLength": obj.get("preferredSummaryLength"),
            "documentSpecs": [DocumentSpec.from_dict(_item) for _item in obj["documentSpecs"]] if obj.get("documentSpecs") is not None else None,
            "trackingToken": obj.get("trackingToken")
        })
        return _obj


