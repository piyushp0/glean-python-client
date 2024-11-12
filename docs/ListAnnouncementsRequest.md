# ListAnnouncementsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**AnnouncementChannel**](AnnouncementChannel.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_announcements_request import ListAnnouncementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnnouncementsRequest from a JSON string
list_announcements_request_instance = ListAnnouncementsRequest.from_json(json)
# print the JSON string representation of the object
print(ListAnnouncementsRequest.to_json())

# convert the object into a dict
list_announcements_request_dict = list_announcements_request_instance.to_dict()
# create an instance of ListAnnouncementsRequest from a dict
list_announcements_request_from_dict = ListAnnouncementsRequest.from_dict(list_announcements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


