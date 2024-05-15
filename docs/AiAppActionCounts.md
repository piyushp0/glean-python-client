# AiAppActionCounts

Map from action to frequency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_slackbot_responses** | **int** | Total number of Slackbot responses, both proactive and reactive. | [optional] 
**total_slackbot_responses_shared** | **int** | Total number of Slackbot responses shared publicly (upvoted). | [optional] 
**total_slackbot_responses_not_helpful** | **int** | Total number of Slackbot responses rejected as not helpful (downvoted). | [optional] 
**total_chat_messages** | **int** | Total number of Chat messages sent in requested period. | [optional] 
**total_upvotes** | **int** | Total number of Chat messages which received upvotes by the user. | [optional] 
**total_downvotes** | **int** | Total number of Chat messages which received downvotes by the user. | [optional] 

## Example

```python
from openapi_client.models.ai_app_action_counts import AiAppActionCounts

# TODO update the JSON string below
json = "{}"
# create an instance of AiAppActionCounts from a JSON string
ai_app_action_counts_instance = AiAppActionCounts.from_json(json)
# print the JSON string representation of the object
print(AiAppActionCounts.to_json())

# convert the object into a dict
ai_app_action_counts_dict = ai_app_action_counts_instance.to_dict()
# create an instance of AiAppActionCounts from a dict
ai_app_action_counts_from_dict = AiAppActionCounts.from_dict(ai_app_action_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


