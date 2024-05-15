# GetDraftAnnouncementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | [**Announcement**](Announcement.md) |  | [optional] 
**error** | [**AnnouncementError**](AnnouncementError.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_draft_announcement_response import GetDraftAnnouncementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDraftAnnouncementResponse from a JSON string
get_draft_announcement_response_instance = GetDraftAnnouncementResponse.from_json(json)
# print the JSON string representation of the object
print(GetDraftAnnouncementResponse.to_json())

# convert the object into a dict
get_draft_announcement_response_dict = get_draft_announcement_response_instance.to_dict()
# create an instance of GetDraftAnnouncementResponse from a dict
get_draft_announcement_response_from_dict = GetDraftAnnouncementResponse.from_dict(get_draft_announcement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


