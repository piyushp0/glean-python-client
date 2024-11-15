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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.auth_token import AuthToken
from openapi_client.models.facet_bucket_filter import FacetBucketFilter
from openapi_client.models.facet_filter import FacetFilter
from openapi_client.models.facet_filter_set import FacetFilterSet
from openapi_client.models.restriction_filters import RestrictionFilters
from typing import Optional, Set
from typing_extensions import Self

class SearchRequestOptions(BaseModel):
    """
    SearchRequestOptions
    """ # noqa: E501
    datasource_filter: Optional[StrictStr] = Field(default=None, description="Filter results to a single datasource name (e.g. gmail, slack). All results are returned if missing.", alias="datasourceFilter")
    datasources_filter: Optional[List[StrictStr]] = Field(default=None, description="Filter results to one or more datasources (e.g. gmail, slack). All results are returned if missing.", alias="datasourcesFilter")
    query_overrides_facet_filters: Optional[StrictBool] = Field(default=None, description="If true, the operators in the query are taken to override any operators in facetFilters in the case of conflict. This is used to correctly set rewrittenFacetFilters and rewrittenQuery.", alias="queryOverridesFacetFilters")
    facet_filters: Optional[List[FacetFilter]] = Field(default=None, description="A list of filters for the query. An AND is assumed between different facetFilters. For example, owner Sumeet and type Spreadsheet shows documents that are by Sumeet AND are Spreadsheets.", alias="facetFilters")
    facet_filter_sets: Optional[List[FacetFilterSet]] = Field(default=None, description="A list of facet filter sets that will be OR'ed together. SearchRequestOptions where both facetFilterSets and facetFilters set are considered as bad request. Callers should set only one of these fields.", alias="facetFilterSets")
    facet_bucket_filter: Optional[FacetBucketFilter] = Field(default=None, alias="facetBucketFilter")
    facet_bucket_size: StrictInt = Field(description="The maximum number of FacetBuckets to return in each FacetResult.", alias="facetBucketSize")
    default_facets: Optional[List[StrictStr]] = Field(default=None, description="Facets for which FacetResults should be fetched and that don't apply to a particular datasource. If specified, these values will replace the standard default facets (last_updated_at, from, etc.). The requested facets will be returned alongside datasource-specific facets if searching a single datasource.", alias="defaultFacets")
    auth_tokens: Optional[List[AuthToken]] = Field(default=None, description="Auth tokens which may be used for non-indexed, federated results (e.g. Gmail).", alias="authTokens")
    fetch_all_datasource_counts: Optional[StrictBool] = Field(default=None, description="Hints that the QE should return result counts (via the datasource facet result) for all supported datasources, rather than just those specified in the datasource[s]Filter", alias="fetchAllDatasourceCounts")
    response_hints: Optional[List[StrictStr]] = Field(default=None, description="Array of hints containing which fields should be populated in the response.", alias="responseHints")
    timezone_offset: Optional[StrictInt] = Field(default=None, description="The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.", alias="timezoneOffset")
    disable_spellcheck: Optional[StrictBool] = Field(default=None, description="Whether or not to disable spellcheck.", alias="disableSpellcheck")
    disable_query_autocorrect: Optional[StrictBool] = Field(default=None, description="Disables automatic adjustment of the input query for spelling corrections or other reasons.", alias="disableQueryAutocorrect")
    return_llm_content_over_snippets: Optional[StrictBool] = Field(default=None, description="[beta] Enables expanded content to be returned for LLM usage. The size of content per result returned should be modified using maxSnippetSize. Server may return less or more than what is specified in maxSnippetSize. For more details, https://docs.google.com/document/d/1CTOLSxWWT9WDEnHVLoCUaxbGYyXYP8kctPRF-RluSQY/edit. Requires sufficient permissions.", alias="returnLlmContentOverSnippets")
    inclusions: Optional[RestrictionFilters] = None
    exclusions: Optional[RestrictionFilters] = None
    __properties: ClassVar[List[str]] = ["datasourceFilter", "datasourcesFilter", "queryOverridesFacetFilters", "facetFilters", "facetFilterSets", "facetBucketFilter", "facetBucketSize", "defaultFacets", "authTokens", "fetchAllDatasourceCounts", "responseHints", "timezoneOffset", "disableSpellcheck", "disableQueryAutocorrect", "returnLlmContentOverSnippets", "inclusions", "exclusions"]

    @field_validator('response_hints')
    def response_hints_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ALL_RESULT_COUNTS', 'FACET_RESULTS', 'QUERY_METADATA', 'RESULTS', 'SPELLCHECK_METADATA']):
                raise ValueError("each list item must be one of ('ALL_RESULT_COUNTS', 'FACET_RESULTS', 'QUERY_METADATA', 'RESULTS', 'SPELLCHECK_METADATA')")
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
        """Create an instance of SearchRequestOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in facet_filters (list)
        _items = []
        if self.facet_filters:
            for _item_facet_filters in self.facet_filters:
                if _item_facet_filters:
                    _items.append(_item_facet_filters.to_dict())
            _dict['facetFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in facet_filter_sets (list)
        _items = []
        if self.facet_filter_sets:
            for _item_facet_filter_sets in self.facet_filter_sets:
                if _item_facet_filter_sets:
                    _items.append(_item_facet_filter_sets.to_dict())
            _dict['facetFilterSets'] = _items
        # override the default output from pydantic by calling `to_dict()` of facet_bucket_filter
        if self.facet_bucket_filter:
            _dict['facetBucketFilter'] = self.facet_bucket_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in auth_tokens (list)
        _items = []
        if self.auth_tokens:
            for _item_auth_tokens in self.auth_tokens:
                if _item_auth_tokens:
                    _items.append(_item_auth_tokens.to_dict())
            _dict['authTokens'] = _items
        # override the default output from pydantic by calling `to_dict()` of inclusions
        if self.inclusions:
            _dict['inclusions'] = self.inclusions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exclusions
        if self.exclusions:
            _dict['exclusions'] = self.exclusions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchRequestOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "datasourceFilter": obj.get("datasourceFilter"),
            "datasourcesFilter": obj.get("datasourcesFilter"),
            "queryOverridesFacetFilters": obj.get("queryOverridesFacetFilters"),
            "facetFilters": [FacetFilter.from_dict(_item) for _item in obj["facetFilters"]] if obj.get("facetFilters") is not None else None,
            "facetFilterSets": [FacetFilterSet.from_dict(_item) for _item in obj["facetFilterSets"]] if obj.get("facetFilterSets") is not None else None,
            "facetBucketFilter": FacetBucketFilter.from_dict(obj["facetBucketFilter"]) if obj.get("facetBucketFilter") is not None else None,
            "facetBucketSize": obj.get("facetBucketSize"),
            "defaultFacets": obj.get("defaultFacets"),
            "authTokens": [AuthToken.from_dict(_item) for _item in obj["authTokens"]] if obj.get("authTokens") is not None else None,
            "fetchAllDatasourceCounts": obj.get("fetchAllDatasourceCounts"),
            "responseHints": obj.get("responseHints"),
            "timezoneOffset": obj.get("timezoneOffset"),
            "disableSpellcheck": obj.get("disableSpellcheck"),
            "disableQueryAutocorrect": obj.get("disableQueryAutocorrect"),
            "returnLlmContentOverSnippets": obj.get("returnLlmContentOverSnippets"),
            "inclusions": RestrictionFilters.from_dict(obj["inclusions"]) if obj.get("inclusions") is not None else None,
            "exclusions": RestrictionFilters.from_dict(obj["exclusions"]) if obj.get("exclusions") is not None else None
        })
        return _obj


