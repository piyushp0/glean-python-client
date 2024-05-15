# UserActivityInsight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**Person**](Person.md) |  | 
**activity** | **str** | Activity e.g. search, home page visit or all. | 
**last_activity_timestamp** | **int** | Unix timestamp of the last activity (in seconds since epoch UTC). | [optional] 
**activity_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**active_day_count** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_activity_insight import UserActivityInsight

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivityInsight from a JSON string
user_activity_insight_instance = UserActivityInsight.from_json(json)
# print the JSON string representation of the object
print(UserActivityInsight.to_json())

# convert the object into a dict
user_activity_insight_dict = user_activity_insight_instance.to_dict()
# create an instance of UserActivityInsight from a dict
user_activity_insight_from_dict = UserActivityInsight.from_dict(user_activity_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


