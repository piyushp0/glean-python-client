# GetAnswerBoardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the Answer Board to be retrieved. | 

## Example

```python
from openapi_client.models.get_answer_board_request import GetAnswerBoardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnswerBoardRequest from a JSON string
get_answer_board_request_instance = GetAnswerBoardRequest.from_json(json)
# print the JSON string representation of the object
print(GetAnswerBoardRequest.to_json())

# convert the object into a dict
get_answer_board_request_dict = get_answer_board_request_instance.to_dict()
# create an instance of GetAnswerBoardRequest from a dict
get_answer_board_request_from_dict = GetAnswerBoardRequest.from_dict(get_answer_board_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


