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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.agent_client_config import AgentClientConfig
from openapi_client.models.file_upload_config import FileUploadConfig
from typing import Optional, Set
from typing_extensions import Self

class AssistantConfig(BaseModel):
    """
    Configuration settings specific to Assistant features
    """ # noqa: E501
    chat_banner_text: Optional[StrictStr] = Field(default=None, description="Disclaimer message to be displayed as a banner on top of chat. This could be in markdown format with \"\\n\" between each line.", alias="chatBannerText")
    chat_box_disclaimer: Optional[StrictStr] = Field(default=None, description="Disclaimer message to be displayed below the chat box. This could be in markdown format.", alias="chatBoxDisclaimer")
    chat_link_url_template: Optional[StrictStr] = Field(default=None, description="The URL to use for outbound links to Glean Chat. Defaults to {webAppUrl}/chat.", alias="chatLinkUrlTemplate")
    chat_starter_header: Optional[StrictStr] = Field(default=None, description="Label for the chat header during initial state.", alias="chatStarterHeader")
    chat_starter_subheader: Optional[StrictStr] = Field(default=None, description="Label for the chat subheader during initial state.", alias="chatStarterSubheader")
    agent_client_configs: Optional[List[AgentClientConfig]] = Field(default=None, alias="agentClientConfigs")
    redlisted_datasources: Optional[List[StrictStr]] = Field(default=None, description="A list of datasources that are disabled in Chat", alias="redlistedDatasources")
    greenlisted_datasource_instances: Optional[List[StrictStr]] = Field(default=None, description="A list of datasources that are always visible in Chat", alias="greenlistedDatasourceInstances")
    gpt_agent_enabled: Optional[StrictBool] = Field(default=None, description="Whether the GPT agent (general mode) for Chat is enabled", alias="gptAgentEnabled")
    file_upload: Optional[FileUploadConfig] = Field(default=None, alias="fileUpload")
    chat_history_enabled: Optional[StrictBool] = Field(default=None, description="Whether the chat history for Chat is enabled for the deployment", alias="chatHistoryEnabled")
    chat_guide_url: Optional[StrictStr] = Field(default=None, description="Redirect URL for \"Chat guide\" in the default chat starter subheader", alias="chatGuideUrl")
    prompts_enabled: Optional[StrictBool] = Field(default=None, description="Whether prompt templates feature are enabled for the deployment.", alias="promptsEnabled")
    default_user_can_share_prompts: Optional[StrictBool] = Field(default=None, description="Whether a default user can share prompts to the prompt library.", alias="defaultUserCanSharePrompts")
    file_upload_enabled: Optional[StrictBool] = Field(default=None, description="Whether file upload for Chat is enabled for the deployment", alias="fileUploadEnabled")
    __properties: ClassVar[List[str]] = ["chatBannerText", "chatBoxDisclaimer", "chatLinkUrlTemplate", "chatStarterHeader", "chatStarterSubheader", "agentClientConfigs", "redlistedDatasources", "greenlistedDatasourceInstances", "gptAgentEnabled", "fileUpload", "chatHistoryEnabled", "chatGuideUrl", "promptsEnabled", "defaultUserCanSharePrompts", "fileUploadEnabled"]

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
        """Create an instance of AssistantConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in agent_client_configs (list)
        _items = []
        if self.agent_client_configs:
            for _item_agent_client_configs in self.agent_client_configs:
                if _item_agent_client_configs:
                    _items.append(_item_agent_client_configs.to_dict())
            _dict['agentClientConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of file_upload
        if self.file_upload:
            _dict['fileUpload'] = self.file_upload.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssistantConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chatBannerText": obj.get("chatBannerText"),
            "chatBoxDisclaimer": obj.get("chatBoxDisclaimer"),
            "chatLinkUrlTemplate": obj.get("chatLinkUrlTemplate"),
            "chatStarterHeader": obj.get("chatStarterHeader"),
            "chatStarterSubheader": obj.get("chatStarterSubheader"),
            "agentClientConfigs": [AgentClientConfig.from_dict(_item) for _item in obj["agentClientConfigs"]] if obj.get("agentClientConfigs") is not None else None,
            "redlistedDatasources": obj.get("redlistedDatasources"),
            "greenlistedDatasourceInstances": obj.get("greenlistedDatasourceInstances"),
            "gptAgentEnabled": obj.get("gptAgentEnabled"),
            "fileUpload": FileUploadConfig.from_dict(obj["fileUpload"]) if obj.get("fileUpload") is not None else None,
            "chatHistoryEnabled": obj.get("chatHistoryEnabled"),
            "chatGuideUrl": obj.get("chatGuideUrl"),
            "promptsEnabled": obj.get("promptsEnabled"),
            "defaultUserCanSharePrompts": obj.get("defaultUserCanSharePrompts"),
            "fileUploadEnabled": obj.get("fileUploadEnabled")
        })
        return _obj


