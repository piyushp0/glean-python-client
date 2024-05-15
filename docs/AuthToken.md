# AuthToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**datasource** | **str** |  | 
**scope** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**auth_user** | **str** | Used by Google to indicate the index of the logged in user. Useful for generating hyperlinks that support multilogin. | [optional] 
**expiration** | **int** | Unix timestamp when this token expires (in seconds since epoch UTC). | [optional] 

## Example

```python
from openapi_client.models.auth_token import AuthToken

# TODO update the JSON string below
json = "{}"
# create an instance of AuthToken from a JSON string
auth_token_instance = AuthToken.from_json(json)
# print the JSON string representation of the object
print(AuthToken.to_json())

# convert the object into a dict
auth_token_dict = auth_token_instance.to_dict()
# create an instance of AuthToken from a dict
auth_token_from_dict = AuthToken.from_dict(auth_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


