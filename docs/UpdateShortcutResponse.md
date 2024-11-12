# UpdateShortcutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**error** | [**ShortcutError**](ShortcutError.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_shortcut_response import UpdateShortcutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShortcutResponse from a JSON string
update_shortcut_response_instance = UpdateShortcutResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateShortcutResponse.to_json())

# convert the object into a dict
update_shortcut_response_dict = update_shortcut_response_instance.to_dict()
# create an instance of UpdateShortcutResponse from a dict
update_shortcut_response_from_dict = UpdateShortcutResponse.from_dict(update_shortcut_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


