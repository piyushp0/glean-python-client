# GeneratedAttachment

These are attachments that aren't natively present on the event, and have been smartly suggested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_name** | [**EventStrategyName**](EventStrategyName.md) |  | [optional] 
**documents** | [**List[Document]**](Document.md) |  | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**external_links** | [**List[StructuredLink]**](StructuredLink.md) | A list of links to external sources outside of Glean. | [optional] 
**content** | [**List[GeneratedAttachmentContent]**](GeneratedAttachmentContent.md) |  | [optional] 

## Example

```python
from openapi_client.models.generated_attachment import GeneratedAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedAttachment from a JSON string
generated_attachment_instance = GeneratedAttachment.from_json(json)
# print the JSON string representation of the object
print(GeneratedAttachment.to_json())

# convert the object into a dict
generated_attachment_dict = generated_attachment_instance.to_dict()
# create an instance of GeneratedAttachment from a dict
generated_attachment_from_dict = GeneratedAttachment.from_dict(generated_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


