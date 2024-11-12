# ListAnswerBoardsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**with_audience** | **bool** | Whether to include the audience filters with the listed Answer Boards. | [optional] 
**with_roles** | **bool** | Whether to include the editor roles with the listed Answer Boards. | [optional] 

## Example

```python
from openapi_client.models.list_answer_boards_request import ListAnswerBoardsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnswerBoardsRequest from a JSON string
list_answer_boards_request_instance = ListAnswerBoardsRequest.from_json(json)
# print the JSON string representation of the object
print(ListAnswerBoardsRequest.to_json())

# convert the object into a dict
list_answer_boards_request_dict = list_answer_boards_request_instance.to_dict()
# create an instance of ListAnswerBoardsRequest from a dict
list_answer_boards_request_from_dict = ListAnswerBoardsRequest.from_dict(list_answer_boards_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


