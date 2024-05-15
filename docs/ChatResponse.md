# ChatResponse

A single response from the /chat backend.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[ChatMessage]**](ChatMessage.md) |  | [optional] 
**chat_id** | **str** | The id of the associated Chat the messages belong to, if one exists. | [optional] 
**follow_up_prompts** | **List[str]** | Follow-up prompts for the user to potentially use | [optional] 
**agent_config** | [**AgentConfig**](AgentConfig.md) |  | [optional] 
**backend_time_millis** | **int** | Time in milliseconds the backend took to respond to the request. | [optional] 
**chat_session_tracking_token** | **str** | A token that is used to track the session. | [optional] 

## Example

```python
from openapi_client.models.chat_response import ChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatResponse from a JSON string
chat_response_instance = ChatResponse.from_json(json)
# print the JSON string representation of the object
print(ChatResponse.to_json())

# convert the object into a dict
chat_response_dict = chat_response_instance.to_dict()
# create an instance of ChatResponse from a dict
chat_response_from_dict = ChatResponse.from_dict(chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


