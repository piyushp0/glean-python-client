# DeleteCollectionItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**Collection**](Collection.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_collection_item_response import DeleteCollectionItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCollectionItemResponse from a JSON string
delete_collection_item_response_instance = DeleteCollectionItemResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteCollectionItemResponse.to_json())

# convert the object into a dict
delete_collection_item_response_dict = delete_collection_item_response_instance.to_dict()
# create an instance of DeleteCollectionItemResponse from a dict
delete_collection_item_response_from_dict = DeleteCollectionItemResponse.from_dict(delete_collection_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


