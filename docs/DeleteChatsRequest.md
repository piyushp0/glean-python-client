# DeleteChatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | A non-empty list of ids of the Chats to be deleted. | 

## Example

```python
from openapi_client.models.delete_chats_request import DeleteChatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatsRequest from a JSON string
delete_chats_request_instance = DeleteChatsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteChatsRequest.to_json())

# convert the object into a dict
delete_chats_request_dict = delete_chats_request_instance.to_dict()
# create an instance of DeleteChatsRequest from a dict
delete_chats_request_from_dict = DeleteChatsRequest.from_dict(delete_chats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


