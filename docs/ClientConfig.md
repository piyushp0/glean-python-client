# ClientConfig

Configuration settings for a specific client deployment that are not related to any particular datasource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant** | [**AssistantConfig**](AssistantConfig.md) |  | [optional] 
**tools** | [**ToolsConfig**](ToolsConfig.md) |  | [optional] 
**shortcuts** | [**ShortcutsConfig**](ShortcutsConfig.md) |  | [optional] 
**bad_versions** | **List[str]** | Known bad client versions that should force update themselves | [optional] 
**feed_people_celebrations_enabled** | **bool** | Whether people celebrations is enabled or not for the instance | [optional] 
**feed_suggested_enabled** | **bool** | Whether the suggested feed is enabled | [optional] 
**feed_trending_enabled** | **bool** | Whether the trending feed is enabled | [optional] 
**feed_recents_enabled** | **bool** | Whether the recents feed is enabled | [optional] 
**feed_mentions_enabled** | **bool** | Whether the mentions feed is enabled | [optional] 
**gpt_agent_enabled** | **bool** | Whether the GPT agent for Chat is enabled | [optional] 
**chat_history_enabled** | **bool** | Whether the chat history for Chat is enabled | [optional] 
**bool_values** | **Dict[str, bool]** | A map of {string, boolean} pairs representing flags that globally guard conditional features. Omitted flags mean the client should use its default state. | [optional] 
**integer_values** | **Dict[str, int]** | A map of {string, integer} pairs for client consumption. | [optional] 
**company_display_name** | **str** | The user-facing name of the company owning the deployment | [optional] 
**custom_serp_markdown** | **str** | A markdown string to be displayed on the search results page. Useful for outlinks to help pages. | [optional] 
**onboarding_query** | **str** | A demonstrative query to show during new user onboarding | [optional] 
**is_org_chart_link_visible** | **bool** | Determines whether the org chart link in the Directory panel is visible to all users. | [optional] 
**is_org_chart_accessible** | **bool** | Determines whether the org chart is accessible to all users, regardless of link visibility. Org chart can be accessible even if the org chart link in Directory is not visible. | [optional] 
**is_people_setup** | **bool** | Whether or not people data has been set up. | [optional] 
**is_pilot_mode** | **bool** | Whether or not the deployment is in pilot mode. | [optional] 
**web_app_url** | **str** | URL the company uses to access the web app | [optional] 
**user_outreach** | [**UserOutreachConfig**](UserOutreachConfig.md) |  | [optional] 
**search_link_url_template** | **str** | The URL to use for outbound links to Glean Search. Defaults to {webAppUrl}/search?q&#x3D;%s. | [optional] 
**chat_link_url_template** | **str** | The URL to use for outbound links to Glean Chat. Defaults to {webAppUrl}/chat. | [optional] 
**themes** | [**Themes**](Themes.md) |  | [optional] 
**brandings** | [**ClientConfigBrandings**](ClientConfigBrandings.md) |  | [optional] 
**greeting_format** | **str** | Describes how to format the web app greeting. Possible format options include \\%t - timely greeting \\%n - the user&#39;s first name | [optional] 
**task_see_all_label** | **str** | Label for the external link at the end of the Task card in order to guide user to the source. | [optional] 
**task_see_all_link** | **str** | Link used in conjunction with taskSeeAllLabel to redirect user to the task&#39;s source. | [optional] 
**search_placeholder** | **str** | Custom autocomplete box placeholder to replace rotating prompts | [optional] 
**shortcuts_prefix** | **str** | Company-wide custom prefix for Go Links. | [optional] 
**sso_company_provider** | **str** | SSO provider used by the company | [optional] 
**feedback_customizations** | [**FeedbackCustomizations**](FeedbackCustomizations.md) |  | [optional] 

## Example

```python
from openapi_client.models.client_config import ClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConfig from a JSON string
client_config_instance = ClientConfig.from_json(json)
# print the JSON string representation of the object
print(ClientConfig.to_json())

# convert the object into a dict
client_config_dict = client_config_instance.to_dict()
# create an instance of ClientConfig from a dict
client_config_from_dict = ClientConfig.from_dict(client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


