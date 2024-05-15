# DeleteCollectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The IDs of the Collections to delete. | 
**allowed_datasource** | **str** | The datasource allowed in the Collection to be deleted. | [optional] 

## Example

```python
from openapi_client.models.delete_collection_request import DeleteCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCollectionRequest from a JSON string
delete_collection_request_instance = DeleteCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteCollectionRequest.to_json())

# convert the object into a dict
delete_collection_request_dict = delete_collection_request_instance.to_dict()
# create an instance of DeleteCollectionRequest from a dict
delete_collection_request_from_dict = DeleteCollectionRequest.from_dict(delete_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


