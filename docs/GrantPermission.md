# GrantPermission

Describes the grant permission level that a user has for a specific feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_type** | [**ScopeType**](ScopeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.grant_permission import GrantPermission

# TODO update the JSON string below
json = "{}"
# create an instance of GrantPermission from a JSON string
grant_permission_instance = GrantPermission.from_json(json)
# print the JSON string representation of the object
print(GrantPermission.to_json())

# convert the object into a dict
grant_permission_dict = grant_permission_instance.to_dict()
# create an instance of GrantPermission from a dict
grant_permission_from_dict = GrantPermission.from_dict(grant_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


