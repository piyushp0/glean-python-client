# ChatMetadataResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**ChatMetadata**](ChatMetadata.md) |  | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular Chat. To be used for &#x60;/feedback&#x60; reporting. | [optional] 

## Example

```python
from openapi_client.models.chat_metadata_result import ChatMetadataResult

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMetadataResult from a JSON string
chat_metadata_result_instance = ChatMetadataResult.from_json(json)
# print the JSON string representation of the object
print(ChatMetadataResult.to_json())

# convert the object into a dict
chat_metadata_result_dict = chat_metadata_result_instance.to_dict()
# create an instance of ChatMetadataResult from a dict
chat_metadata_result_from_dict = ChatMetadataResult.from_dict(chat_metadata_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


