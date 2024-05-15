# ListEntitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Person]**](Person.md) |  | [optional] 
**team_results** | [**List[Team]**](Team.md) |  | [optional] 
**custom_entity_results** | [**List[CustomEntity]**](CustomEntity.md) |  | [optional] 
**facet_results** | [**List[FacetResult]**](FacetResult.md) |  | [optional] 
**cursor** | **str** | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start. | [optional] 
**total_count** | **int** | The total number of entities available | [optional] 
**has_more_results** | **bool** | Whether or not more entities can be fetched. | [optional] 
**sort_options** | [**List[EntitiesSortOrder]**](EntitiesSortOrder.md) | Sort options from EntitiesSortOrder supported for this response. Default is empty list. | [optional] 
**custom_facet_names** | **List[str]** | list of Person attributes that are custom setup by deployment | [optional] 

## Example

```python
from openapi_client.models.list_entities_response import ListEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEntitiesResponse from a JSON string
list_entities_response_instance = ListEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print(ListEntitiesResponse.to_json())

# convert the object into a dict
list_entities_response_dict = list_entities_response_instance.to_dict()
# create an instance of ListEntitiesResponse from a dict
list_entities_response_from_dict = ListEntitiesResponse.from_dict(list_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


