# FacetFilterValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**relation_type** | **str** |  | [optional] 
**is_negated** | **bool** | DEPRECATED - please use relationType instead | [optional] 

## Example

```python
from openapi_client.models.facet_filter_value import FacetFilterValue

# TODO update the JSON string below
json = "{}"
# create an instance of FacetFilterValue from a JSON string
facet_filter_value_instance = FacetFilterValue.from_json(json)
# print the JSON string representation of the object
print(FacetFilterValue.to_json())

# convert the object into a dict
facet_filter_value_dict = facet_filter_value_instance.to_dict()
# create an instance of FacetFilterValue from a dict
facet_filter_value_from_dict = FacetFilterValue.from_dict(facet_filter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


