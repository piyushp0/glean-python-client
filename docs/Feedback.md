# Feedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Universally unique identifier of the event. To allow for reliable retransmission, only the earliest received event of a given UUID is considered valid by the server and subsequent are ignored. | [optional] 
**category** | **str** | The feature category to which the feedback applies. These should be broad product areas such as Announcements, Answers, Search, etc. rather than specific components or UI treatments within those areas. | [optional] 
**tracking_tokens** | **List[str]** | A list of server-generated trackingTokens to which this event applies. | 
**event** | **str** | The action the user took within a Glean client with respect to the object referred to by the given &#x60;trackingToken&#x60;. | 
**position** | **int** | Position of the element in the case that the client controls order (such as feed and autocomplete). | [optional] 
**payload** | **str** | For type MANUAL_FEEDBACK, contains string of user feedback. For autocomplete, partial query string. For feed, string of user feedback in addition to manual feedback signals extracted from all suggested content. | [optional] 
**session_info** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**timestamp** | **datetime** | The ISO 8601 timestamp when the event occured. | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**pathname** | **str** | The path the client was at when the feedback event triggered. | [optional] 
**channels** | **List[str]** | Where the feedback will be sent, e.g. to Glean, the user&#39;s company, or both. If no channels are specified, feedback will go only to Glean. | [optional] 
**url** | **str** | The URL the client was at when the feedback event triggered. | [optional] 
**ui_element** | **str** | The UI element associated with the event, if any. | [optional] 
**manual_feedback_info** | [**ManualFeedbackInfo**](ManualFeedbackInfo.md) |  | [optional] 
**seen_feedback_info** | [**SeenFeedbackInfo**](SeenFeedbackInfo.md) |  | [optional] 
**user_view_info** | [**UserViewInfo**](UserViewInfo.md) |  | [optional] 
**debug_info** | [**FeedbackDebugInfo**](FeedbackDebugInfo.md) |  | [optional] 
**application_id** | **str** | The application ID of the client that sent the feedback event. | [optional] 

## Example

```python
from openapi_client.models.feedback import Feedback

# TODO update the JSON string below
json = "{}"
# create an instance of Feedback from a JSON string
feedback_instance = Feedback.from_json(json)
# print the JSON string representation of the object
print(Feedback.to_json())

# convert the object into a dict
feedback_dict = feedback_instance.to_dict()
# create an instance of Feedback from a dict
feedback_from_dict = Feedback.from_dict(feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


