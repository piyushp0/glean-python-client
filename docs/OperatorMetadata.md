# OperatorMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_custom** | **bool** | Whether this operator is supported by default or something that was created within a workplace app (e.g. custom jira field). | [optional] 
**operator_type** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 
**scopes** | [**List[OperatorScope]**](OperatorScope.md) |  | [optional] 
**value** | **str** | Raw/canonical value of the operator. Only applies when result is an operator value. | [optional] 
**display_value** | **str** | Human readable value of the operator that can be shown to the user. Only applies when result is an operator value. | [optional] 

## Example

```python
from openapi_client.models.operator_metadata import OperatorMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorMetadata from a JSON string
operator_metadata_instance = OperatorMetadata.from_json(json)
# print the JSON string representation of the object
print(OperatorMetadata.to_json())

# convert the object into a dict
operator_metadata_dict = operator_metadata_instance.to_dict()
# create an instance of OperatorMetadata from a dict
operator_metadata_from_dict = OperatorMetadata.from_dict(operator_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


