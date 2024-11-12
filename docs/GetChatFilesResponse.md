# GetChatFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**Dict[str, ChatFile]**](ChatFile.md) | A map of file IDs to ChatFile structs. | [optional] 

## Example

```python
from openapi_client.models.get_chat_files_response import GetChatFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatFilesResponse from a JSON string
get_chat_files_response_instance = GetChatFilesResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatFilesResponse.to_json())

# convert the object into a dict
get_chat_files_response_dict = get_chat_files_response_instance.to_dict()
# create an instance of GetChatFilesResponse from a dict
get_chat_files_response_from_dict = GetChatFilesResponse.from_dict(get_chat_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


