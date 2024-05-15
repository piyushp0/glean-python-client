# ReadPermission

Describes the read permission level that a user has for a specific feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_type** | [**ScopeType**](ScopeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_permission import ReadPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ReadPermission from a JSON string
read_permission_instance = ReadPermission.from_json(json)
# print the JSON string representation of the object
print(ReadPermission.to_json())

# convert the object into a dict
read_permission_dict = read_permission_instance.to_dict()
# create an instance of ReadPermission from a dict
read_permission_from_dict = ReadPermission.from_dict(read_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


