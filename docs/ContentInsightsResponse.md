# ContentInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_log_timestamp** | **int** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**document_insights** | [**List[DocumentInsight]**](DocumentInsight.md) | Insights for documents. | [optional] 
**departments** | **List[str]** | list of departments applicable for contents tab. | [optional] 
**min_department_size_threshold** | **int** | Min threshold in size of departments while populating results, otherwise 0. | [optional] 
**min_visitor_threshold** | **int** | Minimum number of visitors to a document required to be included in insights. | [optional] 

## Example

```python
from openapi_client.models.content_insights_response import ContentInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentInsightsResponse from a JSON string
content_insights_response_instance = ContentInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(ContentInsightsResponse.to_json())

# convert the object into a dict
content_insights_response_dict = content_insights_response_instance.to_dict()
# create an instance of ContentInsightsResponse from a dict
content_insights_response_from_dict = ContentInsightsResponse.from_dict(content_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


