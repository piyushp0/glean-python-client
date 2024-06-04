# ChatFileMetadata

Metadata of a file uploaded by a user for Chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ChatFileStatus**](ChatFileStatus.md) |  | [optional] 
**upload_time** | **int** | Upload time, in epoch seconds. | [optional] 
**processed_size** | **int** | Size of the processed file in bytes. | [optional] 
**failure_reason** | [**ChatFileFailureReason**](ChatFileFailureReason.md) |  | [optional] 

## Example

```python
from openapi_client.models.chat_file_metadata import ChatFileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ChatFileMetadata from a JSON string
chat_file_metadata_instance = ChatFileMetadata.from_json(json)
# print the JSON string representation of the object
print(ChatFileMetadata.to_json())

# convert the object into a dict
chat_file_metadata_dict = chat_file_metadata_instance.to_dict()
# create an instance of ChatFileMetadata from a dict
chat_file_metadata_from_dict = ChatFileMetadata.from_dict(chat_file_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


