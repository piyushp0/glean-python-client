# Permissions

Describes the permissions levels that a user has for permissioned features. When the client sends this, Permissions.read and Permissions.write are the additional permissions granted to a user on top of what they have via their roles. When the server sends this, Permissions.read and Permissions.write are the complete (merged) set of permissions the user has, and Permissions.roles is just for display purposes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_admin_search** | **bool** | TODO--deprecate in favor of the read and write properties. True if the user has access to /adminsearch | [optional] 
**can_admin_client_api_global_tokens** | **bool** | TODO--deprecate in favor of the read and write properties. True if the user can administrate client API tokens with global scope | [optional] 
**can_dlp** | **bool** | TODO--deprecate in favor of the read and write properties. True if the user has access to data loss prevention (DLP) features | [optional] 
**read** | **Dict[str, List[ReadPermission]]** | Describes the read permission levels that a user has for permissioned features. Key must be PermissionedFeatureOrObject | [optional] 
**write** | **Dict[str, List[WritePermission]]** | Describes the write permissions levels that a user has for permissioned features. Key must be PermissionedFeatureOrObject | [optional] 
**grant** | **Dict[str, List[GrantPermission]]** | Describes the grant permission levels that a user has for permissioned features. Key must be PermissionedFeatureOrObject | [optional] 
**role** | **str** | The roleId of the canonical role a user has. The displayName is equal to the roleId. | [optional] 
**roles** | **List[str]** | The roleIds of the roles a user has. | [optional] 

## Example

```python
from openapi_client.models.permissions import Permissions

# TODO update the JSON string below
json = "{}"
# create an instance of Permissions from a JSON string
permissions_instance = Permissions.from_json(json)
# print the JSON string representation of the object
print(Permissions.to_json())

# convert the object into a dict
permissions_dict = permissions_instance.to_dict()
# create an instance of Permissions from a dict
permissions_from_dict = Permissions.from_dict(permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


