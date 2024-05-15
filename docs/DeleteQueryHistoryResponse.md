# DeleteQueryHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**DeleteQueryHistoryError**](DeleteQueryHistoryError.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_query_history_response import DeleteQueryHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteQueryHistoryResponse from a JSON string
delete_query_history_response_instance = DeleteQueryHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteQueryHistoryResponse.to_json())

# convert the object into a dict
delete_query_history_response_dict = delete_query_history_response_instance.to_dict()
# create an instance of DeleteQueryHistoryResponse from a dict
delete_query_history_response_from_dict = DeleteQueryHistoryResponse.from_dict(delete_query_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


