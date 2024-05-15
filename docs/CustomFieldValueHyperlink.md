# CustomFieldValueHyperlink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_anchor** | **str** | Anchor text for hyperlink. | [optional] 
**url_link** | **str** | Link for this URL. | [optional] 

## Example

```python
from openapi_client.models.custom_field_value_hyperlink import CustomFieldValueHyperlink

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldValueHyperlink from a JSON string
custom_field_value_hyperlink_instance = CustomFieldValueHyperlink.from_json(json)
# print the JSON string representation of the object
print(CustomFieldValueHyperlink.to_json())

# convert the object into a dict
custom_field_value_hyperlink_dict = custom_field_value_hyperlink_instance.to_dict()
# create an instance of CustomFieldValueHyperlink from a dict
custom_field_value_hyperlink_from_dict = CustomFieldValueHyperlink.from_dict(custom_field_value_hyperlink_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


