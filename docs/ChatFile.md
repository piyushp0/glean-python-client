# ChatFile

Structure for file uploaded by a user for Chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the file. | [optional] 
**url** | **str** | Url of the file. | [optional] 
**name** | **str** | Name of the uploaded file. | [optional] 
**metadata** | [**ChatFileMetadata**](ChatFileMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.chat_file import ChatFile

# TODO update the JSON string below
json = "{}"
# create an instance of ChatFile from a JSON string
chat_file_instance = ChatFile.from_json(json)
# print the JSON string representation of the object
print(ChatFile.to_json())

# convert the object into a dict
chat_file_dict = chat_file_instance.to_dict()
# create an instance of ChatFile from a dict
chat_file_from_dict = ChatFile.from_dict(chat_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


