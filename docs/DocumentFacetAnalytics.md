# DocumentFacetAnalytics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facet** | [**FacetFilter**](FacetFilter.md) |  | [optional] 
**analytics** | [**DocumentAnalytics**](DocumentAnalytics.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_facet_analytics import DocumentFacetAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFacetAnalytics from a JSON string
document_facet_analytics_instance = DocumentFacetAnalytics.from_json(json)
# print the JSON string representation of the object
print(DocumentFacetAnalytics.to_json())

# convert the object into a dict
document_facet_analytics_dict = document_facet_analytics_instance.to_dict()
# create an instance of DocumentFacetAnalytics from a dict
document_facet_analytics_from_dict = DocumentFacetAnalytics.from_dict(document_facet_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


