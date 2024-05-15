# PossibleValue

Possible value of a specific parameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Possible value | [optional] 
**label** | **str** | User-friendly label associated with the value | [optional] 

## Example

```python
from openapi_client.models.possible_value import PossibleValue

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleValue from a JSON string
possible_value_instance = PossibleValue.from_json(json)
# print the JSON string representation of the object
print(PossibleValue.to_json())

# convert the object into a dict
possible_value_dict = possible_value_instance.to_dict()
# create an instance of PossibleValue from a dict
possible_value_from_dict = PossibleValue.from_dict(possible_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


