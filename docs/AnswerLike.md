# AnswerLike


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**Person**](Person.md) |  | [optional] 
**create_time** | **datetime** | The time the user liked the answer in ISO format (ISO 8601). | [optional] 

## Example

```python
from openapi_client.models.answer_like import AnswerLike

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerLike from a JSON string
answer_like_instance = AnswerLike.from_json(json)
# print the JSON string representation of the object
print(AnswerLike.to_json())

# convert the object into a dict
answer_like_dict = answer_like_instance.to_dict()
# create an instance of AnswerLike from a dict
answer_like_from_dict = AnswerLike.from_dict(answer_like_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


