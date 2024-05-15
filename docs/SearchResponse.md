# SearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_token** | **str** | A token that should be passed for additional requests related to this request (such as more results requests). | [optional] 
**session_info** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**results** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**structured_results** | [**List[StructuredResult]**](StructuredResult.md) |  | [optional] 
**generated_qna_result** | [**GeneratedQna**](GeneratedQna.md) |  | [optional] 
**error_info** | [**ErrorInfo**](ErrorInfo.md) |  | [optional] 
**request_id** | **str** | A platform-generated request ID to correlate backend logs. | [optional] 
**backend_time_millis** | **int** | Time in milliseconds the backend took to respond to the request. | [optional] 
**experiment_ids** | **List[int]** | List of experiment ids for the corresponding request. | [optional] 
**metadata** | [**SearchResponseMetadata**](SearchResponseMetadata.md) |  | [optional] 
**facet_results** | [**List[FacetResult]**](FacetResult.md) |  | [optional] 
**result_tabs** | [**List[ResultTab]**](ResultTab.md) | All result tabs available for the current query. Populated if QUERY_METADATA is specified in the request. | [optional] 
**result_tab_ids** | **List[str]** | The unique IDs of the result tabs to which this response belongs. | [optional] 
**results_description** | [**ResultsDescription**](ResultsDescription.md) |  | [optional] 
**rewritten_facet_filters** | [**List[FacetFilter]**](FacetFilter.md) | The actual applied facet filters based on the operators and facetFilters in the query. Useful for mapping typed operators to visual facets. | [optional] 
**cursor** | **str** | Cursor that indicates the start of the next page of results. To be passed in \&quot;more\&quot; requests for this query. | [optional] 
**has_more_results** | **bool** | Whether more results are available. Use cursor to retrieve them. | [optional] 

## Example

```python
from openapi_client.models.search_response import SearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponse from a JSON string
search_response_instance = SearchResponse.from_json(json)
# print the JSON string representation of the object
print(SearchResponse.to_json())

# convert the object into a dict
search_response_dict = search_response_instance.to_dict()
# create an instance of SearchResponse from a dict
search_response_from_dict = SearchResponse.from_dict(search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


