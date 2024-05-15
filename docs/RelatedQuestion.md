# RelatedQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | The text of the related question | [optional] 
**answer** | **str** | The answer for the related question | [optional] 
**ranges** | [**List[TextRange]**](TextRange.md) | Subsections of the answer string to which some special formatting should be applied (eg. bold) | [optional] 

## Example

```python
from openapi_client.models.related_question import RelatedQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedQuestion from a JSON string
related_question_instance = RelatedQuestion.from_json(json)
# print the JSON string representation of the object
print(RelatedQuestion.to_json())

# convert the object into a dict
related_question_dict = related_question_instance.to_dict()
# create an instance of RelatedQuestion from a dict
related_question_from_dict = RelatedQuestion.from_dict(related_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


