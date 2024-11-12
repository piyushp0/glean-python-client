# RestrictionFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_specs** | [**List[DocumentSpec]**](DocumentSpec.md) | Specifications for containers that should be used as part of the restriction (include/exclude). Memberships are recursively defined for a subset of datasources (currently: SharePoint, OneDrive, Google Drive, and Confluence). Please contact the Glean team to enable this for more datasources. Recursive memberships do not apply for Collections. | [optional] 

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


