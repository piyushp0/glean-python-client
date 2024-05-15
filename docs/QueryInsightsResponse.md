# QueryInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_log_timestamp** | **int** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**query_insights** | [**List[QueryInsight]**](QueryInsight.md) | Insights for queries. | [optional] 
**low_performing_query_insights** | [**List[QueryInsight]**](QueryInsight.md) | Insights for low performing queries without good results. | [optional] 
**departments** | **List[str]** | list of departments applicable for queries tab. | [optional] 
**min_visitor_threshold** | **int** | Min threshold in number of visitors while populating results, otherwise 0. | [optional] 

## Example

```python
from openapi_client.models.query_insights_response import QueryInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryInsightsResponse from a JSON string
query_insights_response_instance = QueryInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(QueryInsightsResponse.to_json())

# convert the object into a dict
query_insights_response_dict = query_insights_response_instance.to_dict()
# create an instance of QueryInsightsResponse from a dict
query_insights_response_from_dict = QueryInsightsResponse.from_dict(query_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


