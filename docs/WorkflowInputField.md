# WorkflowInputField

Input field argument of a workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the input. | [optional] 
**display_name** | **str** | Name of the field as displayed to the user. | [optional] 
**description** | **str** | Description of the field. | [optional] 

## Example

```python
from openapi_client.models.workflow_input_field import WorkflowInputField

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowInputField from a JSON string
workflow_input_field_instance = WorkflowInputField.from_json(json)
# print the JSON string representation of the object
print(WorkflowInputField.to_json())

# convert the object into a dict
workflow_input_field_dict = workflow_input_field_instance.to_dict()
# create an instance of WorkflowInputField from a dict
workflow_input_field_from_dict = WorkflowInputField.from_dict(workflow_input_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


