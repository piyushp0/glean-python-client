# EditAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque ID of the Answer. | 
**doc_id** | **str** | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn&#39;t available. If both are available, using the Answer ID is preferred. | [optional] 
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
**added_collections** | **List[int]** | IDs of Collections to which a document is added. | [optional] 
**removed_collections** | **List[int]** | IDs of Collections from which a document is removed. | [optional] 
**combined_answer_text** | [**StructuredTextMutableProperties**](StructuredTextMutableProperties.md) |  | [optional] 

## Example

```python
from openapi_client.models.edit_answer_request import EditAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditAnswerRequest from a JSON string
edit_answer_request_instance = EditAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(EditAnswerRequest.to_json())

# convert the object into a dict
edit_answer_request_dict = edit_answer_request_instance.to_dict()
# create an instance of EditAnswerRequest from a dict
edit_answer_request_from_dict = EditAnswerRequest.from_dict(edit_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


