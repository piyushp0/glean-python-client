# DocumentContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_text_list** | **List[str]** | The plaintext content of the document. | [optional] 

## Example

```python
from openapi_client.models.document_content import DocumentContent

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentContent from a JSON string
document_content_instance = DocumentContent.from_json(json)
# print the JSON string representation of the object
print(DocumentContent.to_json())

# convert the object into a dict
document_content_dict = document_content_instance.to_dict()
# create an instance of DocumentContent from a dict
document_content_from_dict = DocumentContent.from_dict(document_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


