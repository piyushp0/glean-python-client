# GetShortcutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**error** | [**ShortcutError**](ShortcutError.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_shortcut_response import GetShortcutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetShortcutResponse from a JSON string
get_shortcut_response_instance = GetShortcutResponse.from_json(json)
# print the JSON string representation of the object
print(GetShortcutResponse.to_json())

# convert the object into a dict
get_shortcut_response_dict = get_shortcut_response_instance.to_dict()
# create an instance of GetShortcutResponse from a dict
get_shortcut_response_from_dict = GetShortcutResponse.from_dict(get_shortcut_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


