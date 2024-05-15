# CreateShortcutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**error** | [**ShortcutError**](ShortcutError.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_shortcut_response import CreateShortcutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShortcutResponse from a JSON string
create_shortcut_response_instance = CreateShortcutResponse.from_json(json)
# print the JSON string representation of the object
print(CreateShortcutResponse.to_json())

# convert the object into a dict
create_shortcut_response_dict = create_shortcut_response_instance.to_dict()
# create an instance of CreateShortcutResponse from a dict
create_shortcut_response_from_dict = CreateShortcutResponse.from_dict(create_shortcut_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


