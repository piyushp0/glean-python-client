# GetAnnouncementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | [**Announcement**](Announcement.md) |  | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular announcement. To be used for /feedback reporting. | [optional] 
**error** | [**AnnouncementError**](AnnouncementError.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_announcement_response import GetAnnouncementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnnouncementResponse from a JSON string
get_announcement_response_instance = GetAnnouncementResponse.from_json(json)
# print the JSON string representation of the object
print(GetAnnouncementResponse.to_json())

# convert the object into a dict
get_announcement_response_dict = get_announcement_response_instance.to_dict()
# create an instance of GetAnnouncementResponse from a dict
get_announcement_response_from_dict = GetAnnouncementResponse.from_dict(get_announcement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


