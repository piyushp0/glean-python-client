# AiInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_log_timestamp** | **int** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**assistant_insights** | [**List[UserActivityInsight]**](UserActivityInsight.md) |  | [optional] 
**total_active_assistant_users** | **int** | Total number of Active Assistant users (chat, summary, AIA) in requested period. | [optional] 
**total_chat_messages** | **int** | Total number of Chat messages sent in requested period. | [optional] 
**total_ai_summarizations** | **int** | Total number of AI Document Summarizations invoked in the requested period. | [optional] 
**total_ai_answers** | **int** | Total number of AI Answers generated in the requested period. | [optional] 
**total_upvotes** | **int** | Total number of Chat messages which received upvotes by the user. | [optional] 
**total_downvotes** | **int** | Total number of Chat messages which received downvotes by the user. | [optional] 
**total_gleanbot_responses** | **int** | Total number of Gleanbot responses, both proactive and reactive. | [optional] 
**total_gleanbot_responses_shared** | **int** | Total number of Gleanbot responses shared publicly (upvoted). | [optional] 
**total_gleanbot_responses_not_helpful** | **int** | Total number of Glean responses rejected as not helpful (downvoted). | [optional] 
**departments** | **List[str]** | list of departments applicable for users tab. | [optional] 

## Example

```python
from openapi_client.models.ai_insights_response import AiInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiInsightsResponse from a JSON string
ai_insights_response_instance = AiInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(AiInsightsResponse.to_json())

# convert the object into a dict
ai_insights_response_dict = ai_insights_response_instance.to_dict()
# create an instance of AiInsightsResponse from a dict
ai_insights_response_from_dict = AiInsightsResponse.from_dict(ai_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


