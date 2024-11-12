# GetDocumentAnalyticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_specs** | [**List[DocumentSpec]**](DocumentSpec.md) | The specification for the documents for which analytics will be retrieved. | 
**day_range** | [**Period**](Period.md) |  | 
**with_clicker_counts** | **bool** | Whether response should include click information or not. Default is to not include click information. | [optional] 
**with_impression_counts** | **bool** | Whether response should include impression information or not. Default is to not include impression information. | [optional] 
**with_facet_aggregations** | **bool** | Whether the results will include aggregate counts/info for facets like location, department, etc. | [optional] 
**with_visit_counts** | **bool** | Whether response should include visit counts or not. Default is to return only visitor counts. | [optional] 

## Example

```python
from openapi_client.models.get_document_analytics_request import GetDocumentAnalyticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentAnalyticsRequest from a JSON string
get_document_analytics_request_instance = GetDocumentAnalyticsRequest.from_json(json)
# print the JSON string representation of the object
print(GetDocumentAnalyticsRequest.to_json())

# convert the object into a dict
get_document_analytics_request_dict = get_document_analytics_request_instance.to_dict()
# create an instance of GetDocumentAnalyticsRequest from a dict
get_document_analytics_request_from_dict = GetDocumentAnalyticsRequest.from_dict(get_document_analytics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


