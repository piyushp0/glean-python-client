# UploadChatFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[ChatFile]**](ChatFile.md) | Files uploaded for chat. | [optional] 

## Example

```python
from openapi_client.models.upload_chat_files_response import UploadChatFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadChatFilesResponse from a JSON string
upload_chat_files_response_instance = UploadChatFilesResponse.from_json(json)
# print the JSON string representation of the object
print(UploadChatFilesResponse.to_json())

# convert the object into a dict
upload_chat_files_response_dict = upload_chat_files_response_instance.to_dict()
# create an instance of UploadChatFilesResponse from a dict
upload_chat_files_response_from_dict = UploadChatFilesResponse.from_dict(upload_chat_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


