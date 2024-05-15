# GetDocumentAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DocumentAnalytics]**](DocumentAnalytics.md) | Analytics for requested documents. There will be one-to-one mapping for documents included in the request. | [optional] 

## Example

```python
from openapi_client.models.get_document_analytics_response import GetDocumentAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentAnalyticsResponse from a JSON string
get_document_analytics_response_instance = GetDocumentAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentAnalyticsResponse.to_json())

# convert the object into a dict
get_document_analytics_response_dict = get_document_analytics_response_instance.to_dict()
# create an instance of GetDocumentAnalyticsResponse from a dict
get_document_analytics_response_from_dict = GetDocumentAnalyticsResponse.from_dict(get_document_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


