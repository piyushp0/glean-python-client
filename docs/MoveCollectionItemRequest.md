# MoveCollectionItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **int** | The ID of the Collection to move items in. | 
**item_id** | **str** | The item ID of the item being moved. | 
**new_next_item_id** | **str** | The (optional) item ID of the item that is the new next of itemId, or empty if this is now the last item. This item does not move, it&#39;s used as a reference position to put the itemId in the right position. | [optional] 

## Example

```python
from openapi_client.models.move_collection_item_request import MoveCollectionItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MoveCollectionItemRequest from a JSON string
move_collection_item_request_instance = MoveCollectionItemRequest.from_json(json)
# print the JSON string representation of the object
print(MoveCollectionItemRequest.to_json())

# convert the object into a dict
move_collection_item_request_dict = move_collection_item_request_instance.to_dict()
# create an instance of MoveCollectionItemRequest from a dict
move_collection_item_request_from_dict = MoveCollectionItemRequest.from_dict(move_collection_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


