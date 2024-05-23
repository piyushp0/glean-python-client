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
from openapi_client.models.cluster_type_enum import ClusterTypeEnum
from openapi_client.models.search_result_prominence_enum import SearchResultProminenceEnum
from typing import Optional, Set
from typing_extensions import Self

class SearchResult(BaseModel):
    """
    SearchResult
    """ # noqa: E501
    structured_results: Optional[List[StructuredResult]] = Field(default=None, description="An array of entities in the work graph retrieved via a data request.", alias="structuredResults")
    tracking_token: Optional[StrictStr] = Field(default=None, description="An opaque token that represents this particular result in this particular query. To be used for /feedback reporting.", alias="trackingToken")
    document: Optional[Document] = None
    title: Optional[StrictStr] = None
    url: StrictStr
    native_app_url: Optional[StrictStr] = Field(default=None, description="A deep link, if available, into the datasource's native application for the user's platform (e.g. slack://...).", alias="nativeAppUrl")
    snippets: Optional[List[SearchResultSnippet]] = Field(default=None, description="Text content from the result document which contains search query terms, if available.")
    expanded_snippets: Optional[List[StrictStr]] = Field(default=None, description="The expanded snippets for this result. This is only populated if the query has the expand_snippets parameter set to true.", alias="expandedSnippets")
    full_text: Optional[StrictStr] = Field(default=None, description="The full body text of the result if not already contained in the snippets", alias="fullText")
    full_text_list: Optional[List[StrictStr]] = Field(default=None, description="The full body text of the result if not already contained in the snippets; each item in the array represents a separate line in the original text", alias="fullTextList")
    related_results: Optional[List[RelatedDocuments]] = Field(default=None, description="A list of results related to this search result. Eg. for conversation results it contains individual messages from the conversation document which will be shown on SERP.", alias="relatedResults")
    clustered_results: Optional[List[SearchResult]] = Field(default=None, description="A list of results that should be displayed as associated with this result.", alias="clusteredResults")
    all_clustered_results: Optional[List[ClusterGroup]] = Field(default=None, description="A list of results that should be displayed as associated with this result.", alias="allClusteredResults")
    attachment_count: Optional[StrictInt] = Field(default=None, description="The total number of attachments.", alias="attachmentCount")
    attachments: Optional[List[SearchResult]] = Field(default=None, description="A (potentially partial) list of results representing documents attached to the main result document.")
    backlink_results: Optional[List[SearchResult]] = Field(default=None, description="A list of results that should be displayed as backlinks of this result in reverse chronological order.", alias="backlinkResults")
    cluster_type: Optional[ClusterTypeEnum] = Field(default=None, alias="clusterType")
    query_suggestion: Optional[QuerySuggestion] = Field(default=None, alias="querySuggestion")
    prominence: Optional[SearchResultProminenceEnum] = None
    attachment_context: Optional[StrictStr] = Field(default=None, description="Additional context for the relationship between the result and the document it's attached to.", alias="attachmentContext")
    pins: Optional[List[PinDocument]] = Field(default=None, description="A list of pins associated with this search result.")
    __properties: ClassVar[List[str]] = ["structuredResults", "trackingToken", "document", "title", "url", "nativeAppUrl", "snippets", "expandedSnippets", "fullText", "fullTextList", "relatedResults", "clusteredResults", "allClusteredResults", "attachmentCount", "attachments", "backlinkResults", "clusterType", "mustIncludeSuggestions", "querySuggestion", "prominence", "attachmentContext", "pins"]

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
        """Create an instance of SearchResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in structured_results (list)
        _items = []
        if self.structured_results:
            for _item in self.structured_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['structuredResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict['document'] = self.document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in snippets (list)
        _items = []
        if self.snippets:
            for _item in self.snippets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['snippets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in related_results (list)
        _items = []
        if self.related_results:
            for _item in self.related_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relatedResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in clustered_results (list)
        _items = []
        if self.clustered_results:
            for _item in self.clustered_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clusteredResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in all_clustered_results (list)
        _items = []
        if self.all_clustered_results:
            for _item in self.all_clustered_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['allClusteredResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in backlink_results (list)
        _items = []
        if self.backlink_results:
            for _item in self.backlink_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['backlinkResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of must_include_suggestions
        if self.must_include_suggestions:
            _dict['mustIncludeSuggestions'] = self.must_include_suggestions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of query_suggestion
        if self.query_suggestion:
            _dict['querySuggestion'] = self.query_suggestion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pins (list)
        _items = []
        if self.pins:
            for _item in self.pins:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pins'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "structuredResults": [StructuredResult.from_dict(_item) for _item in obj["structuredResults"]] if obj.get("structuredResults") is not None else None,
            "trackingToken": obj.get("trackingToken"),
            "document": Document.from_dict(obj["document"]) if obj.get("document") is not None else None,
            "title": obj.get("title"),
            "url": obj.get("url"),
            "nativeAppUrl": obj.get("nativeAppUrl"),
            "snippets": [SearchResultSnippet.from_dict(_item) for _item in obj["snippets"]] if obj.get("snippets") is not None else None,
            "expandedSnippets": obj.get("expandedSnippets"),
            "fullText": obj.get("fullText"),
            "fullTextList": obj.get("fullTextList"),
            "relatedResults": [RelatedDocuments.from_dict(_item) for _item in obj["relatedResults"]] if obj.get("relatedResults") is not None else None,
            "clusteredResults": [SearchResult.from_dict(_item) for _item in obj["clusteredResults"]] if obj.get("clusteredResults") is not None else None,
            "allClusteredResults": [ClusterGroup.from_dict(_item) for _item in obj["allClusteredResults"]] if obj.get("allClusteredResults") is not None else None,
            "attachmentCount": obj.get("attachmentCount"),
            "attachments": [SearchResult.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "backlinkResults": [SearchResult.from_dict(_item) for _item in obj["backlinkResults"]] if obj.get("backlinkResults") is not None else None,
            "clusterType": obj.get("clusterType"),
            "querySuggestion": QuerySuggestion.from_dict(obj["querySuggestion"]) if obj.get("querySuggestion") is not None else None,
            "prominence": obj.get("prominence"),
            "attachmentContext": obj.get("attachmentContext"),
            "pins": [PinDocument.from_dict(_item) for _item in obj["pins"]] if obj.get("pins") is not None else None
        })
        return _obj

from openapi_client.models.cluster_group import ClusterGroup
from openapi_client.models.document import Document
from openapi_client.models.pin_document import PinDocument
from openapi_client.models.query_suggestion import QuerySuggestion
from openapi_client.models.query_suggestion_list import QuerySuggestionList
from openapi_client.models.related_documents import RelatedDocuments
from openapi_client.models.search_result_snippet import SearchResultSnippet
from openapi_client.models.structured_result import StructuredResult
# TODO: Rewrite to not use raise_errors
SearchResult.model_rebuild(raise_errors=False)

