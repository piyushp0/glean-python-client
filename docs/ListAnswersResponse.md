# ListAnswersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_results** | [**List[AnswerResult]**](AnswerResult.md) | List of answers with tracking tokens. | 

## Example

```python
from openapi_client.models.list_answers_response import ListAnswersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnswersResponse from a JSON string
list_answers_response_instance = ListAnswersResponse.from_json(json)
# print the JSON string representation of the object
print(ListAnswersResponse.to_json())

# convert the object into a dict
list_answers_response_dict = list_answers_response_instance.to_dict()
# create an instance of ListAnswersResponse from a dict
list_answers_response_from_dict = ListAnswersResponse.from_dict(list_answers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


