# RecommendationsRequestOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_filter** | **str** | Filter results to a single datasource name (e.g. gmail, slack). All results are returned if missing. | [optional] 
**datasources_filter** | **List[str]** | Filter results to only those relevant to one or more datasources (e.g. jira, gdrive). All results are returned if missing. | [optional] 
**context** | [**Document**](Document.md) |  | [optional] 
**result_prominence** | [**List[SearchResultProminenceEnum]**](SearchResultProminenceEnum.md) | The types of prominence wanted in results returned. Default is any type. | [optional] 

## Example

```python
from openapi_client.models.recommendations_request_options import RecommendationsRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationsRequestOptions from a JSON string
recommendations_request_options_instance = RecommendationsRequestOptions.from_json(json)
# print the JSON string representation of the object
print(RecommendationsRequestOptions.to_json())

# convert the object into a dict
recommendations_request_options_dict = recommendations_request_options_instance.to_dict()
# create an instance of RecommendationsRequestOptions from a dict
recommendations_request_options_from_dict = RecommendationsRequestOptions.from_dict(recommendations_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


