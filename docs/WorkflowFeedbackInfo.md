# WorkflowFeedbackInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Where the feedback of the workflow originated from | [optional] 

## Example

```python
from openapi_client.models.workflow_feedback_info import WorkflowFeedbackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowFeedbackInfo from a JSON string
workflow_feedback_info_instance = WorkflowFeedbackInfo.from_json(json)
# print the JSON string representation of the object
print(WorkflowFeedbackInfo.to_json())

# convert the object into a dict
workflow_feedback_info_dict = workflow_feedback_info_instance.to_dict()
# create an instance of WorkflowFeedbackInfo from a dict
workflow_feedback_info_from_dict = WorkflowFeedbackInfo.from_dict(workflow_feedback_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


