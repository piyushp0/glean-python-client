# FacetBucketFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facet** | **str** | The facet whose buckets should be filtered. | [optional] 
**prefix** | **str** | The per-term prefix that facet buckets should be filtered on. | [optional] 

## Example

```python
from openapi_client.models.facet_bucket_filter import FacetBucketFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FacetBucketFilter from a JSON string
facet_bucket_filter_instance = FacetBucketFilter.from_json(json)
# print the JSON string representation of the object
print(FacetBucketFilter.to_json())

# convert the object into a dict
facet_bucket_filter_dict = facet_bucket_filter_instance.to_dict()
# create an instance of FacetBucketFilter from a dict
facet_bucket_filter_from_dict = FacetBucketFilter.from_dict(facet_bucket_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


