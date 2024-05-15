# AnswerBoardResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board** | [**AnswerBoard**](AnswerBoard.md) |  | 
**tracking_token** | **str** | An opaque token that represents this particular Answer Board. To be used for /feedback reporting. | [optional] 

## Example

```python
from openapi_client.models.answer_board_result import AnswerBoardResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerBoardResult from a JSON string
answer_board_result_instance = AnswerBoardResult.from_json(json)
# print the JSON string representation of the object
print(AnswerBoardResult.to_json())

# convert the object into a dict
answer_board_result_dict = answer_board_result_instance.to_dict()
# create an instance of AnswerBoardResult from a dict
answer_board_result_from_dict = AnswerBoardResult.from_dict(answer_board_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


