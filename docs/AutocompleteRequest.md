# AutocompleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_token** | **str** |  | [optional] 
**session_info** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**query** | **str** | Partially typed query. | [optional] 
**datasources_filter** | **List[str]** | Filter results to only those relevant to one or more datasources (e.g. jira, gdrive). Results are unfiltered if missing. | [optional] 
**datasource** | **str** | Filter to only return results relevant to the given datasource. | [optional] 
**result_types** | **List[str]** | Filter to only return results of the given type(s). All types may be returned if omitted. | [optional] 
**result_size** | **int** | Maximum number of results to be returned. If no value is provided, the backend will cap at 200.  | [optional] 
**auth_tokens** | [**List[AuthToken]**](AuthToken.md) | Auth tokens which may be used for federated results. | [optional] 

## Example

```python
from openapi_client.models.autocomplete_request import AutocompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteRequest from a JSON string
autocomplete_request_instance = AutocompleteRequest.from_json(json)
# print the JSON string representation of the object
print(AutocompleteRequest.to_json())

# convert the object into a dict
autocomplete_request_dict = autocomplete_request_instance.to_dict()
# create an instance of AutocompleteRequest from a dict
autocomplete_request_from_dict = AutocompleteRequest.from_dict(autocomplete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


