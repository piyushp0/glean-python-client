# ProductTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**localizations** | [**Dict[str, ProductTermLocalizationsValue]**](ProductTermLocalizationsValue.md) | Mapping of locale to the display name of the product term. | [optional] 

## Example

```python
from openapi_client.models.product_term import ProductTerm

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTerm from a JSON string
product_term_instance = ProductTerm.from_json(json)
# print the JSON string representation of the object
print(ProductTerm.to_json())

# convert the object into a dict
product_term_dict = product_term_instance.to_dict()
# create an instance of ProductTerm from a dict
product_term_from_dict = ProductTerm.from_dict(product_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


