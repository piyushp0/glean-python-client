# GetSimilarShortcutsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Link text following go/ prefix. | 

## Example

```python
from openapi_client.models.get_similar_shortcuts_request import GetSimilarShortcutsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimilarShortcutsRequest from a JSON string
get_similar_shortcuts_request_instance = GetSimilarShortcutsRequest.from_json(json)
# print the JSON string representation of the object
print(GetSimilarShortcutsRequest.to_json())

# convert the object into a dict
get_similar_shortcuts_request_dict = get_similar_shortcuts_request_instance.to_dict()
# create an instance of GetSimilarShortcutsRequest from a dict
get_similar_shortcuts_request_from_dict = GetSimilarShortcutsRequest.from_dict(get_similar_shortcuts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


