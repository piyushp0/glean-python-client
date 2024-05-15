# CreateAuthTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | An authentication token that can be passed to any endpoint via Bearer Authentication | 
**expiration_time** | **int** | Unix timestamp for when this token expires (in seconds since epoch UTC). | 

## Example

```python
from openapi_client.models.create_auth_token_response import CreateAuthTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthTokenResponse from a JSON string
create_auth_token_response_instance = CreateAuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAuthTokenResponse.to_json())

# convert the object into a dict
create_auth_token_response_dict = create_auth_token_response_instance.to_dict()
# create an instance of CreateAuthTokenResponse from a dict
create_auth_token_response_from_dict = CreateAuthTokenResponse.from_dict(create_auth_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


