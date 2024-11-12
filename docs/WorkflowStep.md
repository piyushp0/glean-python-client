# WorkflowStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of this step in the workflow. | [optional] 
**instruction_template** | **str** | The templatic input to the workflow step. | [optional] 
**tool_config** | [**List[WorkflowToolConfig]**](WorkflowToolConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.workflow_step import WorkflowStep

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStep from a JSON string
workflow_step_instance = WorkflowStep.from_json(json)
# print the JSON string representation of the object
print(WorkflowStep.to_json())

# convert the object into a dict
workflow_step_dict = workflow_step_instance.to_dict()
# create an instance of WorkflowStep from a dict
workflow_step_from_dict = WorkflowStep.from_dict(workflow_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


