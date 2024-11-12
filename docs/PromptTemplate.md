# PromptTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-given identifier for this prompt template. | [optional] 
**template** | **str** | The actual template string. | 
**application_id** | **str** | The Application Id the prompt template should be created under. Empty for default assistant. | [optional] 
**inclusions** | [**ChatRestrictionFilters**](ChatRestrictionFilters.md) |  | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of added user roles for the Workflow. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of removed user roles for the Workflow. | [optional] 
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**id** | **str** | Opaque id for this prompt template | [optional] 
**author** | [**Person**](Person.md) |  | [optional] 
**create_timestamp** | **int** | Server Unix timestamp of the creation time. | [optional] 
**last_update_timestamp** | **int** | Server Unix timestamp of the last update time. | [optional] 
**last_updated_by** | [**Person**](Person.md) |  | [optional] 
**roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of roles for this prompt template explicitly granted. | [optional] 

## Example

```python
from openapi_client.models.prompt_template import PromptTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PromptTemplate from a JSON string
prompt_template_instance = PromptTemplate.from_json(json)
# print the JSON string representation of the object
print(PromptTemplate.to_json())

# convert the object into a dict
prompt_template_dict = prompt_template_instance.to_dict()
# create an instance of PromptTemplate from a dict
prompt_template_from_dict = PromptTemplate.from_dict(prompt_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


