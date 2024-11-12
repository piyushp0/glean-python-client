# CreateAnswerBoardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_result** | [**AnswerBoardResult**](AnswerBoardResult.md) |  | [optional] 
**error** | [**AnswerBoardError**](AnswerBoardError.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_answer_board_response import CreateAnswerBoardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnswerBoardResponse from a JSON string
create_answer_board_response_instance = CreateAnswerBoardResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAnswerBoardResponse.to_json())

# convert the object into a dict
create_answer_board_response_dict = create_answer_board_response_instance.to_dict()
# create an instance of CreateAnswerBoardResponse from a dict
create_answer_board_response_from_dict = CreateAnswerBoardResponse.from_dict(create_answer_board_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


