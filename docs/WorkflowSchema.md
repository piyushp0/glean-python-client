# WorkflowSchema

The schema of a workflow, such as the goal and the steps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | **str** | The goal of the workflow. This is passed into each step. | [optional] 
**steps** | [**List[WorkflowStep]**](WorkflowStep.md) |  | 
**fields** | [**List[WorkflowInputField]**](WorkflowInputField.md) | Fields can be used in the goal, step instruction templates, and tool config input templates. | [optional] 

## Example

```python
from openapi_client.models.workflow_schema import WorkflowSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSchema from a JSON string
workflow_schema_instance = WorkflowSchema.from_json(json)
# print the JSON string representation of the object
print(WorkflowSchema.to_json())

# convert the object into a dict
workflow_schema_dict = workflow_schema_instance.to_dict()
# create an instance of WorkflowSchema from a dict
workflow_schema_from_dict = WorkflowSchema.from_dict(workflow_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


