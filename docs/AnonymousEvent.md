# AnonymousEvent

A generic, light-weight calendar event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**event_type** | **str** | The nature of the event, for example \&quot;out of office\&quot;. | [optional] 

## Example

```python
from openapi_client.models.anonymous_event import AnonymousEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymousEvent from a JSON string
anonymous_event_instance = AnonymousEvent.from_json(json)
# print the JSON string representation of the object
print(AnonymousEvent.to_json())

# convert the object into a dict
anonymous_event_dict = anonymous_event_instance.to_dict()
# create an instance of AnonymousEvent from a dict
anonymous_event_from_dict = AnonymousEvent.from_dict(anonymous_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


