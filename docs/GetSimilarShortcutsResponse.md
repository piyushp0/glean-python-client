# GetSimilarShortcutsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortcuts** | [**List[Shortcut]**](Shortcut.md) | Shortcuts with similar aliases to the given. Includes shortcut with the exact alias if it exists. | 

## Example

```python
from openapi_client.models.get_similar_shortcuts_response import GetSimilarShortcutsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimilarShortcutsResponse from a JSON string
get_similar_shortcuts_response_instance = GetSimilarShortcutsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSimilarShortcutsResponse.to_json())

# convert the object into a dict
get_similar_shortcuts_response_dict = get_similar_shortcuts_response_instance.to_dict()
# create an instance of GetSimilarShortcutsResponse from a dict
get_similar_shortcuts_response_from_dict = GetSimilarShortcutsResponse.from_dict(get_similar_shortcuts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


