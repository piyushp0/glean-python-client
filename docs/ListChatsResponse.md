# ListChatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_results** | [**List[ChatMetadataResult]**](ChatMetadataResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_chats_response import ListChatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListChatsResponse from a JSON string
list_chats_response_instance = ListChatsResponse.from_json(json)
# print the JSON string representation of the object
print(ListChatsResponse.to_json())

# convert the object into a dict
list_chats_response_dict = list_chats_response_instance.to_dict()
# create an instance of ListChatsResponse from a dict
list_chats_response_from_dict = ListChatsResponse.from_dict(list_chats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


