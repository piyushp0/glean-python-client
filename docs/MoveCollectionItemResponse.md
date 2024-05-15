# MoveCollectionItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**Collection**](Collection.md) |  | [optional] 

## Example

```python
from openapi_client.models.move_collection_item_response import MoveCollectionItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MoveCollectionItemResponse from a JSON string
move_collection_item_response_instance = MoveCollectionItemResponse.from_json(json)
# print the JSON string representation of the object
print(MoveCollectionItemResponse.to_json())

# convert the object into a dict
move_collection_item_response_dict = move_collection_item_response_instance.to_dict()
# create an instance of MoveCollectionItemResponse from a dict
move_collection_item_response_from_dict = MoveCollectionItemResponse.from_dict(move_collection_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


