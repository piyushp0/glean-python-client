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
from openapi_client.models.assistant_config import AssistantConfig
from openapi_client.models.client_config_brandings import ClientConfigBrandings
from openapi_client.models.feedback_customizations import FeedbackCustomizations
from openapi_client.models.shortcuts_config import ShortcutsConfig
from openapi_client.models.themes import Themes
from openapi_client.models.tools_config import ToolsConfig
from openapi_client.models.user_outreach_config import UserOutreachConfig
from typing import Optional, Set
from typing_extensions import Self

class ClientConfig(BaseModel):
    """
    Configuration settings for a specific client deployment that are not related to any particular datasource
    """ # noqa: E501
    assistant: Optional[AssistantConfig] = None
    tools: Optional[ToolsConfig] = None
    shortcuts: Optional[ShortcutsConfig] = None
    bad_versions: Optional[List[StrictStr]] = Field(default=None, description="Known bad client versions that should force update themselves", alias="badVersions")
    feed_people_celebrations_enabled: Optional[StrictBool] = Field(default=None, description="Whether people celebrations is enabled or not for the instance", alias="feedPeopleCelebrationsEnabled")
    feed_suggested_enabled: Optional[StrictBool] = Field(default=None, description="Whether the suggested feed is enabled", alias="feedSuggestedEnabled")
    feed_trending_enabled: Optional[StrictBool] = Field(default=None, description="Whether the trending feed is enabled", alias="feedTrendingEnabled")
    feed_recents_enabled: Optional[StrictBool] = Field(default=None, description="Whether the recents feed is enabled", alias="feedRecentsEnabled")
    feed_mentions_enabled: Optional[StrictBool] = Field(default=None, description="Whether the mentions feed is enabled", alias="feedMentionsEnabled")
    gpt_agent_enabled: Optional[StrictBool] = Field(default=None, description="Whether the GPT agent for Chat is enabled", alias="gptAgentEnabled")
    chat_history_enabled: Optional[StrictBool] = Field(default=None, description="Whether the chat history for Chat is enabled", alias="chatHistoryEnabled")
    bool_values: Optional[Dict[str, StrictBool]] = Field(default=None, description="A map of {string, boolean} pairs representing flags that globally guard conditional features. Omitted flags mean the client should use its default state.", alias="boolValues")
    integer_values: Optional[Dict[str, StrictInt]] = Field(default=None, description="A map of {string, integer} pairs for client consumption.", alias="integerValues")
    company_display_name: Optional[StrictStr] = Field(default=None, description="The user-facing name of the company owning the deployment", alias="companyDisplayName")
    custom_serp_markdown: Optional[StrictStr] = Field(default=None, description="A markdown string to be displayed on the search results page. Useful for outlinks to help pages.", alias="customSerpMarkdown")
    onboarding_query: Optional[StrictStr] = Field(default=None, description="A demonstrative query to show during new user onboarding", alias="onboardingQuery")
    is_org_chart_link_visible: Optional[StrictBool] = Field(default=None, description="Determines whether the org chart link in the Directory panel is visible to all users.", alias="isOrgChartLinkVisible")
    is_org_chart_accessible: Optional[StrictBool] = Field(default=None, description="Determines whether the org chart is accessible to all users, regardless of link visibility. Org chart can be accessible even if the org chart link in Directory is not visible.", alias="isOrgChartAccessible")
    is_people_setup: Optional[StrictBool] = Field(default=None, description="Whether or not people data has been set up.", alias="isPeopleSetup")
    is_pilot_mode: Optional[StrictBool] = Field(default=None, description="Whether or not the deployment is in pilot mode.", alias="isPilotMode")
    web_app_url: Optional[StrictStr] = Field(default=None, description="URL the company uses to access the web app", alias="webAppUrl")
    user_outreach: Optional[UserOutreachConfig] = Field(default=None, alias="userOutreach")
    search_link_url_template: Optional[StrictStr] = Field(default=None, description="The URL to use for outbound links to Glean Search. Defaults to {webAppUrl}/search?q=%s.", alias="searchLinkUrlTemplate")
    chat_link_url_template: Optional[StrictStr] = Field(default=None, description="The URL to use for outbound links to Glean Chat. Defaults to {webAppUrl}/chat.", alias="chatLinkUrlTemplate")
    themes: Optional[Themes] = None
    brandings: Optional[ClientConfigBrandings] = None
    greeting_format: Optional[StrictStr] = Field(default=None, description="Describes how to format the web app greeting. Possible format options include \\%t - timely greeting \\%n - the user's first name", alias="greetingFormat")
    task_see_all_label: Optional[StrictStr] = Field(default=None, description="Label for the external link at the end of the Task card in order to guide user to the source.", alias="taskSeeAllLabel")
    task_see_all_link: Optional[StrictStr] = Field(default=None, description="Link used in conjunction with taskSeeAllLabel to redirect user to the task's source.", alias="taskSeeAllLink")
    shortcuts_prefix: Optional[StrictStr] = Field(default=None, description="Company-wide custom prefix for Go Links.", alias="shortcutsPrefix")
    sso_company_provider: Optional[StrictStr] = Field(default=None, description="SSO provider used by the company", alias="ssoCompanyProvider")
    feedback_customizations: Optional[FeedbackCustomizations] = Field(default=None, alias="feedbackCustomizations")
    __properties: ClassVar[List[str]] = ["assistant", "tools", "shortcuts", "badVersions", "feedPeopleCelebrationsEnabled", "feedSuggestedEnabled", "feedTrendingEnabled", "feedRecentsEnabled", "feedMentionsEnabled", "gptAgentEnabled", "chatHistoryEnabled", "boolValues", "integerValues", "companyDisplayName", "customSerpMarkdown", "onboardingQuery", "isOrgChartLinkVisible", "isOrgChartAccessible", "isPeopleSetup", "isPilotMode", "webAppUrl", "userOutreach", "searchLinkUrlTemplate", "chatLinkUrlTemplate", "themes", "brandings", "greetingFormat", "taskSeeAllLabel", "taskSeeAllLink", "shortcutsPrefix", "ssoCompanyProvider", "feedbackCustomizations"]

    @field_validator('sso_company_provider')
    def sso_company_provider_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gsuite', 'iap', 'okta', 'ping', 'azure', 'onelogin', 'onelogin_saml']):
            raise ValueError("must be one of enum values ('gsuite', 'iap', 'okta', 'ping', 'azure', 'onelogin', 'onelogin_saml')")
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
        """Create an instance of ClientConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of assistant
        if self.assistant:
            _dict['assistant'] = self.assistant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tools
        if self.tools:
            _dict['tools'] = self.tools.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shortcuts
        if self.shortcuts:
            _dict['shortcuts'] = self.shortcuts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_outreach
        if self.user_outreach:
            _dict['userOutreach'] = self.user_outreach.to_dict()
        # override the default output from pydantic by calling `to_dict()` of themes
        if self.themes:
            _dict['themes'] = self.themes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of brandings
        if self.brandings:
            _dict['brandings'] = self.brandings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feedback_customizations
        if self.feedback_customizations:
            _dict['feedbackCustomizations'] = self.feedback_customizations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assistant": AssistantConfig.from_dict(obj["assistant"]) if obj.get("assistant") is not None else None,
            "tools": ToolsConfig.from_dict(obj["tools"]) if obj.get("tools") is not None else None,
            "shortcuts": ShortcutsConfig.from_dict(obj["shortcuts"]) if obj.get("shortcuts") is not None else None,
            "badVersions": obj.get("badVersions"),
            "feedPeopleCelebrationsEnabled": obj.get("feedPeopleCelebrationsEnabled"),
            "feedSuggestedEnabled": obj.get("feedSuggestedEnabled"),
            "feedTrendingEnabled": obj.get("feedTrendingEnabled"),
            "feedRecentsEnabled": obj.get("feedRecentsEnabled"),
            "feedMentionsEnabled": obj.get("feedMentionsEnabled"),
            "gptAgentEnabled": obj.get("gptAgentEnabled"),
            "chatHistoryEnabled": obj.get("chatHistoryEnabled"),
            "boolValues": obj.get("boolValues"),
            "integerValues": obj.get("integerValues"),
            "companyDisplayName": obj.get("companyDisplayName"),
            "customSerpMarkdown": obj.get("customSerpMarkdown"),
            "onboardingQuery": obj.get("onboardingQuery"),
            "isOrgChartLinkVisible": obj.get("isOrgChartLinkVisible"),
            "isOrgChartAccessible": obj.get("isOrgChartAccessible"),
            "isPeopleSetup": obj.get("isPeopleSetup"),
            "isPilotMode": obj.get("isPilotMode"),
            "webAppUrl": obj.get("webAppUrl"),
            "userOutreach": UserOutreachConfig.from_dict(obj["userOutreach"]) if obj.get("userOutreach") is not None else None,
            "searchLinkUrlTemplate": obj.get("searchLinkUrlTemplate"),
            "chatLinkUrlTemplate": obj.get("chatLinkUrlTemplate"),
            "themes": Themes.from_dict(obj["themes"]) if obj.get("themes") is not None else None,
            "brandings": ClientConfigBrandings.from_dict(obj["brandings"]) if obj.get("brandings") is not None else None,
            "greetingFormat": obj.get("greetingFormat"),
            "taskSeeAllLabel": obj.get("taskSeeAllLabel"),
            "taskSeeAllLink": obj.get("taskSeeAllLink"),
            "shortcutsPrefix": obj.get("shortcutsPrefix"),
            "ssoCompanyProvider": obj.get("ssoCompanyProvider"),
            "feedbackCustomizations": FeedbackCustomizations.from_dict(obj["feedbackCustomizations"]) if obj.get("feedbackCustomizations") is not None else None
        })
        return _obj


