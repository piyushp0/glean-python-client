# ChatMessageCitation

Information about the source for a ChatMessage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_token** | **str** | An opaque token that represents this particular result in this particular ChatMessage. To be used for /feedback reporting. | [optional] 
**source_document** | [**Document**](Document.md) |  | [optional] 
**source_person** | [**Person**](Person.md) |  | [optional] 
**reference_ranges** | [**List[ReferenceRange]**](ReferenceRange.md) | Each reference range and its corresponding snippets | [optional] 

## Example

```python
from openapi_client.models.chat_message_citation import ChatMessageCitation

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageCitation from a JSON string
chat_message_citation_instance = ChatMessageCitation.from_json(json)
# print the JSON string representation of the object
print(ChatMessageCitation.to_json())

# convert the object into a dict
chat_message_citation_dict = chat_message_citation_instance.to_dict()
# create an instance of ChatMessageCitation from a dict
chat_message_citation_from_dict = ChatMessageCitation.from_dict(chat_message_citation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


