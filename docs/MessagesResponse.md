# MessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Whether there are more results for client to continue requesting. | 
**search_response** | [**SearchResponse**](SearchResponse.md) |  | [optional] 
**root_message** | [**SearchResult**](SearchResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.messages_response import MessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesResponse from a JSON string
messages_response_instance = MessagesResponse.from_json(json)
# print the JSON string representation of the object
print(MessagesResponse.to_json())

# convert the object into a dict
messages_response_dict = messages_response_instance.to_dict()
# create an instance of MessagesResponse from a dict
messages_response_from_dict = MessagesResponse.from_dict(messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


