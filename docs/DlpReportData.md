# DlpReportData

Dlp report metadata which is used to construct report email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | The frequency of the report | [optional] 
**request_time** | **datetime** | The time the report was requested, applicable only for one time reports | [optional] 
**report_name** | **str** |  | [optional] 
**status** | [**DlpSimpleResult**](DlpSimpleResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.dlp_report_data import DlpReportData

# TODO update the JSON string below
json = "{}"
# create an instance of DlpReportData from a JSON string
dlp_report_data_instance = DlpReportData.from_json(json)
# print the JSON string representation of the object
print(DlpReportData.to_json())

# convert the object into a dict
dlp_report_data_dict = dlp_report_data_instance.to_dict()
# create an instance of DlpReportData from a dict
dlp_report_data_from_dict = DlpReportData.from_dict(dlp_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


