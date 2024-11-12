# FeedRequestOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_size** | **int** | Number of results asked in response. If a result is a collection, counts as one. | 
**timezone_offset** | **int** | The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 
**category_to_result_size** | [**Dict[str, FeedRequestOptionsCategoryToResultSizeValue]**](FeedRequestOptionsCategoryToResultSizeValue.md) | Mapping from category to number of results asked for the category. | [optional] 
**datasource_filter** | **List[str]** | Datasources for which content should be included. Empty is for all. | [optional] 
**chat_zero_state_suggestion_options** | [**ChatZeroStateSuggestionOptions**](ChatZeroStateSuggestionOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.feed_request_options import FeedRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FeedRequestOptions from a JSON string
feed_request_options_instance = FeedRequestOptions.from_json(json)
# print the JSON string representation of the object
print(FeedRequestOptions.to_json())

# convert the object into a dict
feed_request_options_dict = feed_request_options_instance.to_dict()
# create an instance of FeedRequestOptions from a dict
feed_request_options_from_dict = FeedRequestOptions.from_dict(feed_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


