# FeedEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **str** | optional ID associated with a single feed entry (displayable_list_id) | [optional] 
**title** | **str** | Title for the result. Can be document title, event title and so on. | 
**thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**created_by** | [**Person**](Person.md) |  | [optional] 
**ui_config** | [**FeedEntryUiConfig**](FeedEntryUiConfig.md) |  | [optional] 
**snippet** | **str** | A textual snippet representing this entry, dependent on type. For example, for USER_MENTION, it may contain the sentence in which the mention occurred. | [optional] 
**justification_type** | **str** | Type of the justification. | [optional] 
**justification** | **str** | Server side generated justification string if server provides one. | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular feed entry in this particular response. To be used for /feedback reporting. | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**event** | [**CalendarEvent**](CalendarEvent.md) |  | [optional] 
**announcement** | [**Announcement**](Announcement.md) |  | [optional] 
**collection** | [**Collection**](Collection.md) |  | [optional] 
**collection_item** | [**CollectionItem**](CollectionItem.md) |  | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**app** | [**AppResult**](AppResult.md) |  | [optional] 
**activities** | [**List[UserActivity]**](UserActivity.md) | List of activity where each activity has user, action, timestamp. | [optional] 
**document_visitor_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**view_url** | **str** | View URL for the entry if based on links that are not documents in Glean. | [optional] 
**additional_client_actions** | [**List[ClientAction]**](ClientAction.md) | List of client actions suggested by the backend to be included for entry. | [optional] 

## Example

```python
from openapi_client.models.feed_entry import FeedEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FeedEntry from a JSON string
feed_entry_instance = FeedEntry.from_json(json)
# print the JSON string representation of the object
print(FeedEntry.to_json())

# convert the object into a dict
feed_entry_dict = feed_entry_instance.to_dict()
# create an instance of FeedEntry from a dict
feed_entry_from_dict = FeedEntry.from_dict(feed_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


