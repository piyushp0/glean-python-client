# GetDocPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | The Glean Document ID to retrieve permissions for. | [optional] 

## Example

```python
from openapi_client.models.get_doc_permissions_request import GetDocPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocPermissionsRequest from a JSON string
get_doc_permissions_request_instance = GetDocPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetDocPermissionsRequest.to_json())

# convert the object into a dict
get_doc_permissions_request_dict = get_doc_permissions_request_instance.to_dict()
# create an instance of GetDocPermissionsRequest from a dict
get_doc_permissions_request_from_dict = GetDocPermissionsRequest.from_dict(get_doc_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


