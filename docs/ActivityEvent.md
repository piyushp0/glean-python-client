# ActivityEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Universally unique identifier of the event. To allow for reliable retransmission, only the earliest received event of a given UUID is considered valid by the server and subsequent are ignored. | [optional] 
**action** | **str** | The type of activity this represents. | 
**params** | [**ActivityEventParams**](ActivityEventParams.md) |  | [optional] 
**timestamp** | **datetime** | The ISO 8601 timestamp when the activity began. | 
**url** | **str** | The URL of the activity. | 

## Example

```python
from openapi_client.models.activity_event import ActivityEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityEvent from a JSON string
activity_event_instance = ActivityEvent.from_json(json)
# print the JSON string representation of the object
print(ActivityEvent.to_json())

# convert the object into a dict
activity_event_dict = activity_event_instance.to_dict()
# create an instance of ActivityEvent from a dict
activity_event_from_dict = ActivityEvent.from_dict(activity_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


