# DeleteAnswerBoardsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The IDs of the Answer Boards to delete. | 

## Example

```python
from openapi_client.models.delete_answer_boards_request import DeleteAnswerBoardsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnswerBoardsRequest from a JSON string
delete_answer_boards_request_instance = DeleteAnswerBoardsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteAnswerBoardsRequest.to_json())

# convert the object into a dict
delete_answer_boards_request_dict = delete_answer_boards_request_instance.to_dict()
# create an instance of DeleteAnswerBoardsRequest from a dict
delete_answer_boards_request_from_dict = DeleteAnswerBoardsRequest.from_dict(delete_answer_boards_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


