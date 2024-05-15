# EditCollectionItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **int** | The ID of the Collection to edit CollectionItems in. | 
**item_id** | **str** | The ID of the CollectionItem to edit. | 
**name** | **str** | The optional name of the Collection item. | [optional] 
**description** | **str** | A helpful description of why this CollectionItem is in the Collection that it&#39;s in. | [optional] 
**icon** | **str** | The emoji icon for this CollectionItem. Only used for Text type items. | [optional] 

## Example

```python
from openapi_client.models.edit_collection_item_request import EditCollectionItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditCollectionItemRequest from a JSON string
edit_collection_item_request_instance = EditCollectionItemRequest.from_json(json)
# print the JSON string representation of the object
print(EditCollectionItemRequest.to_json())

# convert the object into a dict
edit_collection_item_request_dict = edit_collection_item_request_instance.to_dict()
# create an instance of EditCollectionItemRequest from a dict
edit_collection_item_request_from_dict = EditCollectionItemRequest.from_dict(edit_collection_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


