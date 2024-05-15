# AddCollectionItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**Collection**](Collection.md) |  | [optional] 
**error** | [**AddCollectionItemsError**](AddCollectionItemsError.md) |  | [optional] 

## Example

```python
from openapi_client.models.add_collection_items_response import AddCollectionItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddCollectionItemsResponse from a JSON string
add_collection_items_response_instance = AddCollectionItemsResponse.from_json(json)
# print the JSON string representation of the object
print(AddCollectionItemsResponse.to_json())

# convert the object into a dict
add_collection_items_response_dict = add_collection_items_response_instance.to_dict()
# create an instance of AddCollectionItemsResponse from a dict
add_collection_items_response_from_dict = AddCollectionItemsResponse.from_dict(add_collection_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


