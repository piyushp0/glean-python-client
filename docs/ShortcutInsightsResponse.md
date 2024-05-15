# ShortcutInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_log_timestamp** | **int** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**shortcut_insights** | [**List[ShortcutInsight]**](ShortcutInsight.md) | Insights for shortcuts. | [optional] 
**departments** | **List[str]** | list of departments applicable for shortcuts tab. | [optional] 
**min_visitor_threshold** | **int** | Min threshold in number of visitors while populating results, otherwise 0. | [optional] 

## Example

```python
from openapi_client.models.shortcut_insights_response import ShortcutInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShortcutInsightsResponse from a JSON string
shortcut_insights_response_instance = ShortcutInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(ShortcutInsightsResponse.to_json())

# convert the object into a dict
shortcut_insights_response_dict = shortcut_insights_response_instance.to_dict()
# create an instance of ShortcutInsightsResponse from a dict
shortcut_insights_response_from_dict = ShortcutInsightsResponse.from_dict(shortcut_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


