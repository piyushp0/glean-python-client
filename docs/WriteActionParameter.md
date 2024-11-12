# WriteActionParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the value (e.g., integer, string, boolean, etc.) | [optional] 
**display_name** | **str** | Human readable display name for the key. | [optional] 
**value** | **str** | The value of the field. | [optional] 
**label** | **str** | User-friendly label associated with the value. | [optional] 
**is_required** | **bool** | Is the parameter a required field. | [optional] 
**description** | **str** | Description of the parameter. | [optional] 
**possible_values** | [**List[PossibleValue]**](PossibleValue.md) | Possible values that the parameter can take. | [optional] 

## Example

```python
from openapi_client.models.write_action_parameter import WriteActionParameter

# TODO update the JSON string below
json = "{}"
# create an instance of WriteActionParameter from a JSON string
write_action_parameter_instance = WriteActionParameter.from_json(json)
# print the JSON string representation of the object
print(WriteActionParameter.to_json())

# convert the object into a dict
write_action_parameter_dict = write_action_parameter_instance.to_dict()
# create an instance of WriteActionParameter from a dict
write_action_parameter_from_dict = WriteActionParameter.from_dict(write_action_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


