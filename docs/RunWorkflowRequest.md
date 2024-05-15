# RunWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The ID of the workflow to be triggered. | 
**fields** | **Dict[str, str]** | Key-value mapping of string -&gt; string where the key is the name of the field in the prompt. | [optional] 

## Example

```python
from openapi_client.models.run_workflow_request import RunWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunWorkflowRequest from a JSON string
run_workflow_request_instance = RunWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(RunWorkflowRequest.to_json())

# convert the object into a dict
run_workflow_request_dict = run_workflow_request_instance.to_dict()
# create an instance of RunWorkflowRequest from a dict
run_workflow_request_from_dict = RunWorkflowRequest.from_dict(run_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


