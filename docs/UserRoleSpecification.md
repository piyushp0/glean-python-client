# UserRoleSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_document_spec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**role** | [**UserRole**](UserRole.md) |  | 

## Example

```python
from openapi_client.models.user_role_specification import UserRoleSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleSpecification from a JSON string
user_role_specification_instance = UserRoleSpecification.from_json(json)
# print the JSON string representation of the object
print(UserRoleSpecification.to_json())

# convert the object into a dict
user_role_specification_dict = user_role_specification_instance.to_dict()
# create an instance of UserRoleSpecification from a dict
user_role_specification_from_dict = UserRoleSpecification.from_dict(user_role_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


