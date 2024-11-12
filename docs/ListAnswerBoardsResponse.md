# ListAnswerBoardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_results** | [**List[AnswerBoardResult]**](AnswerBoardResult.md) | List of all Answer Boards, no Answers are included. | 

## Example

```python
from openapi_client.models.list_answer_boards_response import ListAnswerBoardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnswerBoardsResponse from a JSON string
list_answer_boards_response_instance = ListAnswerBoardsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAnswerBoardsResponse.to_json())

# convert the object into a dict
list_answer_boards_response_dict = list_answer_boards_response_instance.to_dict()
# create an instance of ListAnswerBoardsResponse from a dict
list_answer_boards_response_from_dict = ListAnswerBoardsResponse.from_dict(list_answer_boards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


