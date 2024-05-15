# GetChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_result** | [**ChatResult**](ChatResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_chat_response import GetChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatResponse from a JSON string
get_chat_response_instance = GetChatResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatResponse.to_json())

# convert the object into a dict
get_chat_response_dict = get_chat_response_instance.to_dict()
# create an instance of GetChatResponse from a dict
get_chat_response_from_dict = GetChatResponse.from_dict(get_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


