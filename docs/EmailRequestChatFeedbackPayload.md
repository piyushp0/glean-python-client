# EmailRequestChatFeedbackPayload

Payload for chat feedback reporting. Required when template is `CHAT_FEEDBACK`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **str** | Rating given to the conversation (currently either \&quot;upvoted\&quot; or \&quot;downvoted\&quot;). | [optional] 
**comments** | **str** | Additional freeform comments provided by the reporter. | [optional] 
**previous_messages** | **List[str]** | Previous messages in this conversation. | [optional] 

## Example

```python
from openapi_client.models.email_request_chat_feedback_payload import EmailRequestChatFeedbackPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmailRequestChatFeedbackPayload from a JSON string
email_request_chat_feedback_payload_instance = EmailRequestChatFeedbackPayload.from_json(json)
# print the JSON string representation of the object
print(EmailRequestChatFeedbackPayload.to_json())

# convert the object into a dict
email_request_chat_feedback_payload_dict = email_request_chat_feedback_payload_instance.to_dict()
# create an instance of EmailRequestChatFeedbackPayload from a dict
email_request_chat_feedback_payload_from_dict = EmailRequestChatFeedbackPayload.from_dict(email_request_chat_feedback_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


