# WorkflowMutableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workflow. | [optional] 
**var_schema** | [**WorkflowSchema**](WorkflowSchema.md) |  | [optional] 
**application_id** | **str** | The Application Id the workflow should be created under. Empty for default assistant. | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of added user roles for the Workflow. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of removed user roles for the Workflow. | [optional] 
**fields** | [**List[WorkflowInputField]**](WorkflowInputField.md) | Use schema instead. | [optional] 
**steps** | [**List[WorkflowStep]**](WorkflowStep.md) | Use schema instead. | [optional] 

## Example

```python
from openapi_client.models.workflow_mutable_properties import WorkflowMutableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowMutableProperties from a JSON string
workflow_mutable_properties_instance = WorkflowMutableProperties.from_json(json)
# print the JSON string representation of the object
print(WorkflowMutableProperties.to_json())

# convert the object into a dict
workflow_mutable_properties_dict = workflow_mutable_properties_instance.to_dict()
# create an instance of WorkflowMutableProperties from a dict
workflow_mutable_properties_from_dict = WorkflowMutableProperties.from_dict(workflow_mutable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


