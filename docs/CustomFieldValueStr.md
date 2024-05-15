# CustomFieldValueStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**str_text** | **str** | Text field for string value. | [optional] 

## Example

```python
from openapi_client.models.custom_field_value_str import CustomFieldValueStr

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldValueStr from a JSON string
custom_field_value_str_instance = CustomFieldValueStr.from_json(json)
# print the JSON string representation of the object
print(CustomFieldValueStr.to_json())

# convert the object into a dict
custom_field_value_str_dict = custom_field_value_str_instance.to_dict()
# create an instance of CustomFieldValueStr from a dict
custom_field_value_str_from_dict = CustomFieldValueStr.from_dict(custom_field_value_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


