# InsightsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Categories of data requested. Request can include single or multiple types. | 
**departments** | **List[str]** | Departments that the data is requested for. If this is empty, corresponds to whole company. | [optional] 
**day_range** | [**Period**](Period.md) |  | [optional] 
**ai_app_request_options** | [**InsightsAiAppRequestOptions**](InsightsAiAppRequestOptions.md) |  | [optional] 
**assistant_activity_types** | **List[str]** | Types of activity that should count in the definition of an Assistant Active User. Affects only insights for AI category. | [optional] 
**disable_per_user_insights** | **bool** | If true, suppresses the generation of per-user Insights in the response. Default is false. | [optional] 

## Example

```python
from openapi_client.models.insights_request import InsightsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsRequest from a JSON string
insights_request_instance = InsightsRequest.from_json(json)
# print the JSON string representation of the object
print(InsightsRequest.to_json())

# convert the object into a dict
insights_request_dict = insights_request_instance.to_dict()
# create an instance of InsightsRequest from a dict
insights_request_from_dict = InsightsRequest.from_dict(insights_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


