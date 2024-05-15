# SearchResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rewritten_query** | **str** | A cleaned up or updated version of the query to be displayed in the query box. Useful for mapping visual facets to search operators. | [optional] 
**searched_query** | **str** | The actual query used to perform search and return results. | [optional] 
**searched_query_ranges** | [**List[TextRange]**](TextRange.md) | The bolded ranges within the searched query. | [optional] 
**original_query** | **str** | The query text sent by the client in the request. | [optional] 
**query_suggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**additional_query_suggestions** | [**QuerySuggestionList**](QuerySuggestionList.md) |  | [optional] 
**negated_terms** | **List[str]** | A list of terms that were negated when processing the query. | [optional] 
**modified_query_was_used** | **bool** | A different query was performed than the one requested. | [optional] 
**original_query_had_no_results** | **bool** | No results were found for the original query. The usage of this bit in conjunction with modifiedQueryWasUsed will dictate whether the full page replacement is 0-result or few-result based. | [optional] 
**search_warning** | [**SearchWarning**](SearchWarning.md) |  | [optional] 
**triggered_expert_detection** | **bool** | Whether the query triggered expert detection results in the People tab. | [optional] 

## Example

```python
from openapi_client.models.search_response_metadata import SearchResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseMetadata from a JSON string
search_response_metadata_instance = SearchResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(SearchResponseMetadata.to_json())

# convert the object into a dict
search_response_metadata_dict = search_response_metadata_instance.to_dict()
# create an instance of SearchResponseMetadata from a dict
search_response_metadata_from_dict = SearchResponseMetadata.from_dict(search_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


