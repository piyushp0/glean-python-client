# RestrictionFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_specs** | [**List[DocumentSpec]**](DocumentSpec.md) |  | [optional] 
**datasource_instances** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.restriction_filters import RestrictionFilters

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictionFilters from a JSON string
restriction_filters_instance = RestrictionFilters.from_json(json)
# print the JSON string representation of the object
print(RestrictionFilters.to_json())

# convert the object into a dict
restriction_filters_dict = restriction_filters_instance.to_dict()
# create an instance of RestrictionFilters from a dict
restriction_filters_from_dict = RestrictionFilters.from_dict(restriction_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


