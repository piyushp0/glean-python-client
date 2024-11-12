# DownloadInsightsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Categories of data requested. Request can include single or multiple types. | 
**departments** | **List[str]** | Departments that the data is requested for. If this is empty, corresponds to whole company. | [optional] 
**day_range** | [**Period**](Period.md) |  | [optional] 
**ai_app_request_options** | [**InsightsAiAppRequestOptions**](InsightsAiAppRequestOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.download_insights_request import DownloadInsightsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadInsightsRequest from a JSON string
download_insights_request_instance = DownloadInsightsRequest.from_json(json)
# print the JSON string representation of the object
print(DownloadInsightsRequest.to_json())

# convert the object into a dict
download_insights_request_dict = download_insights_request_instance.to_dict()
# create an instance of DownloadInsightsRequest from a dict
download_insights_request_from_dict = DownloadInsightsRequest.from_dict(download_insights_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


