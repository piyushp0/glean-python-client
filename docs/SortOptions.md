# SortOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_by** | **str** |  | [optional] 
**sort_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sort_options import SortOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SortOptions from a JSON string
sort_options_instance = SortOptions.from_json(json)
# print the JSON string representation of the object
print(SortOptions.to_json())

# convert the object into a dict
sort_options_dict = sort_options_instance.to_dict()
# create an instance of SortOptions from a dict
sort_options_from_dict = SortOptions.from_dict(sort_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


