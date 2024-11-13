# ChatMessage

A message that is rendered as one coherent unit with one given sender.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_config** | [**AgentConfig**](AgentConfig.md) |  | [optional] 
**author** | **str** |  | [optional] [default to 'USER']
**citations** | [**List[ChatMessageCitation]**](ChatMessageCitation.md) | A list of Citations that were used to generate the response. | [optional] 
**uploaded_file_ids** | **List[str]** | IDs of files uploaded in the message that are referenced to generate the answer. | [optional] 
**fragments** | [**List[ChatMessageFragment]**](ChatMessageFragment.md) | A list of rich data used to represent the response or formulate a request. These are linearly stitched together to support richer data formats beyond simple text. | [optional] 
**ts** | **str** | Response timestamp of the message. | [optional] 
**message_id** | **str** | A unique server-side generated ID used to identify a message, automatically populated for any USER authored messages. | [optional] 
**message_tracking_token** | **str** | Opaque tracking token generated server-side. | [optional] 
**message_type** | **str** | Semantically groups content of a certain type. It can be used for purposes such as differential UI treatment. USER authored messages should be of type CONTENT and do not need &#x60;messageType&#x60; specified. | [optional] [default to 'CONTENT']
**has_more_fragments** | **bool** | Signals there are additional response fragments incoming. | [optional] 

## Example

```python
from openapi_client.models.chat_message import ChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessage from a JSON string
chat_message_instance = ChatMessage.from_json(json)
# print the JSON string representation of the object
print(ChatMessage.to_json())

# convert the object into a dict
chat_message_dict = chat_message_instance.to_dict()
# create an instance of ChatMessage from a dict
chat_message_from_dict = ChatMessage.from_dict(chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


