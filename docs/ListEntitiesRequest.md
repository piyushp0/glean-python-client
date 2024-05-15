# ListEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**List[FacetFilter]**](FacetFilter.md) |  | [optional] 
**sort** | [**List[SortOptions]**](SortOptions.md) | Use EntitiesSortOrder enum for SortOptions.sortBy | [optional] 
**entity_type** | **str** |  | [optional] [default to 'PEOPLE']
**datasource** | **str** | The datasource associated with the entity type, most commonly used with CUSTOM_ENTITIES | [optional] 
**query** | **str** | A query string to search for entities that each entity in the response must conform to. An empty query does not filter any entities. | [optional] 
**include_fields** | **List[str]** | List of entity fields to return (that aren&#39;t returned by default) | [optional] 
**page_size** | **int** | Hint to the server about how many results to send back. Server may return less. | [optional] 
**cursor** | **str** | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start. | [optional] 
**source** | **str** | A string denoting the search surface from which the endpoint is called. | [optional] 

## Example

```python
from openapi_client.models.list_entities_request import ListEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListEntitiesRequest from a JSON string
list_entities_request_instance = ListEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(ListEntitiesRequest.to_json())

# convert the object into a dict
list_entities_request_dict = list_entities_request_instance.to_dict()
# create an instance of ListEntitiesRequest from a dict
list_entities_request_from_dict = ListEntitiesRequest.from_dict(list_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


