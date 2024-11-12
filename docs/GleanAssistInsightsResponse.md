# GleanAssistInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_log_timestamp** | **int** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**activity_insights** | [**List[UserActivityInsight]**](UserActivityInsight.md) | Insights for all active users with respect to set of actions. | [optional] 
**total_active_users** | **int** | Total number of active users in the requested period. | [optional] 
**datasource_instances** | **List[str]** | List of datasource instances for which glean assist is enabled. | [optional] 

## Example

```python
from openapi_client.models.glean_assist_insights_response import GleanAssistInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GleanAssistInsightsResponse from a JSON string
glean_assist_insights_response_instance = GleanAssistInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(GleanAssistInsightsResponse.to_json())

# convert the object into a dict
glean_assist_insights_response_dict = glean_assist_insights_response_instance.to_dict()
# create an instance of GleanAssistInsightsResponse from a dict
glean_assist_insights_response_from_dict = GleanAssistInsightsResponse.from_dict(glean_assist_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


