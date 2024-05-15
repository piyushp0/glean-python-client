# DisplayableListConfig

UI specific configurations for a displayable list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | defines how to render this particular displayable list card | [optional] 
**title** | **str** | Primary title for the list. | [optional] 
**enabled** | **bool** | Whether the list should be shown to the user | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should should see displayable list | [optional] 
**item_ui_config** | [**DisplayableListItemUIConfig**](DisplayableListItemUIConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.displayable_list_config import DisplayableListConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayableListConfig from a JSON string
displayable_list_config_instance = DisplayableListConfig.from_json(json)
# print the JSON string representation of the object
print(DisplayableListConfig.to_json())

# convert the object into a dict
displayable_list_config_dict = displayable_list_config_instance.to_dict()
# create an instance of DisplayableListConfig from a dict
displayable_list_config_from_dict = DisplayableListConfig.from_dict(displayable_list_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


