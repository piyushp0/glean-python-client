# DisplayableListItemUIConfig

UI configurations for each item of the list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_new_indicator** | **bool** | show a \&quot;New\&quot; pill next to the item | [optional] 

## Example

```python
from openapi_client.models.displayable_list_item_ui_config import DisplayableListItemUIConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayableListItemUIConfig from a JSON string
displayable_list_item_ui_config_instance = DisplayableListItemUIConfig.from_json(json)
# print the JSON string representation of the object
print(DisplayableListItemUIConfig.to_json())

# convert the object into a dict
displayable_list_item_ui_config_dict = displayable_list_item_ui_config_instance.to_dict()
# create an instance of DisplayableListItemUIConfig from a dict
displayable_list_item_ui_config_from_dict = DisplayableListItemUIConfig.from_dict(displayable_list_item_ui_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


