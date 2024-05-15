# UserInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_log_timestamp** | **int** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**activity_insights** | [**List[UserActivityInsight]**](UserActivityInsight.md) | Insights for all active users with respect to set of actions. | [optional] 
**inactive_insights** | [**List[UserActivityInsight]**](UserActivityInsight.md) | Insights for all in inactive users with respect to set of actions and time period. Activity count will be set to 0. | [optional] 
**total_teammates** | **int** | Total number of teammates that have logged in to the product, that are still valid teammates. | [optional] 
**total_active_users** | **int** | Total number of active users in the requested period. | [optional] 
**departments** | **List[str]** | list of departments applicable for users tab. | [optional] 

## Example

```python
from openapi_client.models.user_insights_response import UserInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserInsightsResponse from a JSON string
user_insights_response_instance = UserInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(UserInsightsResponse.to_json())

# convert the object into a dict
user_insights_response_dict = user_insights_response_instance.to_dict()
# create an instance of UserInsightsResponse from a dict
user_insights_response_from_dict = UserInsightsResponse.from_dict(user_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


