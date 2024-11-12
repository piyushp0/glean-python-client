# DocumentAnalytics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_spec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**visitor_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**clicker_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**user_impression_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**visit_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**facet_analytics** | [**List[DocumentFacetAnalytics]**](DocumentFacetAnalytics.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_analytics import DocumentAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAnalytics from a JSON string
document_analytics_instance = DocumentAnalytics.from_json(json)
# print the JSON string representation of the object
print(DocumentAnalytics.to_json())

# convert the object into a dict
document_analytics_dict = document_analytics_instance.to_dict()
# create an instance of DocumentAnalytics from a dict
document_analytics_from_dict = DocumentAnalytics.from_dict(document_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


