# FeedEntryUiConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | defines how to render this particular displayable list card | [optional] 
**additional_flags** | [**DisplayableListItemUIConfig**](DisplayableListItemUIConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.feed_entry_ui_config import FeedEntryUiConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FeedEntryUiConfig from a JSON string
feed_entry_ui_config_instance = FeedEntryUiConfig.from_json(json)
# print the JSON string representation of the object
print(FeedEntryUiConfig.to_json())

# convert the object into a dict
feed_entry_ui_config_dict = feed_entry_ui_config_instance.to_dict()
# create an instance of FeedEntryUiConfig from a dict
feed_entry_ui_config_from_dict = FeedEntryUiConfig.from_dict(feed_entry_ui_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


