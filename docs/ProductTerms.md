# ProductTerms

Mapping of product terms to the term's description. These product terms should match their counterpart in productTerms.json

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant** | [**ProductTerm**](ProductTerm.md) |  | [optional] 
**glean_assistant** | [**ProductTerm**](ProductTerm.md) |  | [optional] 
**public_knowledge** | [**ProductTerm**](ProductTerm.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_terms import ProductTerms

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTerms from a JSON string
product_terms_instance = ProductTerms.from_json(json)
# print the JSON string representation of the object
print(ProductTerms.to_json())

# convert the object into a dict
product_terms_dict = product_terms_instance.to_dict()
# create an instance of ProductTerms from a dict
product_terms_from_dict = ProductTerms.from_dict(product_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


