# ListCollectionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_audience** | **bool** | Whether to include the audience filters with the listed Collections. | [optional] 
**include_roles** | **bool** | Whether to include the editor roles with the listed Collections. | [optional] 
**allowed_datasource** | **str** | The datasource type this Collection can hold. ANSWERS - for Collections representing answer boards | [optional] 

## Example

```python
from openapi_client.models.list_collections_request import ListCollectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListCollectionsRequest from a JSON string
list_collections_request_instance = ListCollectionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListCollectionsRequest.to_json())

# convert the object into a dict
list_collections_request_dict = list_collections_request_instance.to_dict()
# create an instance of ListCollectionsRequest from a dict
list_collections_request_from_dict = ListCollectionsRequest.from_dict(list_collections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


