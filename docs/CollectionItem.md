# CollectionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The optional name of the Collection item. | [optional] 
**description** | **str** | A helpful description of why this CollectionItem is in the Collection that it&#39;s in. | [optional] 
**icon** | **str** | The emoji icon for this CollectionItem. Only used for Text type items. | [optional] 
**collection_id** | **int** | The Collection ID of the Collection that this CollectionItem belongs in. | 
**document_id** | **str** | If this CollectionItem is indexed, the Glean Document ID of that document. | [optional] 
**url** | **str** | The URL of this CollectionItem. | [optional] 
**item_id** | **str** | Unique identifier for the item within the Collection it belongs to. | [optional] 
**created_by** | [**Person**](Person.md) |  | [optional] 
**created_at** | **datetime** | Unix timestamp for when the item was first added (in seconds since epoch UTC). | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**collection** | [**Collection**](Collection.md) |  | [optional] 
**item_type** | **str** |  | 

## Example

```python
from openapi_client.models.collection_item import CollectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionItem from a JSON string
collection_item_instance = CollectionItem.from_json(json)
# print the JSON string representation of the object
print(CollectionItem.to_json())

# convert the object into a dict
collection_item_dict = collection_item_instance.to_dict()
# create an instance of CollectionItem from a dict
collection_item_from_dict = CollectionItem.from_dict(collection_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


