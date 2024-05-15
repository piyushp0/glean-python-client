# FacetBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Estimated number of results in this facet. | [optional] 
**datasource** | **str** | The datasource the value belongs to. This will be used by the all tab to show types across all datasources. | [optional] 
**percentage** | **int** | Estimated percentage of results in this facet. | [optional] 
**value** | [**FacetValue**](FacetValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.facet_bucket import FacetBucket

# TODO update the JSON string below
json = "{}"
# create an instance of FacetBucket from a JSON string
facet_bucket_instance = FacetBucket.from_json(json)
# print the JSON string representation of the object
print(FacetBucket.to_json())

# convert the object into a dict
facet_bucket_dict = facet_bucket_instance.to_dict()
# create an instance of FacetBucket from a dict
facet_bucket_from_dict = FacetBucket.from_dict(facet_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


