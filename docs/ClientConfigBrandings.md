# ClientConfigBrandings

Branding customizations applicable to the current user, such as custom company logos and background images for light and dark mode or company-specific product terminology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light** | [**Branding**](Branding.md) |  | [optional] 
**dark** | [**Branding**](Branding.md) |  | [optional] 
**product_terms** | [**ProductTerms**](ProductTerms.md) |  | [optional] 

## Example

```python
from openapi_client.models.client_config_brandings import ClientConfigBrandings

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConfigBrandings from a JSON string
client_config_brandings_instance = ClientConfigBrandings.from_json(json)
# print the JSON string representation of the object
print(ClientConfigBrandings.to_json())

# convert the object into a dict
client_config_brandings_dict = client_config_brandings_instance.to_dict()
# create an instance of ClientConfigBrandings from a dict
client_config_brandings_from_dict = ClientConfigBrandings.from_dict(client_config_brandings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


