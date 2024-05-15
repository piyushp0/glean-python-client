# AuthConfig

Config for tool's authentication method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_on_prem** | **bool** | Whether or not this tool is hosted on-premise. | [optional] 
**type** | **str** | The type of authentication being used. Use &#39;OAUTH_*&#39; when Glean calls an external API (e.g., Jira) on behalf of a user to obtain an OAuth token. &#39;OAUTH_ADMIN&#39; utilizes an admin token for external API calls on behalf all users. &#39;OAUTH_USER&#39; uses individual user tokens for external API calls. | [optional] 
**status** | **str** | Auth status of the tool. | [optional] 
**client_url** | **str** | The URL where users will be directed to start the OAuth flow. | [optional] 
**scopes** | **List[str]** | A list of strings denoting the different scopes or access levels required by the tool. | [optional] 
**authorization_url** | **str** | The OAuth provider&#39;s endpoint, where access tokens are requested. | [optional] 

## Example

```python
from openapi_client.models.auth_config import AuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuthConfig from a JSON string
auth_config_instance = AuthConfig.from_json(json)
# print the JSON string representation of the object
print(AuthConfig.to_json())

# convert the object into a dict
auth_config_dict = auth_config_instance.to_dict()
# create an instance of AuthConfig from a dict
auth_config_from_dict = AuthConfig.from_dict(auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


