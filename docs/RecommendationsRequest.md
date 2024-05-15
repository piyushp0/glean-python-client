# RecommendationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The ISO 8601 timestamp associated with the client request. | [optional] 
**tracking_token** | **str** | A previously received trackingToken for a search associated with the same query. Useful for more requests and requests for other tabs. | [optional] 
**session_info** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**source_document** | [**Document**](Document.md) |  | [optional] 
**page_size** | **int** | Hint to the server about how many results to send back. Server may return less or more. Structured results and clustered results don&#39;t count towards pageSize. | [optional] 
**max_snippet_size** | **int** | Hint to the server about how many characters long a snippet may be. Server may return less or more. | [optional] 
**recommendation_document_spec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**request_options** | [**RecommendationsRequestOptions**](RecommendationsRequestOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.recommendations_request import RecommendationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationsRequest from a JSON string
recommendations_request_instance = RecommendationsRequest.from_json(json)
# print the JSON string representation of the object
print(RecommendationsRequest.to_json())

# convert the object into a dict
recommendations_request_dict = recommendations_request_instance.to_dict()
# create an instance of RecommendationsRequest from a dict
recommendations_request_from_dict = RecommendationsRequest.from_dict(recommendations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


