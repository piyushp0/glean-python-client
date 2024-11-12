# GetChatApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Chat application to be retrieved. | 

## Example

```python
from openapi_client.models.get_chat_application_request import GetChatApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatApplicationRequest from a JSON string
get_chat_application_request_instance = GetChatApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatApplicationRequest.to_json())

# convert the object into a dict
get_chat_application_request_dict = get_chat_application_request_instance.to_dict()
# create an instance of GetChatApplicationRequest from a dict
get_chat_application_request_from_dict = GetChatApplicationRequest.from_dict(get_chat_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


