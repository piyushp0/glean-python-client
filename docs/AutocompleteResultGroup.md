# AutocompleteResultGroup

A subsection of the results list from which distinct sections should be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** | The inclusive start index of the range. | [optional] 
**end_index** | **int** | The exclusive end index of the range. | [optional] 
**title** | **str** | The title of the result group to be displayed. Empty means no title. | [optional] 

## Example

```python
from openapi_client.models.autocomplete_result_group import AutocompleteResultGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteResultGroup from a JSON string
autocomplete_result_group_instance = AutocompleteResultGroup.from_json(json)
# print the JSON string representation of the object
print(AutocompleteResultGroup.to_json())

# convert the object into a dict
autocomplete_result_group_dict = autocomplete_result_group_instance.to_dict()
# create an instance of AutocompleteResultGroup from a dict
autocomplete_result_group_from_dict = AutocompleteResultGroup.from_dict(autocomplete_result_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


