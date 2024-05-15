# DocumentSpecOneOf2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ugc_type** | **str** | The type of the user generated content (UGC datasource). | [optional] 
**content_id** | **int** | The id for user generated content. | [optional] 
**doc_type** | **str** | The specific type of the user generated content type. | [optional] 

## Example

```python
from openapi_client.models.document_spec_one_of2 import DocumentSpecOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSpecOneOf2 from a JSON string
document_spec_one_of2_instance = DocumentSpecOneOf2.from_json(json)
# print the JSON string representation of the object
print(DocumentSpecOneOf2.to_json())

# convert the object into a dict
document_spec_one_of2_dict = document_spec_one_of2_instance.to_dict()
# create an instance of DocumentSpecOneOf2 from a dict
document_spec_one_of2_from_dict = DocumentSpecOneOf2.from_dict(document_spec_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


