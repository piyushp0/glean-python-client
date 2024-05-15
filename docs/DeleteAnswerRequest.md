# DeleteAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque ID of the Answer. | 
**doc_id** | **str** | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn&#39;t available. If both are available, using the Answer ID is preferred. | [optional] 

## Example

```python
from openapi_client.models.delete_answer_request import DeleteAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnswerRequest from a JSON string
delete_answer_request_instance = DeleteAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteAnswerRequest.to_json())

# convert the object into a dict
delete_answer_request_dict = delete_answer_request_instance.to_dict()
# create an instance of DeleteAnswerRequest from a dict
delete_answer_request_from_dict = DeleteAnswerRequest.from_dict(delete_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


