# FeedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category of the result, one of the requested categories in incoming request. | 
**primary_entry** | [**FeedEntry**](FeedEntry.md) |  | 
**secondary_entries** | [**List[FeedEntry]**](FeedEntry.md) | Secondary entries for the result e.g. suggested docs for the calendar, carousel. | [optional] 
**rank** | **int** | Rank of the result. Rank is suggested by server. Client side rank may differ. | [optional] 
**facet_results** | [**List[FacetResult]**](FacetResult.md) | DEPRECATED - List of facets that can be used to filter the entry&#39;s content. | [optional] 

## Example

```python
from openapi_client.models.feed_result import FeedResult

# TODO update the JSON string below
json = "{}"
# create an instance of FeedResult from a JSON string
feed_result_instance = FeedResult.from_json(json)
# print the JSON string representation of the object
print(FeedResult.to_json())

# convert the object into a dict
feed_result_dict = feed_result_instance.to_dict()
# create an instance of FeedResult from a dict
feed_result_from_dict = FeedResult.from_dict(feed_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


