# GetAnnouncementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the announcement to be retrieved. | 

## Example

```python
from openapi_client.models.get_announcement_request import GetAnnouncementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnnouncementRequest from a JSON string
get_announcement_request_instance = GetAnnouncementRequest.from_json(json)
# print the JSON string representation of the object
print(GetAnnouncementRequest.to_json())

# convert the object into a dict
get_announcement_request_dict = get_announcement_request_instance.to_dict()
# create an instance of GetAnnouncementRequest from a dict
get_announcement_request_from_dict = GetAnnouncementRequest.from_dict(get_announcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


