# PublishDraftAnnouncementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque id of the draft announcement to be published. | 

## Example

```python
from openapi_client.models.publish_draft_announcement_request import PublishDraftAnnouncementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishDraftAnnouncementRequest from a JSON string
publish_draft_announcement_request_instance = PublishDraftAnnouncementRequest.from_json(json)
# print the JSON string representation of the object
print(PublishDraftAnnouncementRequest.to_json())

# convert the object into a dict
publish_draft_announcement_request_dict = publish_draft_announcement_request_instance.to_dict()
# create an instance of PublishDraftAnnouncementRequest from a dict
publish_draft_announcement_request_from_dict = PublishDraftAnnouncementRequest.from_dict(publish_draft_announcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


