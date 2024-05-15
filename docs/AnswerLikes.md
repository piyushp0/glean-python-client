# AnswerLikes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**liked_by** | [**List[AnswerLike]**](AnswerLike.md) |  | 
**liked_by_user** | **bool** | Whether the user in context liked the answer. | 
**num_likes** | **int** | The total number of likes for the answer. | 

## Example

```python
from openapi_client.models.answer_likes import AnswerLikes

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerLikes from a JSON string
answer_likes_instance = AnswerLikes.from_json(json)
# print the JSON string representation of the object
print(AnswerLikes.to_json())

# convert the object into a dict
answer_likes_dict = answer_likes_instance.to_dict()
# create an instance of AnswerLikes from a dict
answer_likes_from_dict = AnswerLikes.from_dict(answer_likes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


