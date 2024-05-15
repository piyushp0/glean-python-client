# Quicklink

An action for a specific datasource that will show up in autocomplete and app card, e.g. \"Create new issue\" for jira.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full action name. Used in autocomplete. | [optional] 
**short_name** | **str** | Shortened name. Used in app cards. | [optional] 
**url** | **str** | The URL of the action. | [optional] 
**icon_config** | [**IconConfig**](IconConfig.md) |  | [optional] 
**id** | **str** | Unique identifier of this quicklink | [optional] 
**scopes** | **List[str]** | The scopes for which this quicklink is applicable | [optional] 

## Example

```python
from openapi_client.models.quicklink import Quicklink

# TODO update the JSON string below
json = "{}"
# create an instance of Quicklink from a JSON string
quicklink_instance = Quicklink.from_json(json)
# print the JSON string representation of the object
print(Quicklink.to_json())

# convert the object into a dict
quicklink_dict = quicklink_instance.to_dict()
# create an instance of Quicklink from a dict
quicklink_from_dict = Quicklink.from_dict(quicklink_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


