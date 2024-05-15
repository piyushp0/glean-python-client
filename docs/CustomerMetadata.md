# CustomerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_id** | **str** | The user visible id of the salesforce customer account. | [optional] 
**custom_data** | [**Dict[str, CustomDataValue]**](CustomDataValue.md) | Custom fields specific to individual datasources | [optional] 

## Example

```python
from openapi_client.models.customer_metadata import CustomerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerMetadata from a JSON string
customer_metadata_instance = CustomerMetadata.from_json(json)
# print the JSON string representation of the object
print(CustomerMetadata.to_json())

# convert the object into a dict
customer_metadata_dict = customer_metadata_instance.to_dict()
# create an instance of CustomerMetadata from a dict
customer_metadata_from_dict = CustomerMetadata.from_dict(customer_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


