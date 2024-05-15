# AnnouncementAllOfViewerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_dismissed** | **bool** | Whether the viewer has dismissed the announcement. | [optional] 
**is_read** | **bool** | Whether the viewer has read the announcement. | [optional] 

## Example

```python
from openapi_client.models.announcement_all_of_viewer_info import AnnouncementAllOfViewerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementAllOfViewerInfo from a JSON string
announcement_all_of_viewer_info_instance = AnnouncementAllOfViewerInfo.from_json(json)
# print the JSON string representation of the object
print(AnnouncementAllOfViewerInfo.to_json())

# convert the object into a dict
announcement_all_of_viewer_info_dict = announcement_all_of_viewer_info_instance.to_dict()
# create an instance of AnnouncementAllOfViewerInfo from a dict
announcement_all_of_viewer_info_from_dict = AnnouncementAllOfViewerInfo.from_dict(announcement_all_of_viewer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


