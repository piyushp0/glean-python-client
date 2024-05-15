# GetCollectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Collection to be retrieved. | 
**with_items** | **bool** | Whether or not to include the Collection Items in this Collection. Only request if absolutely required, as this is expensive. | [optional] 
**with_hierarchy** | **bool** | Whether or not to include the top level Collection in this Collection&#39;s hierarchy. | [optional] 
**allowed_datasource** | **str** | The datasource allowed in the Collection returned. | [optional] 

## Example

```python
from openapi_client.models.get_collection_request import GetCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCollectionRequest from a JSON string
get_collection_request_instance = GetCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(GetCollectionRequest.to_json())

# convert the object into a dict
get_collection_request_dict = get_collection_request_instance.to_dict()
# create an instance of GetCollectionRequest from a dict
get_collection_request_from_dict = GetCollectionRequest.from_dict(get_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


