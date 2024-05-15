# PermissionedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 

## Example

```python
from openapi_client.models.permissioned_object import PermissionedObject

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionedObject from a JSON string
permissioned_object_instance = PermissionedObject.from_json(json)
# print the JSON string representation of the object
print(PermissionedObject.to_json())

# convert the object into a dict
permissioned_object_dict = permissioned_object_instance.to_dict()
# create an instance of PermissionedObject from a dict
permissioned_object_from_dict = PermissionedObject.from_dict(permissioned_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


