# DeleteAnswerBoardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AnswerBoardError**](AnswerBoardError.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_answer_boards_response import DeleteAnswerBoardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnswerBoardsResponse from a JSON string
delete_answer_boards_response_instance = DeleteAnswerBoardsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAnswerBoardsResponse.to_json())

# convert the object into a dict
delete_answer_boards_response_dict = delete_answer_boards_response_instance.to_dict()
# create an instance of DeleteAnswerBoardsResponse from a dict
delete_answer_boards_response_from_dict = DeleteAnswerBoardsResponse.from_dict(delete_answer_boards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


