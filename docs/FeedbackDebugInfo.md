# FeedbackDebugInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desktop_app_version** | **str** | The version of the desktop app from which the feedback was sent, if applicable | [optional] 

## Example

```python
from openapi_client.models.feedback_debug_info import FeedbackDebugInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackDebugInfo from a JSON string
feedback_debug_info_instance = FeedbackDebugInfo.from_json(json)
# print the JSON string representation of the object
print(FeedbackDebugInfo.to_json())

# convert the object into a dict
feedback_debug_info_dict = feedback_debug_info_instance.to_dict()
# create an instance of FeedbackDebugInfo from a dict
feedback_debug_info_from_dict = FeedbackDebugInfo.from_dict(feedback_debug_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


