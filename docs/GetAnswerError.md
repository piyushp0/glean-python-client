# GetAnswerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** |  | [optional] 
**answer_author** | [**Person**](Person.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_answer_error import GetAnswerError

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnswerError from a JSON string
get_answer_error_instance = GetAnswerError.from_json(json)
# print the JSON string representation of the object
print(GetAnswerError.to_json())

# convert the object into a dict
get_answer_error_dict = get_answer_error_instance.to_dict()
# create an instance of GetAnswerError from a dict
get_answer_error_from_dict = GetAnswerError.from_dict(get_answer_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


