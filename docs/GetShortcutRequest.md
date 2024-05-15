# GetShortcutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque id of the user generated content. | [optional] 
**alias** | **str** | The alias for the shortcut, including any arguments for variable shortcuts. | 

## Example

```python
from openapi_client.models.get_shortcut_request import GetShortcutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetShortcutRequest from a JSON string
get_shortcut_request_instance = GetShortcutRequest.from_json(json)
# print the JSON string representation of the object
print(GetShortcutRequest.to_json())

# convert the object into a dict
get_shortcut_request_dict = get_shortcut_request_instance.to_dict()
# create an instance of GetShortcutRequest from a dict
get_shortcut_request_from_dict = GetShortcutRequest.from_dict(get_shortcut_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


