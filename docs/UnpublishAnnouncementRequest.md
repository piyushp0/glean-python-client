# UnpublishAnnouncementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque id of the announcement to be unpublished. | 

## Example

```python
from openapi_client.models.unpublish_announcement_request import UnpublishAnnouncementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnpublishAnnouncementRequest from a JSON string
unpublish_announcement_request_instance = UnpublishAnnouncementRequest.from_json(json)
# print the JSON string representation of the object
print(UnpublishAnnouncementRequest.to_json())

# convert the object into a dict
unpublish_announcement_request_dict = unpublish_announcement_request_instance.to_dict()
# create an instance of UnpublishAnnouncementRequest from a dict
unpublish_announcement_request_from_dict = UnpublishAnnouncementRequest.from_dict(unpublish_announcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


