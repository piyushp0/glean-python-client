# CalendarAttendees


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**people** | [**List[CalendarAttendee]**](CalendarAttendee.md) | Full details of some of the attendees of this event | [optional] 
**is_limit** | **bool** | Whether the total count of the people returned is at the retrieval limit. | [optional] 
**total** | **int** | Total number of attendees in this event. | [optional] 
**num_accepted** | **int** | Total number of attendees who have accepted this event. | [optional] 
**num_declined** | **int** | Total number of attendees who have declined this event. | [optional] 
**num_no_response** | **int** | Total number of attendees who have not responded to this event. | [optional] 
**num_tentative** | **int** | Total number of attendees who have responded tentatively (i.e. responded maybe) to this event. | [optional] 

## Example

```python
from openapi_client.models.calendar_attendees import CalendarAttendees

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarAttendees from a JSON string
calendar_attendees_instance = CalendarAttendees.from_json(json)
# print the JSON string representation of the object
print(CalendarAttendees.to_json())

# convert the object into a dict
calendar_attendees_dict = calendar_attendees_instance.to_dict()
# create an instance of CalendarAttendees from a dict
calendar_attendees_from_dict = CalendarAttendees.from_dict(calendar_attendees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


