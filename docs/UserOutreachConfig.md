# UserOutreachConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weekly_feed_email_enabled** | **bool** | Whether the weekly feed email is enabled | [optional] 
**onboarding_campaign_enabled** | **bool** | Whether the onboarding email campaign is enabled | [optional] 

## Example

```python
from openapi_client.models.user_outreach_config import UserOutreachConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UserOutreachConfig from a JSON string
user_outreach_config_instance = UserOutreachConfig.from_json(json)
# print the JSON string representation of the object
print(UserOutreachConfig.to_json())

# convert the object into a dict
user_outreach_config_dict = user_outreach_config_instance.to_dict()
# create an instance of UserOutreachConfig from a dict
user_outreach_config_from_dict = UserOutreachConfig.from_dict(user_outreach_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


