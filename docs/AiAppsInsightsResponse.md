# AiAppsInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_log_timestamp** | **int** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**ai_app_insights** | [**List[UserActivityInsight]**](UserActivityInsight.md) |  | [optional] 
**total_active_users** | **int** | Total number of active users on the Ai App in the requested period. | [optional] 
**action_counts** | [**AiAppActionCounts**](AiAppActionCounts.md) |  | [optional] 
**departments** | **List[str]** | list of departments applicable for users tab. | [optional] 

## Example

```python
from openapi_client.models.ai_apps_insights_response import AiAppsInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiAppsInsightsResponse from a JSON string
ai_apps_insights_response_instance = AiAppsInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(AiAppsInsightsResponse.to_json())

# convert the object into a dict
ai_apps_insights_response_dict = ai_apps_insights_response_instance.to_dict()
# create an instance of AiAppsInsightsResponse from a dict
ai_apps_insights_response_from_dict = AiAppsInsightsResponse.from_dict(ai_apps_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


