# CreateShortcutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShortcutMutableProperties**](ShortcutMutableProperties.md) |  | 

## Example

```python
from openapi_client.models.create_shortcut_request import CreateShortcutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShortcutRequest from a JSON string
create_shortcut_request_instance = CreateShortcutRequest.from_json(json)
# print the JSON string representation of the object
print(CreateShortcutRequest.to_json())

# convert the object into a dict
create_shortcut_request_dict = create_shortcut_request_instance.to_dict()
# create an instance of CreateShortcutRequest from a dict
create_shortcut_request_from_dict = CreateShortcutRequest.from_dict(create_shortcut_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


