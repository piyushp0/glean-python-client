# RelatedDocuments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** | How this document relates to the including entity. | [optional] 
**associated_entity_id** | **str** | Which entity in the response that this entity relates to. Relevant when there are multiple entities associated with the response (such as merged customers) | [optional] 
**query_suggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**documents** | [**List[Document]**](Document.md) | A truncated list of documents with this relation. TO BE DEPRECATED. | [optional] 
**results** | [**List[SearchResult]**](SearchResult.md) | A truncated list of documents associated with this relation. To be used in favor of &#x60;documents&#x60; because it contains a trackingToken. | [optional] 

## Example

```python
from openapi_client.models.related_documents import RelatedDocuments

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedDocuments from a JSON string
related_documents_instance = RelatedDocuments.from_json(json)
# print the JSON string representation of the object
print(RelatedDocuments.to_json())

# convert the object into a dict
related_documents_dict = related_documents_instance.to_dict()
# create an instance of RelatedDocuments from a dict
related_documents_from_dict = RelatedDocuments.from_dict(related_documents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


