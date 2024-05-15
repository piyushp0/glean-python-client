# CustomEntityMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data** | [**Dict[str, CustomDataValue]**](CustomDataValue.md) | Custom fields specific to individual datasources | [optional] 

## Example

```python
from openapi_client.models.custom_entity_metadata import CustomEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityMetadata from a JSON string
custom_entity_metadata_instance = CustomEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(CustomEntityMetadata.to_json())

# convert the object into a dict
custom_entity_metadata_dict = custom_entity_metadata_instance.to_dict()
# create an instance of CustomEntityMetadata from a dict
custom_entity_metadata_from_dict = CustomEntityMetadata.from_dict(custom_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


