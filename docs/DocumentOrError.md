# DocumentOrError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Glean Document ID. | [optional] 
**datasource** | **str** | The app or other repository type from which the document was extracted | [optional] 
**connector_type** | [**ConnectorType**](ConnectorType.md) |  | [optional] 
**doc_type** | **str** | The datasource-specific type of the document (e.g. for Jira issues, this is the issue type such as Bug or Feature Request). | [optional] 
**content** | [**DocumentContent**](DocumentContent.md) |  | [optional] 
**container_document** | [**Document**](Document.md) |  | [optional] 
**parent_document** | [**Document**](Document.md) |  | [optional] 
**title** | **str** | The title of the document. | [optional] 
**url** | **str** | A permalink for the document. | [optional] 
**metadata** | [**DocumentMetadata**](DocumentMetadata.md) |  | [optional] 
**sections** | [**List[DocumentSection]**](DocumentSection.md) | A list of content sub-sections in the document, e.g. text blocks with different headings in a Drive doc or Confluence page. | [optional] 
**error** | **str** | The text for error, reason. | [optional] 

## Example

```python
from openapi_client.models.document_or_error import DocumentOrError

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentOrError from a JSON string
document_or_error_instance = DocumentOrError.from_json(json)
# print the JSON string representation of the object
print(DocumentOrError.to_json())

# convert the object into a dict
document_or_error_dict = document_or_error_instance.to_dict()
# create an instance of DocumentOrError from a dict
document_or_error_from_dict = DocumentOrError.from_dict(document_or_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


