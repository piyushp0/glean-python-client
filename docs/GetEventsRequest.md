# GetEventsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The ids of the calendar events to be retrieved. | 
**auth_tokens** | [**List[AuthToken]**](AuthToken.md) | Auth tokens if client-side authentication. | [optional] 
**datasource** | **str** | The app or other repository type from which the event was extracted | [optional] 
**annotate** | **bool** | Whether relevant content and documents, via GeneratedAttachments, should be attached to the events. | [optional] 

## Example

```python
from openapi_client.models.get_events_request import GetEventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventsRequest from a JSON string
get_events_request_instance = GetEventsRequest.from_json(json)
# print the JSON string representation of the object
print(GetEventsRequest.to_json())

# convert the object into a dict
get_events_request_dict = get_events_request_instance.to_dict()
# create an instance of GetEventsRequest from a dict
get_events_request_from_dict = GetEventsRequest.from_dict(get_events_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


