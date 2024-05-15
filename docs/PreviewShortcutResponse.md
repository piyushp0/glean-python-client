# PreviewShortcutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**existing_url_shortcuts** | [**List[Shortcut]**](Shortcut.md) | Exising shortcuts that have a similar destination URL. | [optional] 
**error** | [**ShortcutError**](ShortcutError.md) |  | [optional] 

## Example

```python
from openapi_client.models.preview_shortcut_response import PreviewShortcutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewShortcutResponse from a JSON string
preview_shortcut_response_instance = PreviewShortcutResponse.from_json(json)
# print the JSON string representation of the object
print(PreviewShortcutResponse.to_json())

# convert the object into a dict
preview_shortcut_response_dict = preview_shortcut_response_instance.to_dict()
# create an instance of PreviewShortcutResponse from a dict
preview_shortcut_response_from_dict = PreviewShortcutResponse.from_dict(preview_shortcut_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


