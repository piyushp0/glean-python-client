# ActivityEventParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_content** | **str** | The HTML content of the page body. | [optional] 
**datasource_instance** | **str** | The full datasource instance name inferred from the URL of the event | [optional] 
**datasource** | **str** | The datasource without the instance inferred from the URL of the event | [optional] 
**instance_only_name** | **str** | The instance only name of the datasource instance, e.g. 1 for jira_1, inferred from the URL of the event | [optional] 
**duration** | **int** | Length in seconds of the activity. For VIEWS, this represents the amount the page was visible in the foreground. | [optional] 
**query** | **str** | The user&#39;s search query associated with a SEARCH. | [optional] 
**referrer** | **str** | The referring URL of the VIEW or SEARCH. | [optional] 
**title** | **str** | The page title associated with the URL of the event | [optional] 
**truncated** | **bool** | Indicates that the parameters are incomplete and more parameters may be sent with the same action+timestamp+URL in the future. This is used for sending the duration when a &#x60;VIEW&#x60; is finished. | [optional] 

## Example

```python
from openapi_client.models.activity_event_params import ActivityEventParams

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityEventParams from a JSON string
activity_event_params_instance = ActivityEventParams.from_json(json)
# print the JSON string representation of the object
print(ActivityEventParams.to_json())

# convert the object into a dict
activity_event_params_dict = activity_event_params_instance.to_dict()
# create an instance of ActivityEventParams from a dict
activity_event_params_from_dict = ActivityEventParams.from_dict(activity_event_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


