# ShortcutsPaginationMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Cursor indicates the start of the next page of results | [optional] 
**has_next_page** | **bool** |  | [optional] 
**total_item_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.shortcuts_pagination_metadata import ShortcutsPaginationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ShortcutsPaginationMetadata from a JSON string
shortcuts_pagination_metadata_instance = ShortcutsPaginationMetadata.from_json(json)
# print the JSON string representation of the object
print(ShortcutsPaginationMetadata.to_json())

# convert the object into a dict
shortcuts_pagination_metadata_dict = shortcuts_pagination_metadata_instance.to_dict()
# create an instance of ShortcutsPaginationMetadata from a dict
shortcuts_pagination_metadata_from_dict = ShortcutsPaginationMetadata.from_dict(shortcuts_pagination_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


