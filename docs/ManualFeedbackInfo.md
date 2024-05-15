# ManualFeedbackInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address of the user who submitted the Feedback.event.MANUAL_FEEDBACK event. | [optional] 
**source** | **str** | The source associated with the Feedback.event.MANUAL_FEEDBACK event. | [optional] 
**issue** | **str** | The issue the user indicated in the feedback. | [optional] 
**query** | **str** | The query associated with the Feedback.event.MANUAL_FEEDBACK event. | [optional] 
**obscured_query** | **str** | The query associated with the Feedback.event.MANUAL_FEEDBACK event, but obscured such that the vowels are replaced with special characters. For search feedback events only. | [optional] 
**active_tab** | **str** | Which tabs the user had chosen at the time of the Feedback.event.MANUAL_FEEDBACK event. For search feedback events only. | [optional] 
**comments** | **str** | The comments users can optionally add to the Feedback.event.MANUAL_FEEDBACK events. | [optional] 
**search_results** | **List[str]** | The array of search result Glean Document IDs, ordered by top to bottom result. | [optional] 
**previous_messages** | **List[str]** | The array of previous messages in a chat session, ordered by oldest to newest. | [optional] 
**num_queries_from_first_run** | **int** | How many times this query has been run in the past. | [optional] 
**vote** | **str** | The vote associated with the Feedback.event.MANUAL_FEEDBACK event. | [optional] 
**rating** | **int** | A rating associated with the user feedback. The value will be between one and the maximum given by ratingScale, inclusive. | [optional] 
**rating_key** | **str** | A description of the rating that contextualizes how it appeared to the user, e.g. \&quot;satisfied\&quot;. | [optional] 
**rating_scale** | **int** | The scale of comparison for a rating associated with the feedback. Rating values start from one and go up to the maximum specified by ratingScale. For example, a five-option satisfaction rating will have a ratingScale of 5 and a thumbs-up/thumbs-down rating will have a ratingScale of 2. | [optional] 

## Example

```python
from openapi_client.models.manual_feedback_info import ManualFeedbackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManualFeedbackInfo from a JSON string
manual_feedback_info_instance = ManualFeedbackInfo.from_json(json)
# print the JSON string representation of the object
print(ManualFeedbackInfo.to_json())

# convert the object into a dict
manual_feedback_info_dict = manual_feedback_info_instance.to_dict()
# create an instance of ManualFeedbackInfo from a dict
manual_feedback_info_from_dict = ManualFeedbackInfo.from_dict(manual_feedback_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


