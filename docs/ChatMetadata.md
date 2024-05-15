# ChatMetadata

Metadata of a Chat a user had with Glean Assistant. This contains no actual conversational content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The opaque id of the Chat. | [optional] 
**create_time** | **int** | Server Unix timestamp of the creation time (in seconds since epoch UTC). | [optional] 
**created_by** | [**Person**](Person.md) |  | [optional] 
**update_time** | **int** | Server Unix timestamp of the update time (in seconds since epoch UTC). | [optional] 
**name** | **str** | The name of the Chat. | [optional] 

## Example

```python
from openapi_client.models.chat_metadata import ChatMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMetadata from a JSON string
chat_metadata_instance = ChatMetadata.from_json(json)
# print the JSON string representation of the object
print(ChatMetadata.to_json())

# convert the object into a dict
chat_metadata_dict = chat_metadata_instance.to_dict()
# create an instance of ChatMetadata from a dict
chat_metadata_from_dict = ChatMetadata.from_dict(chat_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


