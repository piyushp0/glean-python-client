# CalendarEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**event_type** | **str** | The nature of the event, for example \&quot;out of office\&quot;. | [optional] 
**id** | **str** | The calendar event id | 
**url** | **str** | A permalink for this calendar event | 
**attendees** | [**CalendarAttendees**](CalendarAttendees.md) |  | [optional] 
**location** | **str** | The location that this event is taking place at. | [optional] 
**conference_data** | [**ConferenceData**](ConferenceData.md) |  | [optional] 
**description** | **str** | The HTML description of the event. | [optional] 
**datasource** | **str** | The app or other repository type from which the event was extracted | [optional] 
**classifications** | [**List[EventClassification]**](EventClassification.md) |  | [optional] 
**generated_attachments** | [**List[GeneratedAttachment]**](GeneratedAttachment.md) |  | [optional] 

## Example

```python
from openapi_client.models.calendar_event import CalendarEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEvent from a JSON string
calendar_event_instance = CalendarEvent.from_json(json)
# print the JSON string representation of the object
print(CalendarEvent.to_json())

# convert the object into a dict
calendar_event_dict = calendar_event_instance.to_dict()
# create an instance of CalendarEvent from a dict
calendar_event_from_dict = CalendarEvent.from_dict(calendar_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


