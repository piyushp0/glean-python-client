# GetDocumentsByFacetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[Document]**](Document.md) | The document details, ordered by score. | [optional] 
**has_more_results** | **bool** | Whether more results are available. Use cursor to retrieve them. | [optional] 
**cursor** | **str** | Cursor that indicates the start of the next page of results. To be passed in \&quot;more\&quot; requests for this query. | [optional] 

## Example

```python
from openapi_client.models.get_documents_by_facets_response import GetDocumentsByFacetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentsByFacetsResponse from a JSON string
get_documents_by_facets_response_instance = GetDocumentsByFacetsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentsByFacetsResponse.to_json())

# convert the object into a dict
get_documents_by_facets_response_dict = get_documents_by_facets_response_instance.to_dict()
# create an instance of GetDocumentsByFacetsResponse from a dict
get_documents_by_facets_response_from_dict = GetDocumentsByFacetsResponse.from_dict(get_documents_by_facets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


