# FeedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_ids** | **List[int]** | List of experiment ids for the corresponding request. | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular feed response. | [optional] 
**server_timestamp** | **int** | Server unix timestamp (in seconds since epoch UTC). | 
**results** | [**List[FeedResult]**](FeedResult.md) |  | [optional] 
**facet_results** | **Dict[str, List[FacetResult]]** | Map from category to the list of facets that can be used to filter the entry&#39;s content. | [optional] 
**mentions_time_window_in_hours** | **int** | The time window (in hours) used for generating user mentions. | [optional] 

## Example

```python
from openapi_client.models.feed_response import FeedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeedResponse from a JSON string
feed_response_instance = FeedResponse.from_json(json)
# print the JSON string representation of the object
print(FeedResponse.to_json())

# convert the object into a dict
feed_response_dict = feed_response_instance.to_dict()
# create an instance of FeedResponse from a dict
feed_response_from_dict = FeedResponse.from_dict(feed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


