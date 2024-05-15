# CustomEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**id** | **str** | Unique identifier. | [optional] 
**title** | **str** | Title or name of the custom entity. | [optional] 
**datasource** | **str** | The datasource the custom entity is from. | [optional] 
**object_type** | **str** | The type of the entity. Interpretation is specific to each datasource | [optional] 
**metadata** | [**CustomEntityMetadata**](CustomEntityMetadata.md) |  | [optional] 
**roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles for the custom entity explicitly granted by the owner. | [optional] 

## Example

```python
from openapi_client.models.custom_entity import CustomEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntity from a JSON string
custom_entity_instance = CustomEntity.from_json(json)
# print the JSON string representation of the object
print(CustomEntity.to_json())

# convert the object into a dict
custom_entity_dict = custom_entity_instance.to_dict()
# create an instance of CustomEntity from a dict
custom_entity_from_dict = CustomEntity.from_dict(custom_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


