# AnswerMutableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | [optional] 
**question_variations** | **List[str]** | Additional ways of phrasing this question. | [optional] 
**body_text** | **str** | The plain text answer to the question. | [optional] 
**board_id** | **int** | The parent board ID of this Answer, or 0 if it&#39;s a floating Answer. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see the answer. Values are taken from the corresponding filters in people search. | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles for the answer added by the owner. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles for the answer removed by the owner. | [optional] 
**roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of roles for this answer explicitly granted by an owner, editor, or admin. | [optional] 
**source_document_spec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**source_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.answer_mutable_properties import AnswerMutableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerMutableProperties from a JSON string
answer_mutable_properties_instance = AnswerMutableProperties.from_json(json)
# print the JSON string representation of the object
print(AnswerMutableProperties.to_json())

# convert the object into a dict
answer_mutable_properties_dict = answer_mutable_properties_instance.to_dict()
# create an instance of AnswerMutableProperties from a dict
answer_mutable_properties_from_dict = AnswerMutableProperties.from_dict(answer_mutable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


