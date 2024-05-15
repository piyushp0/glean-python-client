# ToolsConfig

Configuration settings related to Tools.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_tools** | [**List[ToolMetadata]**](ToolMetadata.md) | List of tools available to the user. | [optional] 

## Example

```python
from openapi_client.models.tools_config import ToolsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsConfig from a JSON string
tools_config_instance = ToolsConfig.from_json(json)
# print the JSON string representation of the object
print(ToolsConfig.to_json())

# convert the object into a dict
tools_config_dict = tools_config_instance.to_dict()
# create an instance of ToolsConfig from a dict
tools_config_from_dict = ToolsConfig.from_dict(tools_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


