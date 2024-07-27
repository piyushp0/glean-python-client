# ChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save_chat** | **bool** | Save the current interaction as a Chat for the user to access later. | [optional] 
**chat_id** | **str** | The id of the Chat that this message should be added to. An empty id signifies creating a new Chat if saveChat is true. | [optional] 
**messages** | [**List[ChatMessage]**](ChatMessage.md) | A list of chat messages, from most recent to least recent. It can be assumed that the first chat message in the list is the user&#39;s most recent query. | 
**agent_config** | [**AgentConfig**](AgentConfig.md) |  | [optional] 
**inclusions** | [**ChatRestrictionFilters**](ChatRestrictionFilters.md) |  | [optional] 
**exclusions** | [**ChatRestrictionFilters**](ChatRestrictionFilters.md) |  | [optional] 
**timeout_millis** | **int** | Timeout in milliseconds for the request. A &#x60;408&#x60; error will be returned if handling the request takes longer. | [optional] 
**application_id** | **str** | The ID of the application this request originates from, used to determine the configuration of underlying chat processes. This should correspond to the ID set during admin setup. If not specified, the default chat experience will be used. | [optional] 
**stream** | **bool** | Whether to stream responses as they become available. If false, the entire response will be returned at once. Note if true and the model being used does not support streaming, the model&#39;s response will not be streamed but other messages from the endpoint still will. | [optional] 

## Example

```python
from openapi_client.models.chat_request import ChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatRequest from a JSON string
chat_request_instance = ChatRequest.from_json(json)
# print the JSON string representation of the object
print(ChatRequest.to_json())

# convert the object into a dict
chat_request_dict = chat_request_instance.to_dict()
# create an instance of ChatRequest from a dict
chat_request_from_dict = ChatRequest.from_dict(chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


