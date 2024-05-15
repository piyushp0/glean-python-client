# OperatorScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** |  | [optional] 
**doc_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.operator_scope import OperatorScope

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorScope from a JSON string
operator_scope_instance = OperatorScope.from_json(json)
# print the JSON string representation of the object
print(OperatorScope.to_json())

# convert the object into a dict
operator_scope_dict = operator_scope_instance.to_dict()
# create an instance of OperatorScope from a dict
operator_scope_from_dict = OperatorScope.from_dict(operator_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


