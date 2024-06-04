# Chat

A historical representation of a series of chat messages a user had with Glean Assistant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[ChatMessage]**](ChatMessage.md) | The chat messages within a Chat. | [optional] 
**id** | **str** | The opaque id of the Chat. | [optional] 
**create_time** | **int** | Server Unix timestamp of the creation time (in seconds since epoch UTC). | [optional] 
**created_by** | [**Person**](Person.md) |  | [optional] 
**update_time** | **int** | Server Unix timestamp of the update time (in seconds since epoch UTC). | [optional] 
**name** | **str** | The name of the Chat. | [optional] 
**application_id** | **str** | The ID of the AI App that this Chat is associated to. | [optional] 

## Example

```python
from openapi_client.models.chat import Chat

# TODO update the JSON string below
json = "{}"
# create an instance of Chat from a JSON string
chat_instance = Chat.from_json(json)
# print the JSON string representation of the object
print(Chat.to_json())

# convert the object into a dict
chat_dict = chat_instance.to_dict()
# create an instance of Chat from a dict
chat_from_dict = Chat.from_dict(chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


