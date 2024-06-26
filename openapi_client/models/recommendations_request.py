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
from openapi_client.models.document import Document
from openapi_client.models.document_spec import DocumentSpec
from openapi_client.models.recommendations_request_options import RecommendationsRequestOptions
from openapi_client.models.session_info import SessionInfo
from typing import Optional, Set
from typing_extensions import Self

class RecommendationsRequest(BaseModel):
    """
    RecommendationsRequest
    """ # noqa: E501
    timestamp: Optional[datetime] = Field(default=None, description="The ISO 8601 timestamp associated with the client request.")
    tracking_token: Optional[StrictStr] = Field(default=None, description="A previously received trackingToken for a search associated with the same query. Useful for more requests and requests for other tabs.", alias="trackingToken")
    session_info: Optional[SessionInfo] = Field(default=None, alias="sessionInfo")
    source_document: Optional[Document] = Field(default=None, alias="sourceDocument")
    page_size: Optional[StrictInt] = Field(default=None, description="Hint to the server about how many results to send back. Server may return less or more. Structured results and clustered results don't count towards pageSize.", alias="pageSize")
    max_snippet_size: Optional[StrictInt] = Field(default=None, description="Hint to the server about how many characters long a snippet may be. Server may return less or more.", alias="maxSnippetSize")
    recommendation_document_spec: Optional[DocumentSpec] = Field(default=None, alias="recommendationDocumentSpec")
    request_options: Optional[RecommendationsRequestOptions] = Field(default=None, alias="requestOptions")
    __properties: ClassVar[List[str]] = ["timestamp", "trackingToken", "sessionInfo", "sourceDocument", "pageSize", "maxSnippetSize", "recommendationDocumentSpec", "requestOptions"]

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
        """Create an instance of RecommendationsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_document
        if self.source_document:
            _dict['sourceDocument'] = self.source_document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recommendation_document_spec
        if self.recommendation_document_spec:
            _dict['recommendationDocumentSpec'] = self.recommendation_document_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of request_options
        if self.request_options:
            _dict['requestOptions'] = self.request_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecommendationsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "trackingToken": obj.get("trackingToken"),
            "sessionInfo": SessionInfo.from_dict(obj["sessionInfo"]) if obj.get("sessionInfo") is not None else None,
            "sourceDocument": Document.from_dict(obj["sourceDocument"]) if obj.get("sourceDocument") is not None else None,
            "pageSize": obj.get("pageSize"),
            "maxSnippetSize": obj.get("maxSnippetSize"),
            "recommendationDocumentSpec": DocumentSpec.from_dict(obj["recommendationDocumentSpec"]) if obj.get("recommendationDocumentSpec") is not None else None,
            "requestOptions": RecommendationsRequestOptions.from_dict(obj["requestOptions"]) if obj.get("requestOptions") is not None else None
        })
        return _obj


