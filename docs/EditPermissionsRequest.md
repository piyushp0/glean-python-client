# EditPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | The ids of the users whose permissions will be edited | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | 

## Example

```python
from openapi_client.models.edit_permissions_request import EditPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditPermissionsRequest from a JSON string
edit_permissions_request_instance = EditPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(EditPermissionsRequest.to_json())

# convert the object into a dict
edit_permissions_request_dict = edit_permissions_request_instance.to_dict()
# create an instance of EditPermissionsRequest from a dict
edit_permissions_request_from_dict = EditPermissionsRequest.from_dict(edit_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


