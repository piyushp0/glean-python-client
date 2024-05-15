# ObjectPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**write** | [**WritePermission**](WritePermission.md) |  | [optional] 

## Example

```python
from openapi_client.models.object_permissions import ObjectPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectPermissions from a JSON string
object_permissions_instance = ObjectPermissions.from_json(json)
# print the JSON string representation of the object
print(ObjectPermissions.to_json())

# convert the object into a dict
object_permissions_dict = object_permissions_instance.to_dict()
# create an instance of ObjectPermissions from a dict
object_permissions_from_dict = ObjectPermissions.from_dict(object_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


