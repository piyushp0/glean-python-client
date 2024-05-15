# ChatMessage

A message that is rendered as one coherent unit with one given sender.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_config** | [**AgentConfig**](AgentConfig.md) |  | [optional] 
**author** | **str** |  | [optional] [default to 'USER']
**citations** | [**List[ChatMessageCitation]**](ChatMessageCitation.md) | A list of Citations used to generate the message. | [optional] 
**fragments** | [**List[ChatMessageFragment]**](ChatMessageFragment.md) | A list of chat results. | [optional] 
**metadata** | **str** | Metadata associated with the message (not displayed to the user but stored in the app). | [optional] 
**ts** | **str** | Timestamp of the message. | [optional] 
**message_id** | **str** | Unique ID of the message. | [optional] 
**message_tracking_token** | **str** | Opaque tracking token generated server-side. | [optional] 
**message_type** | **str** | Used to determine the type of UI treatment to apply to this message. UPDATE - intermediate state message for progress updates before content responses. CONTENT - contains content relevant to the user query. CONTEXT - contains additional context relevant to the user query. DEBUG - contains debug information of ChatBot behavior. ERROR - an error happened on server side. | [optional] 
**has_more_fragments** | **bool** | Signals there are more fragments incoming. | [optional] 

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


