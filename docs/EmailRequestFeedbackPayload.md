# EmailRequestFeedbackPayload

Optional payload for feedback reporting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Additional freeform comments provided by the reporter. | [optional] 
**custom_json** | **str** | Arbitrary email param payloads from 3P-customer widgets. Prefer the structured fields when possible. | [optional] 
**image_urls** | **List[str]** | Images uploaded by the user when submitting feedback | [optional] 
**issue_type** | **str** | The type of issue being reported, e.g. RESULT_MISSING or OTHER for search feedback. | [optional] 
**query** | **str** | The query the reporter tried when feedback was sent. | [optional] 
**tracking_token** | **str** | The tracking token of the feedback that admins can provide Glean Support to debug | [optional] 
**url** | **str** | The URL the reporter was on when feedback was sent. | [optional] 
**rating_key** | **str** | The label of the rating that was selected when feedback was sent. | [optional] 

## Example

```python
from openapi_client.models.email_request_feedback_payload import EmailRequestFeedbackPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmailRequestFeedbackPayload from a JSON string
email_request_feedback_payload_instance = EmailRequestFeedbackPayload.from_json(json)
# print the JSON string representation of the object
print(EmailRequestFeedbackPayload.to_json())

# convert the object into a dict
email_request_feedback_payload_dict = email_request_feedback_payload_instance.to_dict()
# create an instance of EmailRequestFeedbackPayload from a dict
email_request_feedback_payload_from_dict = EmailRequestFeedbackPayload.from_dict(email_request_feedback_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


