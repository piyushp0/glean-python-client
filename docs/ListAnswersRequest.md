# ListAnswersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_id** | **int** | The Answer Board Id to list answers on. | [optional] 

## Example

```python
from openapi_client.models.list_answers_request import ListAnswersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnswersRequest from a JSON string
list_answers_request_instance = ListAnswersRequest.from_json(json)
# print the JSON string representation of the object
print(ListAnswersRequest.to_json())

# convert the object into a dict
list_answers_request_dict = list_answers_request_instance.to_dict()
# create an instance of ListAnswersRequest from a dict
list_answers_request_from_dict = ListAnswersRequest.from_dict(list_answers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


