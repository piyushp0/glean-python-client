# DeleteQueryHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | **List[str]** | Queries to delete. | [optional] 

## Example

```python
from openapi_client.models.delete_query_history_request import DeleteQueryHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteQueryHistoryRequest from a JSON string
delete_query_history_request_instance = DeleteQueryHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteQueryHistoryRequest.to_json())

# convert the object into a dict
delete_query_history_request_dict = delete_query_history_request_instance.to_dict()
# create an instance of DeleteQueryHistoryRequest from a dict
delete_query_history_request_from_dict = DeleteQueryHistoryRequest.from_dict(delete_query_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


