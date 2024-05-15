# ChatResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular Chat. To be used for &#x60;/feedback&#x60; reporting. | [optional] 

## Example

```python
from openapi_client.models.chat_result import ChatResult

# TODO update the JSON string below
json = "{}"
# create an instance of ChatResult from a JSON string
chat_result_instance = ChatResult.from_json(json)
# print the JSON string representation of the object
print(ChatResult.to_json())

# convert the object into a dict
chat_result_dict = chat_result_instance.to_dict()
# create an instance of ChatResult from a dict
chat_result_from_dict = ChatResult.from_dict(chat_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


