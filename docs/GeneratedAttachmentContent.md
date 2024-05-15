# GeneratedAttachmentContent

Content that has been generated or extrapolated from the documents present in the document field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_header** | **str** | The header describing the generated content. | [optional] 
**text** | **str** | The content that has been generated. | [optional] 

## Example

```python
from openapi_client.models.generated_attachment_content import GeneratedAttachmentContent

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedAttachmentContent from a JSON string
generated_attachment_content_instance = GeneratedAttachmentContent.from_json(json)
# print the JSON string representation of the object
print(GeneratedAttachmentContent.to_json())

# convert the object into a dict
generated_attachment_content_dict = generated_attachment_content_instance.to_dict()
# create an instance of GeneratedAttachmentContent from a dict
generated_attachment_content_from_dict = GeneratedAttachmentContent.from_dict(generated_attachment_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


