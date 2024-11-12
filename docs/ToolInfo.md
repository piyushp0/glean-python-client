# ToolInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ToolMetadata**](ToolMetadata.md) |  | [optional] 
**parameters** | [**Dict[str, WriteActionParameter]**](WriteActionParameter.md) | Parameters supported by the tool. | [optional] 

## Example

```python
from openapi_client.models.tool_info import ToolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ToolInfo from a JSON string
tool_info_instance = ToolInfo.from_json(json)
# print the JSON string representation of the object
print(ToolInfo.to_json())

# convert the object into a dict
tool_info_dict = tool_info_instance.to_dict()
# create an instance of ToolInfo from a dict
tool_info_from_dict = ToolInfo.from_dict(tool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


