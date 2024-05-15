# AnswerResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | [**Answer**](Answer.md) |  | 
**tracking_token** | **str** | An opaque token that represents this particular Answer. To be used for &#x60;/feedback&#x60; reporting. | [optional] 

## Example

```python
from openapi_client.models.answer_result import AnswerResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerResult from a JSON string
answer_result_instance = AnswerResult.from_json(json)
# print the JSON string representation of the object
print(AnswerResult.to_json())

# convert the object into a dict
answer_result_dict = answer_result_instance.to_dict()
# create an instance of AnswerResult from a dict
answer_result_from_dict = AnswerResult.from_dict(answer_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


