# DeleteCollectionItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **float** | The ID of the Collection to remove an item in. | 
**item_id** | **str** | The item ID of the CollectionItem to remove from this Collection. | 
**document_id** | **str** | The (optional) Glean Document ID of the CollectionItem to remove from this Collection if this is an indexed document. | [optional] 

## Example

```python
from openapi_client.models.delete_collection_item_request import DeleteCollectionItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCollectionItemRequest from a JSON string
delete_collection_item_request_instance = DeleteCollectionItemRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteCollectionItemRequest.to_json())

# convert the object into a dict
delete_collection_item_request_dict = delete_collection_item_request_instance.to_dict()
# create an instance of DeleteCollectionItemRequest from a dict
delete_collection_item_request_from_dict = DeleteCollectionItemRequest.from_dict(delete_collection_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


