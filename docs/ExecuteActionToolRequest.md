# ExecuteActionToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tool. | 
**parameters** | [**Dict[str, WriteActionParameter]**](WriteActionParameter.md) | The parameters to be passed to the tool for action. | [optional] 

## Example

```python
from openapi_client.models.execute_action_tool_request import ExecuteActionToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionToolRequest from a JSON string
execute_action_tool_request_instance = ExecuteActionToolRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteActionToolRequest.to_json())

# convert the object into a dict
execute_action_tool_request_dict = execute_action_tool_request_instance.to_dict()
# create an instance of ExecuteActionToolRequest from a dict
execute_action_tool_request_from_dict = ExecuteActionToolRequest.from_dict(execute_action_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


