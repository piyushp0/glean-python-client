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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.facet_filter import FacetFilter
from openapi_client.models.sort_options import SortOptions
from typing import Optional, Set
from typing_extensions import Self

class ListEntitiesRequest(BaseModel):
    """
    ListEntitiesRequest
    """ # noqa: E501
    filter: Optional[List[FacetFilter]] = None
    sort: Optional[List[SortOptions]] = Field(default=None, description="Use EntitiesSortOrder enum for SortOptions.sortBy")
    entity_type: Optional[StrictStr] = Field(default='PEOPLE', alias="entityType")
    datasource: Optional[StrictStr] = Field(default=None, description="The datasource associated with the entity type, most commonly used with CUSTOM_ENTITIES")
    query: Optional[StrictStr] = Field(default=None, description="A query string to search for entities that each entity in the response must conform to. An empty query does not filter any entities.")
    include_fields: Optional[List[StrictStr]] = Field(default=None, description="List of entity fields to return (that aren't returned by default)", alias="includeFields")
    page_size: Optional[StrictInt] = Field(default=None, description="Hint to the server about how many results to send back. Server may return less.", alias="pageSize")
    cursor: Optional[StrictStr] = Field(default=None, description="Pagination cursor. A previously received opaque token representing the position in the overall results at which to start.")
    source: Optional[StrictStr] = Field(default=None, description="A string denoting the search surface from which the endpoint is called.")
    __properties: ClassVar[List[str]] = ["filter", "sort", "entityType", "datasource", "query", "includeFields", "pageSize", "cursor", "source"]

    @field_validator('entity_type')
    def entity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PEOPLE', 'TEAMS', 'CUSTOM_ENTITIES']):
            raise ValueError("must be one of enum values ('PEOPLE', 'TEAMS', 'CUSTOM_ENTITIES')")
        return value

    @field_validator('include_fields')
    def include_fields_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['PEOPLE', 'TEAMS', 'PEOPLE_DISTANCE', 'PERMISSIONS', 'FACETS', 'INVITE_INFO', 'LAST_EXTENSION_USE', 'MANAGEMENT_DETAILS', 'UNPROCESSED_TEAMS']):
                raise ValueError("each list item must be one of ('PEOPLE', 'TEAMS', 'PEOPLE_DISTANCE', 'PERMISSIONS', 'FACETS', 'INVITE_INFO', 'LAST_EXTENSION_USE', 'MANAGEMENT_DETAILS', 'UNPROCESSED_TEAMS')")
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
        """Create an instance of ListEntitiesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in filter (list)
        _items = []
        if self.filter:
            for _item_filter in self.filter:
                if _item_filter:
                    _items.append(_item_filter.to_dict())
            _dict['filter'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sort (list)
        _items = []
        if self.sort:
            for _item_sort in self.sort:
                if _item_sort:
                    _items.append(_item_sort.to_dict())
            _dict['sort'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListEntitiesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filter": [FacetFilter.from_dict(_item) for _item in obj["filter"]] if obj.get("filter") is not None else None,
            "sort": [SortOptions.from_dict(_item) for _item in obj["sort"]] if obj.get("sort") is not None else None,
            "entityType": obj.get("entityType") if obj.get("entityType") is not None else 'PEOPLE',
            "datasource": obj.get("datasource"),
            "query": obj.get("query"),
            "includeFields": obj.get("includeFields"),
            "pageSize": obj.get("pageSize"),
            "cursor": obj.get("cursor"),
            "source": obj.get("source")
        })
        return _obj


