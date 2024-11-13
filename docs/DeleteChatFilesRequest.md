# DeleteChatFilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[str]** | IDs of files to delete. | 

## Example

```python
from openapi_client.models.delete_chat_files_request import DeleteChatFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatFilesRequest from a JSON string
delete_chat_files_request_instance = DeleteChatFilesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteChatFilesRequest.to_json())

# convert the object into a dict
delete_chat_files_request_dict = delete_chat_files_request_instance.to_dict()
# create an instance of DeleteChatFilesRequest from a dict
delete_chat_files_request_from_dict = DeleteChatFilesRequest.from_dict(delete_chat_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


