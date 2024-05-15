# CustomFieldData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | A user-facing label for this field. | 
**values** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | 
**displayable** | **bool** | Determines whether the client should display this custom field | [default to True]

## Example

```python
from openapi_client.models.custom_field_data import CustomFieldData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldData from a JSON string
custom_field_data_instance = CustomFieldData.from_json(json)
# print the JSON string representation of the object
print(CustomFieldData.to_json())

# convert the object into a dict
custom_field_data_dict = custom_field_data_instance.to_dict()
# create an instance of CustomFieldData from a dict
custom_field_data_from_dict = CustomFieldData.from_dict(custom_field_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


