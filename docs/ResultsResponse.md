# ResultsResponse


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

## Example

```python
from openapi_client.models.results_response import ResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsResponse from a JSON string
results_response_instance = ResultsResponse.from_json(json)
# print the JSON string representation of the object
print(ResultsResponse.to_json())

# convert the object into a dict
results_response_dict = results_response_instance.to_dict()
# create an instance of ResultsResponse from a dict
results_response_from_dict = ResultsResponse.from_dict(results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


