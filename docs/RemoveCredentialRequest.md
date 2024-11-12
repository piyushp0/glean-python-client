# RemoveCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** | the datasource the credential applies to | [optional] 
**datasource_instance** | **str** | the datasource instance the credential applies to | [optional] 
**user** | **str** | the user info (email or username for example) for the credential | [optional] 

## Example

```python
from openapi_client.models.remove_credential_request import RemoveCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCredentialRequest from a JSON string
remove_credential_request_instance = RemoveCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveCredentialRequest.to_json())

# convert the object into a dict
remove_credential_request_dict = remove_credential_request_instance.to_dict()
# create an instance of RemoveCredentialRequest from a dict
remove_credential_request_from_dict = RemoveCredentialRequest.from_dict(remove_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


