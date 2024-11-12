# GetDocumentsByFacetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasources_filter** | **List[str]** | Filter results to one or more datasources (e.g. gmail, slack). All results are returned if missing. | [optional] 
**filter_sets** | [**List[FacetFilterSet]**](FacetFilterSet.md) | A list of facet filter sets that will be OR&#39;ed together. An AND is assumed between different filters in each set. | 
**cursor** | **str** | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start. | [optional] 

## Example

```python
from openapi_client.models.get_documents_by_facets_request import GetDocumentsByFacetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentsByFacetsRequest from a JSON string
get_documents_by_facets_request_instance = GetDocumentsByFacetsRequest.from_json(json)
# print the JSON string representation of the object
print(GetDocumentsByFacetsRequest.to_json())

# convert the object into a dict
get_documents_by_facets_request_dict = get_documents_by_facets_request_instance.to_dict()
# create an instance of GetDocumentsByFacetsRequest from a dict
get_documents_by_facets_request_from_dict = GetDocumentsByFacetsRequest.from_dict(get_documents_by_facets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


