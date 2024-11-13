# WriteAction

A single action that can be executed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | The name of the tool. | [optional] 
**action_instance_id** | **str** | Identifier of the action instance. | [optional] 
**action_id** | **str** | Identifier of the action. | [optional] 
**action_pack_id** | **str** | Identifier of the action pack. | [optional] 
**tool_config** | [**ToolConfig**](ToolConfig.md) |  | [optional] 
**redirect_url** | **str** | If a &#x60;REDIRECT&#x60; action, the URL to visit to execute the action. | [optional] 
**parameters** | [**Dict[str, WriteActionParameter]**](WriteActionParameter.md) | The parameters to be passed to the redirect URL for actions. | [optional] 

## Example

```python
from openapi_client.models.write_action import WriteAction

# TODO update the JSON string below
json = "{}"
# create an instance of WriteAction from a JSON string
write_action_instance = WriteAction.from_json(json)
# print the JSON string representation of the object
print(WriteAction.to_json())

# convert the object into a dict
write_action_dict = write_action_instance.to_dict()
# create an instance of WriteAction from a dict
write_action_from_dict = WriteAction.from_dict(write_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


