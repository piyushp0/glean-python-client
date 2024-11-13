# AssistantConfig

Configuration settings specific to Assistant features

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_banner_text** | **str** | Disclaimer message to be displayed as a banner on top of chat. This could be in markdown format with \&quot;\\n\&quot; between each line. | [optional] 
**chat_box_disclaimer** | **str** | Disclaimer message to be displayed below the chat box. This could be in markdown format. | [optional] 
**chat_link_url_template** | **str** | The URL to use for outbound links to Glean Chat. Defaults to {webAppUrl}/chat. | [optional] 
**chat_starter_header** | **str** | Label for the chat header during initial state. | [optional] 
**chat_starter_subheader** | **str** | Label for the chat subheader during initial state. | [optional] 
**agent_client_configs** | [**List[AgentClientConfig]**](AgentClientConfig.md) |  | [optional] 
**redlisted_datasources** | **List[str]** | A list of datasources that are disabled in Chat | [optional] 
**greenlisted_datasource_instances** | **List[str]** | A list of datasources that are always visible in Chat | [optional] 
**gpt_agent_enabled** | **bool** | Whether the GPT agent (general mode) for Chat is enabled | [optional] 
**file_upload** | [**FileUploadConfig**](FileUploadConfig.md) |  | [optional] 
**chat_history_enabled** | **bool** | Whether the chat history for Chat is enabled for the deployment | [optional] 
**chat_guide_url** | **str** | Redirect URL for \&quot;Chat guide\&quot; in the default chat starter subheader | [optional] 
**prompts_enabled** | **bool** | Whether prompt templates feature are enabled for the deployment. | [optional] 
**default_user_can_share_prompts** | **bool** | Whether a default user can share prompts to the prompt library. | [optional] 
**file_upload_enabled** | **bool** | Whether file upload for Chat is enabled for the deployment | [optional] 

## Example

```python
from openapi_client.models.assistant_config import AssistantConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AssistantConfig from a JSON string
assistant_config_instance = AssistantConfig.from_json(json)
# print the JSON string representation of the object
print(AssistantConfig.to_json())

# convert the object into a dict
assistant_config_dict = assistant_config_instance.to_dict()
# create an instance of AssistantConfig from a dict
assistant_config_from_dict = AssistantConfig.from_dict(assistant_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


