# ResultsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The ISO 8601 timestamp associated with the client request. | [optional] 
**tracking_token** | **str** | A previously received trackingToken for a search associated with the same query. Useful for more requests and requests for other tabs. | [optional] 
**session_info** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**source_document** | [**Document**](Document.md) |  | [optional] 
**page_size** | **int** | Hint to the server about how many results to send back. Server may return less or more. Structured results and clustered results don&#39;t count towards pageSize. | [optional] 
**max_snippet_size** | **int** | Hint to the server about how many characters long a snippet may be. Server may return less or more. | [optional] 

## Example

```python
from openapi_client.models.results_request import ResultsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsRequest from a JSON string
results_request_instance = ResultsRequest.from_json(json)
# print the JSON string representation of the object
print(ResultsRequest.to_json())

# convert the object into a dict
results_request_dict = results_request_instance.to_dict()
# create an instance of ResultsRequest from a dict
results_request_from_dict = ResultsRequest.from_dict(results_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


