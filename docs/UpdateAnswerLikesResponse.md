# UpdateAnswerLikesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**likes** | [**AnswerLikes**](AnswerLikes.md) |  | 

## Example

```python
from openapi_client.models.update_answer_likes_response import UpdateAnswerLikesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnswerLikesResponse from a JSON string
update_answer_likes_response_instance = UpdateAnswerLikesResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAnswerLikesResponse.to_json())

# convert the object into a dict
update_answer_likes_response_dict = update_answer_likes_response_instance.to_dict()
# create an instance of UpdateAnswerLikesResponse from a dict
update_answer_likes_response_from_dict = UpdateAnswerLikesResponse.from_dict(update_answer_likes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


