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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.error_info import ErrorInfo
from openapi_client.models.generated_qna import GeneratedQna
from openapi_client.models.search_result import SearchResult
from openapi_client.models.session_info import SessionInfo
from openapi_client.models.structured_result import StructuredResult
from typing import Optional, Set
from typing_extensions import Self

class ResultsResponse(BaseModel):
    """
    ResultsResponse
    """ # noqa: E501
    tracking_token: Optional[StrictStr] = Field(default=None, description="A token that should be passed for additional requests related to this request (such as more results requests).", alias="trackingToken")
    session_info: Optional[SessionInfo] = Field(default=None, alias="sessionInfo")
    results: Optional[List[SearchResult]] = None
    structured_results: Optional[List[StructuredResult]] = Field(default=None, alias="structuredResults")
    generated_qna_result: Optional[GeneratedQna] = Field(default=None, alias="generatedQnaResult")
    error_info: Optional[ErrorInfo] = Field(default=None, alias="errorInfo")
    request_id: Optional[StrictStr] = Field(default=None, description="A platform-generated request ID to correlate backend logs.", alias="requestID")
    backend_time_millis: Optional[StrictInt] = Field(default=None, description="Time in milliseconds the backend took to respond to the request.", alias="backendTimeMillis")
    __properties: ClassVar[List[str]] = ["trackingToken", "sessionInfo", "results", "structuredResults", "generatedQnaResult", "errorInfo", "requestID", "backendTimeMillis"]

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
        """Create an instance of ResultsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item_results in self.results:
                if _item_results:
                    _items.append(_item_results.to_dict())
            _dict['results'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in structured_results (list)
        _items = []
        if self.structured_results:
            for _item_structured_results in self.structured_results:
                if _item_structured_results:
                    _items.append(_item_structured_results.to_dict())
            _dict['structuredResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of generated_qna_result
        if self.generated_qna_result:
            _dict['generatedQnaResult'] = self.generated_qna_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error_info
        if self.error_info:
            _dict['errorInfo'] = self.error_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResultsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "trackingToken": obj.get("trackingToken"),
            "sessionInfo": SessionInfo.from_dict(obj["sessionInfo"]) if obj.get("sessionInfo") is not None else None,
            "results": [SearchResult.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "structuredResults": [StructuredResult.from_dict(_item) for _item in obj["structuredResults"]] if obj.get("structuredResults") is not None else None,
            "generatedQnaResult": GeneratedQna.from_dict(obj["generatedQnaResult"]) if obj.get("generatedQnaResult") is not None else None,
            "errorInfo": ErrorInfo.from_dict(obj["errorInfo"]) if obj.get("errorInfo") is not None else None,
            "requestID": obj.get("requestID"),
            "backendTimeMillis": obj.get("backendTimeMillis")
        })
        return _obj


