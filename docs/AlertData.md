# AlertData

Admin alert related information that is used to construct the admin alert email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the admin alert | [optional] 
**triggered_time** | **datetime** | The time that the alert was triggered | [optional] 
**project_name** | **str** | Human readable name of the project instance | [optional] 
**help_link** | **str** | Help link for the alert that the admin can reference | [optional] 
**datasource** | **str** | Datasource that the alert is related to (possibly null) | [optional] 

## Example

```python
from openapi_client.models.alert_data import AlertData

# TODO update the JSON string below
json = "{}"
# create an instance of AlertData from a JSON string
alert_data_instance = AlertData.from_json(json)
# print the JSON string representation of the object
print(AlertData.to_json())

# convert the object into a dict
alert_data_dict = alert_data_instance.to_dict()
# create an instance of AlertData from a dict
alert_data_from_dict = AlertData.from_dict(alert_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


