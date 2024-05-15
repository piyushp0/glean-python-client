# InvalidOperatorValueError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The operator key that has an invalid value. | [optional] 
**value** | **str** | The invalid operator value. | [optional] 

## Example

```python
from openapi_client.models.invalid_operator_value_error import InvalidOperatorValueError

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidOperatorValueError from a JSON string
invalid_operator_value_error_instance = InvalidOperatorValueError.from_json(json)
# print the JSON string representation of the object
print(InvalidOperatorValueError.to_json())

# convert the object into a dict
invalid_operator_value_error_dict = invalid_operator_value_error_instance.to_dict()
# create an instance of InvalidOperatorValueError from a dict
invalid_operator_value_error_from_dict = InvalidOperatorValueError.from_dict(invalid_operator_value_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


