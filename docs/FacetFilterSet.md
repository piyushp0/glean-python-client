# FacetFilterSet

Within a single FacetFilterSet, the filters are treated as AND. For example, owner Sumeet and type Spreadsheet shows documents that are by Sumeet AND are Spreadsheets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[FacetFilter]**](FacetFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.facet_filter_set import FacetFilterSet

# TODO update the JSON string below
json = "{}"
# create an instance of FacetFilterSet from a JSON string
facet_filter_set_instance = FacetFilterSet.from_json(json)
# print the JSON string representation of the object
print(FacetFilterSet.to_json())

# convert the object into a dict
facet_filter_set_dict = facet_filter_set_instance.to_dict()
# create an instance of FacetFilterSet from a dict
facet_filter_set_from_dict = FacetFilterSet.from_dict(facet_filter_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


