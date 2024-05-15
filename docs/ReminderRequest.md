# ReminderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | The document which the verification is for new reminders and/or update. | 
**assignee** | **str** | The obfuscated id of the person this verification is assigned to. | [optional] 
**remind_in_days** | **int** | Reminder for the next verifications in terms of days. For deletion, this will be omitted. | [optional] 
**reason** | **str** | An optional free-text reason for the reminder. This is particularly useful when a reminder is used to ask for verification from another user (for example, \&quot;Duplicate\&quot;, \&quot;Incomplete\&quot;, \&quot;Incorrect\&quot;). | [optional] 

## Example

```python
from openapi_client.models.reminder_request import ReminderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderRequest from a JSON string
reminder_request_instance = ReminderRequest.from_json(json)
# print the JSON string representation of the object
print(ReminderRequest.to_json())

# convert the object into a dict
reminder_request_dict = reminder_request_instance.to_dict()
# create an instance of ReminderRequest from a dict
reminder_request_from_dict = ReminderRequest.from_dict(reminder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


