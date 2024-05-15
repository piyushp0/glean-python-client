# InsightsAiAppRequestOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_app_ids** | **List[str]** | IDs of the AI Apps for which Insights should be returned. An empty array signifies all. | [optional] 

## Example

```python
from openapi_client.models.insights_ai_app_request_options import InsightsAiAppRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsAiAppRequestOptions from a JSON string
insights_ai_app_request_options_instance = InsightsAiAppRequestOptions.from_json(json)
# print the JSON string representation of the object
print(InsightsAiAppRequestOptions.to_json())

# convert the object into a dict
insights_ai_app_request_options_dict = insights_ai_app_request_options_instance.to_dict()
# create an instance of InsightsAiAppRequestOptions from a dict
insights_ai_app_request_options_from_dict = InsightsAiAppRequestOptions.from_dict(insights_ai_app_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


