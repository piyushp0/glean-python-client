# PeopleFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**List[FacetFilter]**](FacetFilter.md) | Facets used for filtering people search | [optional] 
**query** | **str** | A query string to search for people that each person in the response must conform to. An empty query does not filter any people. | [optional] 

## Example

```python
from openapi_client.models.people_filters import PeopleFilters

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleFilters from a JSON string
people_filters_instance = PeopleFilters.from_json(json)
# print the JSON string representation of the object
print(PeopleFilters.to_json())

# convert the object into a dict
people_filters_dict = people_filters_instance.to_dict()
# create an instance of PeopleFilters from a dict
people_filters_from_dict = PeopleFilters.from_dict(people_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


