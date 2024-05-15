# ListCollectionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | [**List[Collection]**](Collection.md) | List of all Collections, no Collection items are fetched. | 

## Example

```python
from openapi_client.models.list_collections_response import ListCollectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCollectionsResponse from a JSON string
list_collections_response_instance = ListCollectionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListCollectionsResponse.to_json())

# convert the object into a dict
list_collections_response_dict = list_collections_response_instance.to_dict()
# create an instance of ListCollectionsResponse from a dict
list_collections_response_from_dict = ListCollectionsResponse.from_dict(list_collections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


