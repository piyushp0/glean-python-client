# CalendarAttendee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_organizer** | **bool** | Whether or not this attendee is an organizer. | [optional] 
**is_in_group** | **bool** | Whether or not this attendee is in a group. Needed temporarily at least to support both flat attendees and tree for compatibility. | [optional] 
**person** | [**Person**](Person.md) |  | 
**group_attendees** | [**List[CalendarAttendee]**](CalendarAttendee.md) | If this attendee is a group, represents the list of individual attendees in the group. | [optional] 
**response_status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.calendar_attendee import CalendarAttendee

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarAttendee from a JSON string
calendar_attendee_instance = CalendarAttendee.from_json(json)
# print the JSON string representation of the object
print(CalendarAttendee.to_json())

# convert the object into a dict
calendar_attendee_dict = calendar_attendee_instance.to_dict()
# create an instance of CalendarAttendee from a dict
calendar_attendee_from_dict = CalendarAttendee.from_dict(calendar_attendee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


