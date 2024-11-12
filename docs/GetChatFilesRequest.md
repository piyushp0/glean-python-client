# GetChatFilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[str]** | IDs of files to fetch. | 

## Example

```python
from openapi_client.models.get_chat_files_request import GetChatFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatFilesRequest from a JSON string
get_chat_files_request_instance = GetChatFilesRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatFilesRequest.to_json())

# convert the object into a dict
get_chat_files_request_dict = get_chat_files_request_instance.to_dict()
# create an instance of GetChatFilesRequest from a dict
get_chat_files_request_from_dict = GetChatFilesRequest.from_dict(get_chat_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


