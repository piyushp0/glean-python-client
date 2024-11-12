# InsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeseries** | [**List[LabeledCountInfo]**](LabeledCountInfo.md) | List of timeseries to make charts (if applicable). | [optional] 
**users** | [**UserInsightsResponse**](UserInsightsResponse.md) |  | [optional] 
**content** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**queries** | [**QueryInsightsResponse**](QueryInsightsResponse.md) |  | [optional] 
**collections** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**collections_v2** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**shortcuts** | [**ShortcutInsightsResponse**](ShortcutInsightsResponse.md) |  | [optional] 
**announcements** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**answers** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**ai** | [**AiInsightsResponse**](AiInsightsResponse.md) |  | [optional] 
**ai_apps** | [**AiAppsInsightsResponse**](AiAppsInsightsResponse.md) |  | [optional] 
**glean_assist** | [**GleanAssistInsightsResponse**](GleanAssistInsightsResponse.md) |  | [optional] 
**departments** | **List[str]** | list of all departments. | [optional] 

## Example

```python
from openapi_client.models.insights_response import InsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsResponse from a JSON string
insights_response_instance = InsightsResponse.from_json(json)
# print the JSON string representation of the object
print(InsightsResponse.to_json())

# convert the object into a dict
insights_response_dict = insights_response_instance.to_dict()
# create an instance of InsightsResponse from a dict
insights_response_from_dict = InsightsResponse.from_dict(insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


