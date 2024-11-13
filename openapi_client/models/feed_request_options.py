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
from openapi_client.models.chat_zero_state_suggestion_options import ChatZeroStateSuggestionOptions
from openapi_client.models.feed_request_options_category_to_result_size_value import FeedRequestOptionsCategoryToResultSizeValue
from typing import Optional, Set
from typing_extensions import Self

class FeedRequestOptions(BaseModel):
    """
    FeedRequestOptions
    """ # noqa: E501
    result_size: StrictInt = Field(description="Number of results asked in response. If a result is a collection, counts as one.", alias="resultSize")
    timezone_offset: Optional[StrictInt] = Field(default=None, description="The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.", alias="timezoneOffset")
    category_to_result_size: Optional[Dict[str, FeedRequestOptionsCategoryToResultSizeValue]] = Field(default=None, description="Mapping from category to number of results asked for the category.", alias="categoryToResultSize")
    datasource_filter: Optional[List[StrictStr]] = Field(default=None, description="Datasources for which content should be included. Empty is for all.", alias="datasourceFilter")
    chat_zero_state_suggestion_options: Optional[ChatZeroStateSuggestionOptions] = Field(default=None, alias="chatZeroStateSuggestionOptions")
    __properties: ClassVar[List[str]] = ["resultSize", "timezoneOffset", "categoryToResultSize", "datasourceFilter", "chatZeroStateSuggestionOptions"]

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
        """Create an instance of FeedRequestOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in category_to_result_size (dict)
        _field_dict = {}
        if self.category_to_result_size:
            for _key_category_to_result_size in self.category_to_result_size:
                if self.category_to_result_size[_key_category_to_result_size]:
                    _field_dict[_key_category_to_result_size] = self.category_to_result_size[_key_category_to_result_size].to_dict()
            _dict['categoryToResultSize'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of chat_zero_state_suggestion_options
        if self.chat_zero_state_suggestion_options:
            _dict['chatZeroStateSuggestionOptions'] = self.chat_zero_state_suggestion_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FeedRequestOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resultSize": obj.get("resultSize"),
            "timezoneOffset": obj.get("timezoneOffset"),
            "categoryToResultSize": dict(
                (_k, FeedRequestOptionsCategoryToResultSizeValue.from_dict(_v))
                for _k, _v in obj["categoryToResultSize"].items()
            )
            if obj.get("categoryToResultSize") is not None
            else None,
            "datasourceFilter": obj.get("datasourceFilter"),
            "chatZeroStateSuggestionOptions": ChatZeroStateSuggestionOptions.from_dict(obj["chatZeroStateSuggestionOptions"]) if obj.get("chatZeroStateSuggestionOptions") is not None else None
        })
        return _obj


