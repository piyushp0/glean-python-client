# UpdateAnswerLikesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_id** | **int** | The opaque id of the answer to like. | 
**answer_doc_id** | **str** | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID is unavailable. If both are available, using the Answer ID is preferred. | [optional] 
**action** | **str** |  | 

## Example

```python
from openapi_client.models.update_answer_likes_request import UpdateAnswerLikesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnswerLikesRequest from a JSON string
update_answer_likes_request_instance = UpdateAnswerLikesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAnswerLikesRequest.to_json())

# convert the object into a dict
update_answer_likes_request_dict = update_answer_likes_request_instance.to_dict()
# create an instance of UpdateAnswerLikesRequest from a dict
update_answer_likes_request_from_dict = UpdateAnswerLikesRequest.from_dict(update_answer_likes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


