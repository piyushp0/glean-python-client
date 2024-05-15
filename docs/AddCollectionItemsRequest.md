# AddCollectionItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **float** | The ID of the Collection to add items to. | 
**added_collection_item_descriptors** | [**List[CollectionItemDescriptor]**](CollectionItemDescriptor.md) | The CollectionItemDescriptors of the items being added. | [optional] 

## Example

```python
from openapi_client.models.add_collection_items_request import AddCollectionItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCollectionItemsRequest from a JSON string
add_collection_items_request_instance = AddCollectionItemsRequest.from_json(json)
# print the JSON string representation of the object
print(AddCollectionItemsRequest.to_json())

# convert the object into a dict
add_collection_items_request_dict = add_collection_items_request_instance.to_dict()
# create an instance of AddCollectionItemsRequest from a dict
add_collection_items_request_from_dict = AddCollectionItemsRequest.from_dict(add_collection_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


