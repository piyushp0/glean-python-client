# GetDocumentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_specs** | [**List[DocumentSpec]**](DocumentSpec.md) | The specification for the documents to be retrieved. | 
**include_fields** | **List[str]** | List of Document fields to return (that aren&#39;t returned by default) | [optional] 

## Example

```python
from openapi_client.models.get_documents_request import GetDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentsRequest from a JSON string
get_documents_request_instance = GetDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(GetDocumentsRequest.to_json())

# convert the object into a dict
get_documents_request_dict = get_documents_request_instance.to_dict()
# create an instance of GetDocumentsRequest from a dict
get_documents_request_from_dict = GetDocumentsRequest.from_dict(get_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


