# WorkflowToolParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** | Templatic inputs to the tool where params can be either user input fields or step ids. | 
**name** | **str** | tool input field name which is optional. | [optional] 

## Example

```python
from openapi_client.models.workflow_tool_parameter import WorkflowToolParameter

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowToolParameter from a JSON string
workflow_tool_parameter_instance = WorkflowToolParameter.from_json(json)
# print the JSON string representation of the object
print(WorkflowToolParameter.to_json())

# convert the object into a dict
workflow_tool_parameter_dict = workflow_tool_parameter_instance.to_dict()
# create an instance of WorkflowToolParameter from a dict
workflow_tool_parameter_from_dict = WorkflowToolParameter.from_dict(workflow_tool_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


