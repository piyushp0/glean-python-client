# Reminder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**Person**](Person.md) |  | 
**requestor** | [**Person**](Person.md) |  | [optional] 
**remind_at** | **int** | Unix timestamp for when the reminder should trigger (in seconds since epoch UTC). | 
**created_at** | **int** | Unix timestamp for when the reminder was first created (in seconds since epoch UTC). | [optional] 
**reason** | **str** | An optional free-text reason for the reminder. This is particularly useful when a reminder is used to ask for verification from another user (for example, \&quot;Duplicate\&quot;, \&quot;Incomplete\&quot;, \&quot;Incorrect\&quot;). | [optional] 

## Example

```python
from openapi_client.models.reminder import Reminder

# TODO update the JSON string below
json = "{}"
# create an instance of Reminder from a JSON string
reminder_instance = Reminder.from_json(json)
# print the JSON string representation of the object
print(Reminder.to_json())

# convert the object into a dict
reminder_dict = reminder_instance.to_dict()
# create an instance of Reminder from a dict
reminder_from_dict = Reminder.from_dict(reminder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


