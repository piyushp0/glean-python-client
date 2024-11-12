# SearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structured_results** | [**List[StructuredResult]**](StructuredResult.md) | An array of entities in the work graph retrieved via a data request. | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | 
**native_app_url** | **str** | A deep link, if available, into the datasource&#39;s native application for the user&#39;s platform (e.g. slack://...). | [optional] 
**snippets** | [**List[SearchResultSnippet]**](SearchResultSnippet.md) | Text content from the result document which contains search query terms, if available. | [optional] 
**expanded_snippets** | **List[str]** | The expanded snippets for this result. This is only populated if the query has the expand_snippets parameter set to true. | [optional] 
**full_text** | **str** | The full body text of the result if not already contained in the snippets | [optional] 
**full_text_list** | **List[str]** | The full body text of the result if not already contained in the snippets; each item in the array represents a separate line in the original text | [optional] 
**related_results** | [**List[RelatedDocuments]**](RelatedDocuments.md) | A list of results related to this search result. Eg. for conversation results it contains individual messages from the conversation document which will be shown on SERP. | [optional] 
**clustered_results** | [**List[SearchResult]**](SearchResult.md) | A list of results that should be displayed as associated with this result. | [optional] 
**all_clustered_results** | [**List[ClusterGroup]**](ClusterGroup.md) | A list of results that should be displayed as associated with this result. | [optional] 
**attachment_count** | **int** | The total number of attachments. | [optional] 
**attachments** | [**List[SearchResult]**](SearchResult.md) | A (potentially partial) list of results representing documents attached to the main result document. | [optional] 
**backlink_results** | [**List[SearchResult]**](SearchResult.md) | A list of results that should be displayed as backlinks of this result in reverse chronological order. | [optional] 
**cluster_type** | [**ClusterTypeEnum**](ClusterTypeEnum.md) |  | [optional] 
**must_include_suggestions** | [**QuerySuggestionList**](QuerySuggestionList.md) |  | [optional] 
**query_suggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**prominence** | [**SearchResultProminenceEnum**](SearchResultProminenceEnum.md) |  | [optional] 
**attachment_context** | **str** | Additional context for the relationship between the result and the document it&#39;s attached to. | [optional] 
**pins** | [**List[PinDocument]**](PinDocument.md) | A list of pins associated with this search result. | [optional] 

## Example

```python
from openapi_client.models.search_result import SearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResult from a JSON string
search_result_instance = SearchResult.from_json(json)
# print the JSON string representation of the object
print(SearchResult.to_json())

# convert the object into a dict
search_result_dict = search_result_instance.to_dict()
# create an instance of SearchResult from a dict
search_result_from_dict = SearchResult.from_dict(search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


