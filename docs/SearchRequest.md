# SearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The ISO 8601 timestamp associated with the client request. | [optional] 
**tracking_token** | **str** | A previously received trackingToken for a search associated with the same query. Useful for more requests and requests for other tabs. | [optional] 
**session_info** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**source_document** | [**Document**](Document.md) |  | [optional] 
**page_size** | **int** | Hint to the server about how many results to send back. Server may return less or more. Structured results and clustered results don&#39;t count towards pageSize. | [optional] 
**max_snippet_size** | **int** | Hint to the server about how many characters long a snippet may be. Server may return less or more. | [optional] 
**query** | **str** | The search terms. | 
**cursor** | **str** | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start. | [optional] 
**result_tab_ids** | **List[str]** | The unique IDs of the result tabs for which to fetch results. This will have precedence over datasource filters if both are specified and in conflict. | [optional] 
**input_details** | [**SearchRequestInputDetails**](SearchRequestInputDetails.md) |  | [optional] 
**request_options** | [**SearchRequestOptions**](SearchRequestOptions.md) |  | [optional] 
**timeout_millis** | **int** | Timeout in milliseconds for the request. A &#x60;408&#x60; error will be returned if handling the request takes longer. | [optional] 
**people** | [**List[Person]**](Person.md) | People associated with the search request. Hints to the server to fetch additional information for these people. Note that in this request, an email may be used as a person&#39;s obfuscatedId value. | [optional] 
**disable_spellcheck** | **bool** | Whether or not to disable spellcheck. | [optional] 

## Example

```python
from openapi_client.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print(SearchRequest.to_json())

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_from_dict = SearchRequest.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


