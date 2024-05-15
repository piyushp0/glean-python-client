# WritePermission

Describes the write permissions levels that a user has for a specific feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_type** | [**ScopeType**](ScopeType.md) |  | [optional] 
**create** | **bool** | True if user has create permission for this feature and scope | [optional] 
**update** | **bool** | True if user has update permission for this feature and scope | [optional] 
**delete** | **bool** | True if user has delete permission for this feature and scope | [optional] 

## Example

```python
from openapi_client.models.write_permission import WritePermission

# TODO update the JSON string below
json = "{}"
# create an instance of WritePermission from a JSON string
write_permission_instance = WritePermission.from_json(json)
# print the JSON string representation of the object
print(WritePermission.to_json())

# convert the object into a dict
write_permission_dict = write_permission_instance.to_dict()
# create an instance of WritePermission from a dict
write_permission_from_dict = WritePermission.from_dict(write_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


