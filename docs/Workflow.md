# Workflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**name** | **str** | The name of the workflow. | [optional] 
**var_schema** | [**WorkflowSchema**](WorkflowSchema.md) |  | [optional] 
**application_id** | **str** | The Application Id the workflow should be created under. Empty for default assistant. | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of added user roles for the Workflow. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of removed user roles for the Workflow. | [optional] 
**fields** | [**List[WorkflowInputField]**](WorkflowInputField.md) | Use schema instead. | [optional] 
**steps** | [**List[WorkflowStep]**](WorkflowStep.md) | Use schema instead. | [optional] 
**author** | [**Person**](Person.md) |  | [optional] 
**create_timestamp** | **int** | Server Unix timestamp of the creation time. | [optional] 
**last_update_timestamp** | **int** | Server Unix timestamp of the last update time. | [optional] 
**last_updated_by** | [**Person**](Person.md) |  | [optional] 
**roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of roles for this prompt template explicitly granted. | [optional] 
**id** | **str** | The ID of the workflow. | [optional] 

## Example

```python
from openapi_client.models.workflow import Workflow

# TODO update the JSON string below
json = "{}"
# create an instance of Workflow from a JSON string
workflow_instance = Workflow.from_json(json)
# print the JSON string representation of the object
print(Workflow.to_json())

# convert the object into a dict
workflow_dict = workflow_instance.to_dict()
# create an instance of Workflow from a dict
workflow_from_dict = Workflow.from_dict(workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


