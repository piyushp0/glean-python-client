# CreateAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AnswerCreationData**](AnswerCreationData.md) |  | 

## Example

```python
from openapi_client.models.create_answer_request import CreateAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnswerRequest from a JSON string
create_answer_request_instance = CreateAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAnswerRequest.to_json())

# convert the object into a dict
create_answer_request_dict = create_answer_request_instance.to_dict()
# create an instance of CreateAnswerRequest from a dict
create_answer_request_from_dict = CreateAnswerRequest.from_dict(create_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


