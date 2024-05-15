# CustomDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_label** | **str** |  | [optional] 
**string_value** | **str** |  | [optional] 
**string_list_value** | **List[str]** | list of strings for multi-value properties | [optional] 
**number_value** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.custom_data_value import CustomDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataValue from a JSON string
custom_data_value_instance = CustomDataValue.from_json(json)
# print the JSON string representation of the object
print(CustomDataValue.to_json())

# convert the object into a dict
custom_data_value_dict = custom_data_value_instance.to_dict()
# create an instance of CustomDataValue from a dict
custom_data_value_from_dict = CustomDataValue.from_dict(custom_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


