# PromptTemplateMutableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-given identifier for this prompt template. | [optional] 
**template** | **str** | The actual template string. | 
**application_id** | **str** | The Application Id the prompt template should be created under. Empty for default assistant. | [optional] 
**inclusions** | [**ChatRestrictionFilters**](ChatRestrictionFilters.md) |  | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of added user roles for the Workflow. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of removed user roles for the Workflow. | [optional] 

## Example

```python
from openapi_client.models.prompt_template_mutable_properties import PromptTemplateMutableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PromptTemplateMutableProperties from a JSON string
prompt_template_mutable_properties_instance = PromptTemplateMutableProperties.from_json(json)
# print the JSON string representation of the object
print(PromptTemplateMutableProperties.to_json())

# convert the object into a dict
prompt_template_mutable_properties_dict = prompt_template_mutable_properties_instance.to_dict()
# create an instance of PromptTemplateMutableProperties from a dict
prompt_template_mutable_properties_from_dict = PromptTemplateMutableProperties.from_dict(prompt_template_mutable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


