# GetAnswerBoardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_result** | [**AnswerBoardResult**](AnswerBoardResult.md) |  | [optional] 
**error** | [**AnswerBoardError**](AnswerBoardError.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_answer_board_response import GetAnswerBoardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnswerBoardResponse from a JSON string
get_answer_board_response_instance = GetAnswerBoardResponse.from_json(json)
# print the JSON string representation of the object
print(GetAnswerBoardResponse.to_json())

# convert the object into a dict
get_answer_board_response_dict = get_answer_board_response_instance.to_dict()
# create an instance of GetAnswerBoardResponse from a dict
get_answer_board_response_from_dict = GetAnswerBoardResponse.from_dict(get_answer_board_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


