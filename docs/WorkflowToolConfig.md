# WorkflowToolConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the action/tool being used. | [optional] 
**name** | **str** | The name of the tool being used. | [optional] 
**datasources_filter** | **List[str]** | Run this tool on only these datasource instance ids. | [optional] 
**input_template** | [**List[WorkflowToolParameter]**](WorkflowToolParameter.md) |  | [optional] 

## Example

```python
from openapi_client.models.workflow_tool_config import WorkflowToolConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowToolConfig from a JSON string
workflow_tool_config_instance = WorkflowToolConfig.from_json(json)
# print the JSON string representation of the object
print(WorkflowToolConfig.to_json())

# convert the object into a dict
workflow_tool_config_dict = workflow_tool_config_instance.to_dict()
# create an instance of WorkflowToolConfig from a dict
workflow_tool_config_from_dict = WorkflowToolConfig.from_dict(workflow_tool_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


