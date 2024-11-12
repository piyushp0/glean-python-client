# AddCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** | the datasource the credential applies to | [optional] 
**datasource_instance** | **str** | the datasource instance the credential applies to | [optional] 
**user** | **str** | the user info (email or username for example) for the credential | [optional] 
**token** | **str** | the token part of the credential (password, apiToken etc) | [optional] 
**metadata** | **str** | any metadata associated with the user credential | [optional] 

## Example

```python
from openapi_client.models.add_credential_request import AddCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCredentialRequest from a JSON string
add_credential_request_instance = AddCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(AddCredentialRequest.to_json())

# convert the object into a dict
add_credential_request_dict = add_credential_request_instance.to_dict()
# create an instance of AddCredentialRequest from a dict
add_credential_request_from_dict = AddCredentialRequest.from_dict(add_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


