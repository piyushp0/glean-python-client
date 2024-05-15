# DocumentSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the document. | [optional] 
**id** | **str** | The ID of the document. | [optional] 
**ugc_type** | **str** | The type of the user generated content (UGC datasource). | [optional] 
**content_id** | **int** | The id for user generated content. | [optional] 
**doc_type** | **str** | The specific type of the user generated content type. | [optional] 

## Example

```python
from openapi_client.models.document_spec import DocumentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSpec from a JSON string
document_spec_instance = DocumentSpec.from_json(json)
# print the JSON string representation of the object
print(DocumentSpec.to_json())

# convert the object into a dict
document_spec_dict = document_spec_instance.to_dict()
# create an instance of DocumentSpec from a dict
document_spec_from_dict = DocumentSpec.from_dict(document_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


