# FacetFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**values** | [**List[FacetFilterValue]**](FacetFilterValue.md) | Within a single FacetFilter, the values are to be treated like an OR. For example, fieldName type with values [EQUALS Presentation, EQUALS Spreadsheet] means we want to show a document if it&#39;s a Presentation OR a Spreadsheet. | [optional] 
**group_name** | **str** | Indicates the value of a facet, if any, that the given facet is grouped under. This is only used for nested facets, for example, fieldName could be owner and groupName would be Spreadsheet if showing all owners for spreadsheets as a nested facet. | [optional] 

## Example

```python
from openapi_client.models.facet_filter import FacetFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FacetFilter from a JSON string
facet_filter_instance = FacetFilter.from_json(json)
# print the JSON string representation of the object
print(FacetFilter.to_json())

# convert the object into a dict
facet_filter_dict = facet_filter_instance.to_dict()
# create an instance of FacetFilter from a dict
facet_filter_from_dict = FacetFilter.from_dict(facet_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


