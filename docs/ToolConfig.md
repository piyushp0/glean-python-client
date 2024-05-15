# ToolConfig

Config for a specific tool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human understandable name of the tool. Max 50 characters. | [optional] 
**object_name** | **str** | Name of the generated object. This will be used to indicate to the end user what the generated object contains. | [optional] 
**logo_url** | **str** | URL used to fetch the logo. | [optional] 
**type** | **str** | Valid only for ACTION tools. Represents the type of action tool REDIRECT - The client renders the URL which contains information for carrying out the action. EXECUTION - Send a request to an external server and execute the action. | [optional] 

## Example

```python
from openapi_client.models.tool_config import ToolConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ToolConfig from a JSON string
tool_config_instance = ToolConfig.from_json(json)
# print the JSON string representation of the object
print(ToolConfig.to_json())

# convert the object into a dict
tool_config_dict = tool_config_instance.to_dict()
# create an instance of ToolConfig from a dict
tool_config_from_dict = ToolConfig.from_dict(tool_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


