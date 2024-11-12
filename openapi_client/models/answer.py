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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.document_spec import DocumentSpec
from openapi_client.models.facet_filter import FacetFilter
from openapi_client.models.object_permissions import ObjectPermissions
from typing import Optional, Set
from typing_extensions import Self

class Answer(BaseModel):
    """
    Answer
    """ # noqa: E501
    id: StrictInt = Field(description="The opaque ID of the Answer.")
    doc_id: Optional[StrictStr] = Field(default=None, description="Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred.", alias="docId")
    question: Optional[StrictStr] = None
    question_variations: Optional[List[StrictStr]] = Field(default=None, description="Additional ways of phrasing this question.", alias="questionVariations")
    body_text: Optional[StrictStr] = Field(default=None, description="The plain text answer to the question.", alias="bodyText")
    board_id: Optional[StrictInt] = Field(default=None, description="The parent board ID of this Answer, or 0 if it's a floating Answer.", alias="boardId")
    audience_filters: Optional[List[FacetFilter]] = Field(default=None, description="Filters which restrict who should see the answer. Values are taken from the corresponding filters in people search.", alias="audienceFilters")
    added_roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of user roles for the answer added by the owner.", alias="addedRoles")
    removed_roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of user roles for the answer removed by the owner.", alias="removedRoles")
    roles: Optional[List[UserRoleSpecification]] = Field(default=None, description="A list of roles for this answer explicitly granted by an owner, editor, or admin.")
    source_document_spec: Optional[DocumentSpec] = Field(default=None, alias="sourceDocumentSpec")
    source_type: Optional[StrictStr] = Field(default=None, alias="sourceType")
    permissions: Optional[ObjectPermissions] = None
    combined_answer_text: Optional[StructuredText] = Field(default=None, alias="combinedAnswerText")
    likes: Optional[AnswerLikes] = None
    author: Optional[Person] = None
    create_time: Optional[datetime] = Field(default=None, description="The time the answer was created in ISO format (ISO 8601).", alias="createTime")
    update_time: Optional[datetime] = Field(default=None, description="The time the answer was last updated in ISO format (ISO 8601).", alias="updateTime")
    updated_by: Optional[Person] = Field(default=None, alias="updatedBy")
    verification: Optional[Verification] = None
    board: Optional[AnswerBoard] = None
    collections: Optional[List[Collection]] = Field(default=None, description="The collections to which the answer belongs.")
    document_category: Optional[StrictStr] = Field(default=None, description="The document's document_category(.proto).", alias="documentCategory")
    source_document: Optional[Document] = Field(default=None, alias="sourceDocument")
    __properties: ClassVar[List[str]] = ["id", "docId", "question", "questionVariations", "bodyText", "boardId", "audienceFilters", "addedRoles", "removedRoles", "roles", "sourceDocumentSpec", "sourceType", "permissions", "combinedAnswerText", "likes", "author", "createTime", "updateTime", "updatedBy", "verification", "board", "collections", "documentCategory", "sourceDocument"]

    @field_validator('source_type')
    def source_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DOCUMENT', 'ASSISTANT']):
            raise ValueError("must be one of enum values ('DOCUMENT', 'ASSISTANT')")
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
        """Create an instance of Answer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in audience_filters (list)
        _items = []
        if self.audience_filters:
            for _item in self.audience_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['audienceFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in added_roles (list)
        _items = []
        if self.added_roles:
            for _item in self.added_roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addedRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in removed_roles (list)
        _items = []
        if self.removed_roles:
            for _item in self.removed_roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['removedRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of source_document_spec
        if self.source_document_spec:
            _dict['sourceDocumentSpec'] = self.source_document_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of combined_answer_text
        if self.combined_answer_text:
            _dict['combinedAnswerText'] = self.combined_answer_text.to_dict()
        # override the default output from pydantic by calling `to_dict()` of likes
        if self.likes:
            _dict['likes'] = self.likes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verification
        if self.verification:
            _dict['verification'] = self.verification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of board
        if self.board:
            _dict['board'] = self.board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in collections (list)
        _items = []
        if self.collections:
            for _item in self.collections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['collections'] = _items
        # override the default output from pydantic by calling `to_dict()` of source_document
        if self.source_document:
            _dict['sourceDocument'] = self.source_document.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Answer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "docId": obj.get("docId"),
            "question": obj.get("question"),
            "questionVariations": obj.get("questionVariations"),
            "bodyText": obj.get("bodyText"),
            "boardId": obj.get("boardId"),
            "audienceFilters": [FacetFilter.from_dict(_item) for _item in obj["audienceFilters"]] if obj.get("audienceFilters") is not None else None,
            "addedRoles": [UserRoleSpecification.from_dict(_item) for _item in obj["addedRoles"]] if obj.get("addedRoles") is not None else None,
            "removedRoles": [UserRoleSpecification.from_dict(_item) for _item in obj["removedRoles"]] if obj.get("removedRoles") is not None else None,
            "roles": [UserRoleSpecification.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "sourceDocumentSpec": DocumentSpec.from_dict(obj["sourceDocumentSpec"]) if obj.get("sourceDocumentSpec") is not None else None,
            "sourceType": obj.get("sourceType"),
            "permissions": ObjectPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "combinedAnswerText": StructuredText.from_dict(obj["combinedAnswerText"]) if obj.get("combinedAnswerText") is not None else None,
            "likes": AnswerLikes.from_dict(obj["likes"]) if obj.get("likes") is not None else None,
            "author": Person.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "createTime": obj.get("createTime"),
            "updateTime": obj.get("updateTime"),
            "updatedBy": Person.from_dict(obj["updatedBy"]) if obj.get("updatedBy") is not None else None,
            "verification": Verification.from_dict(obj["verification"]) if obj.get("verification") is not None else None,
            "board": AnswerBoard.from_dict(obj["board"]) if obj.get("board") is not None else None,
            "collections": [Collection.from_dict(_item) for _item in obj["collections"]] if obj.get("collections") is not None else None,
            "documentCategory": obj.get("documentCategory"),
            "sourceDocument": Document.from_dict(obj["sourceDocument"]) if obj.get("sourceDocument") is not None else None
        })
        return _obj

from openapi_client.models.answer_board import AnswerBoard
from openapi_client.models.answer_likes import AnswerLikes
from openapi_client.models.collection import Collection
from openapi_client.models.document import Document
from openapi_client.models.person import Person
from openapi_client.models.structured_text import StructuredText
from openapi_client.models.user_role_specification import UserRoleSpecification
from openapi_client.models.verification import Verification
# TODO: Rewrite to not use raise_errors
Answer.model_rebuild(raise_errors=False)

