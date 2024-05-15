# SearchResultSnippet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snippet** | **str** | A matching snippet from the document. Query term matches are marked by the unicode characters uE006 and uE007. | 
**mime_type** | **str** | The mime type of the snippets, currently either text/plain or text/html. | [optional] 
**text** | **str** | A matching snippet from the document with no highlights. | [optional] 
**snippet_text_ordering** | **int** | Used for sorting based off the snippet&#39;s location within all_snippetable_text | [optional] 
**ranges** | [**List[TextRange]**](TextRange.md) | The bolded ranges within text. | [optional] 
**url** | **str** | A URL, generated based on availability, that links to the position of the snippet text or to the nearest header above the snippet text. | [optional] 

## Example

```python
from openapi_client.models.search_result_snippet import SearchResultSnippet

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultSnippet from a JSON string
search_result_snippet_instance = SearchResultSnippet.from_json(json)
# print the JSON string representation of the object
print(SearchResultSnippet.to_json())

# convert the object into a dict
search_result_snippet_dict = search_result_snippet_instance.to_dict()
# create an instance of SearchResultSnippet from a dict
search_result_snippet_from_dict = SearchResultSnippet.from_dict(search_result_snippet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


