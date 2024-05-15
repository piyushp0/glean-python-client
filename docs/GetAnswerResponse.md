# GetAnswerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_result** | [**AnswerResult**](AnswerResult.md) |  | [optional] 
**error** | [**GetAnswerError**](GetAnswerError.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_answer_response import GetAnswerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnswerResponse from a JSON string
get_answer_response_instance = GetAnswerResponse.from_json(json)
# print the JSON string representation of the object
print(GetAnswerResponse.to_json())

# convert the object into a dict
get_answer_response_dict = get_answer_response_instance.to_dict()
# create an instance of GetAnswerResponse from a dict
get_answer_response_from_dict = GetAnswerResponse.from_dict(get_answer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


