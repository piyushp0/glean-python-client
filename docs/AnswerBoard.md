# AnswerBoard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of the Collection. | 
**description** | **str** | A brief summary of the Collection&#39;s contents. | 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of added user roles for the Collection. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of removed user roles for the Collection. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. | [optional] 
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**id** | **int** | The unique ID of the Answer Board. | 
**create_time** | **datetime** |  | [optional] 
**update_time** | **datetime** |  | [optional] 
**creator** | [**Person**](Person.md) |  | [optional] 
**updated_by** | [**Person**](Person.md) |  | [optional] 
**item_count** | **int** | The number of items currently in the Answer Board. Separated from the actual items so we can grab the count without items. | [optional] 
**roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles for the Answer Board. | [optional] 

## Example

```python
from openapi_client.models.answer_board import AnswerBoard

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerBoard from a JSON string
answer_board_instance = AnswerBoard.from_json(json)
# print the JSON string representation of the object
print(AnswerBoard.to_json())

# convert the object into a dict
answer_board_dict = answer_board_instance.to_dict()
# create an instance of AnswerBoard from a dict
answer_board_from_dict = AnswerBoard.from_dict(answer_board_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


