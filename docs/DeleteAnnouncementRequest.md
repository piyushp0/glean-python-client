# DeleteAnnouncementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque id of the announcement to be deleted. | 

## Example

```python
from openapi_client.models.delete_announcement_request import DeleteAnnouncementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnnouncementRequest from a JSON string
delete_announcement_request_instance = DeleteAnnouncementRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteAnnouncementRequest.to_json())

# convert the object into a dict
delete_announcement_request_dict = delete_announcement_request_instance.to_dict()
# create an instance of DeleteAnnouncementRequest from a dict
delete_announcement_request_from_dict = DeleteAnnouncementRequest.from_dict(delete_announcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


