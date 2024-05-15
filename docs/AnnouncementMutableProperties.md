# AnnouncementMutableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** | The date and time at which the announcement becomes active. | [optional] 
**end_time** | **datetime** | The date and time at which the announcement expires. | [optional] 
**title** | **str** | The headline of the announcement. | [optional] 
**body** | [**StructuredText**](StructuredText.md) |  | [optional] 
**emoji** | **str** | An emoji used to indicate the nature of the announcement. | [optional] 
**thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**banner** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search. | [optional] 
**source_document_id** | **str** | The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread). | [optional] 
**hide_attribution** | **bool** | Whether or not to hide an author attribution. | [optional] 
**channel** | **str** | This determines whether this is a Social Feed post or a regular announcement. | [optional] 
**post_type** | **str** | This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site. | [optional] 
**is_prioritized** | **bool** | Used by the Social Feed to pin posts to the front of the feed. | [optional] 
**view_url** | **str** | URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel&#x3D;\&quot;SOCIAL_FEED\&quot;. | [optional] 

## Example

```python
from openapi_client.models.announcement_mutable_properties import AnnouncementMutableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementMutableProperties from a JSON string
announcement_mutable_properties_instance = AnnouncementMutableProperties.from_json(json)
# print the JSON string representation of the object
print(AnnouncementMutableProperties.to_json())

# convert the object into a dict
announcement_mutable_properties_dict = announcement_mutable_properties_instance.to_dict()
# create an instance of AnnouncementMutableProperties from a dict
announcement_mutable_properties_from_dict = AnnouncementMutableProperties.from_dict(announcement_mutable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


