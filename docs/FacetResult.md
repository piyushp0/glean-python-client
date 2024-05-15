# FacetResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | The source of this facet (e.g. container_name, type, last_updated_at). | [optional] 
**operator_name** | **str** | How to display this facet. Currently supportes &#39;SelectSingle&#39; and &#39;SelectMultiple&#39;. | [optional] 
**buckets** | [**List[FacetBucket]**](FacetBucket.md) | A list of unique buckets that exist within this result set. | [optional] 
**has_more_buckets** | **bool** | Returns true if more buckets exist than those returned. Additional buckets can be retrieve by requesting again with a higher facetBucketSize. | [optional] 
**group_name** | **str** | For most facets this will be the empty string, meaning the facet is high-level and applies to all documents for the datasource. When non-empty, this is used to group facets together (i.e. group facets for each doctype for a certain datasource) | [optional] 

## Example

```python
from openapi_client.models.facet_result import FacetResult

# TODO update the JSON string below
json = "{}"
# create an instance of FacetResult from a JSON string
facet_result_instance = FacetResult.from_json(json)
# print the JSON string representation of the object
print(FacetResult.to_json())

# convert the object into a dict
facet_result_dict = facet_result_instance.to_dict()
# create an instance of FacetResult from a dict
facet_result_from_dict = FacetResult.from_dict(facet_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


