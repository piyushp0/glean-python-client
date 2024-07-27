# EmailRequest

A request to send email[s] to the specified users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_template** | [**CommunicationTemplate**](CommunicationTemplate.md) |  | 
**alert_data** | [**AlertData**](AlertData.md) |  | [optional] 
**recipients** | [**List[Person]**](Person.md) | The people to send emails to | [optional] 
**cc_recipients** | [**List[Person]**](Person.md) | The people to CC for each email | [optional] 
**recipient_filters** | [**PeopleFilters**](PeopleFilters.md) |  | [optional] 
**company_name** | **str** | Name of the company. | [optional] 
**datasource_instance** | **str** | The instance ID of the datasource (if any) | [optional] 
**senders** | [**List[Person]**](Person.md) | The people who triggered this email | [optional] 
**web_app_url** | **str** | The URL of the client triggering the request, as received in the ClientConfig | [optional] 
**server_url** | **str** | The URL of the QE instance the email request is processed by. | [optional] 
**unsubscribe_url** | **str** | The URL to unsubscribe from emails. | [optional] 
**documents** | [**List[Document]**](Document.md) | The documents this email request refers to | [optional] 
**reasons** | **List[str]** | Reasons this email request was sent. Will be shown directly to end user. | [optional] 
**blocks** | **Dict[str, List[object]]** | For building complex email UIs, we use a block structure that dictates what we create in the UI | [optional] 
**subjects** | **Dict[str, str]** | Mapping of recipientIds to the email subject they are to receive. Optional and only meant for templates with Sendgrid subject set to {{subject}} | [optional] 
**feedback_payload** | [**EmailRequestFeedbackPayload**](EmailRequestFeedbackPayload.md) |  | [optional] 
**chat_feedback_payload** | [**EmailRequestChatFeedbackPayload**](EmailRequestChatFeedbackPayload.md) |  | [optional] 
**dlp_report_data** | [**DlpReportData**](DlpReportData.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_request import EmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailRequest from a JSON string
email_request_instance = EmailRequest.from_json(json)
# print the JSON string representation of the object
print(EmailRequest.to_json())

# convert the object into a dict
email_request_dict = email_request_instance.to_dict()
# create an instance of EmailRequest from a dict
email_request_from_dict = EmailRequest.from_dict(email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


