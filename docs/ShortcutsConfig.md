# ShortcutsConfig

Configuration settings related to Shortcuts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortcuts_prefix** | **str** | Deployment&#39;s prefix for shortcuts. | [optional] 
**use_external_shortcuts** | **bool** | Whether the deployment uses external shortcuts. | [optional] 

## Example

```python
from openapi_client.models.shortcuts_config import ShortcutsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ShortcutsConfig from a JSON string
shortcuts_config_instance = ShortcutsConfig.from_json(json)
# print the JSON string representation of the object
print(ShortcutsConfig.to_json())

# convert the object into a dict
shortcuts_config_dict = shortcuts_config_instance.to_dict()
# create an instance of ShortcutsConfig from a dict
shortcuts_config_from_dict = ShortcutsConfig.from_dict(shortcuts_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


