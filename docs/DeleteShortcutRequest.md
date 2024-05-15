# DeleteShortcutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque id of the user generated content. | 

## Example

```python
from openapi_client.models.delete_shortcut_request import DeleteShortcutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteShortcutRequest from a JSON string
delete_shortcut_request_instance = DeleteShortcutRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteShortcutRequest.to_json())

# convert the object into a dict
delete_shortcut_request_dict = delete_shortcut_request_instance.to_dict()
# create an instance of DeleteShortcutRequest from a dict
delete_shortcut_request_from_dict = DeleteShortcutRequest.from_dict(delete_shortcut_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


