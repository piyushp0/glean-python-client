# GetDocPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_user_emails** | **List[str]** | A list of emails of users who have access to the document. If the document is visible to all Glean users, a list with only a single value of &#39;VISIBLE_TO_ALL&#39;. | [optional] 

## Example

```python
from openapi_client.models.get_doc_permissions_response import GetDocPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocPermissionsResponse from a JSON string
get_doc_permissions_response_instance = GetDocPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocPermissionsResponse.to_json())

# convert the object into a dict
get_doc_permissions_response_dict = get_doc_permissions_response_instance.to_dict()
# create an instance of GetDocPermissionsResponse from a dict
get_doc_permissions_response_from_dict = GetDocPermissionsResponse.from_dict(get_doc_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


