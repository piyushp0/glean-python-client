# EditPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**Permissions**](Permissions.md) |  | 

## Example

```python
from openapi_client.models.edit_permissions_response import EditPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditPermissionsResponse from a JSON string
edit_permissions_response_instance = EditPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(EditPermissionsResponse.to_json())

# convert the object into a dict
edit_permissions_response_dict = edit_permissions_response_instance.to_dict()
# create an instance of EditPermissionsResponse from a dict
edit_permissions_response_from_dict = EditPermissionsResponse.from_dict(edit_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


