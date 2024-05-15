# SeenFeedbackInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_explicit** | **bool** | The confidence of the user seeing the object is high because they explicitly interacted with it e.g. answer impression in SERP with additional user interaction. | [optional] 

## Example

```python
from openapi_client.models.seen_feedback_info import SeenFeedbackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SeenFeedbackInfo from a JSON string
seen_feedback_info_instance = SeenFeedbackInfo.from_json(json)
# print the JSON string representation of the object
print(SeenFeedbackInfo.to_json())

# convert the object into a dict
seen_feedback_info_dict = seen_feedback_info_instance.to_dict()
# create an instance of SeenFeedbackInfo from a dict
seen_feedback_info_from_dict = SeenFeedbackInfo.from_dict(seen_feedback_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


