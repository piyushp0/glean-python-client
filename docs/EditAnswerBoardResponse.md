# EditAnswerBoardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_result** | [**AnswerBoardResult**](AnswerBoardResult.md) |  | [optional] 
**error** | [**AnswerBoardError**](AnswerBoardError.md) |  | [optional] 

## Example

```python
from openapi_client.models.edit_answer_board_response import EditAnswerBoardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditAnswerBoardResponse from a JSON string
edit_answer_board_response_instance = EditAnswerBoardResponse.from_json(json)
# print the JSON string representation of the object
print(EditAnswerBoardResponse.to_json())

# convert the object into a dict
edit_answer_board_response_dict = edit_answer_board_response_instance.to_dict()
# create an instance of EditAnswerBoardResponse from a dict
edit_answer_board_response_from_dict = EditAnswerBoardResponse.from_dict(edit_answer_board_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


