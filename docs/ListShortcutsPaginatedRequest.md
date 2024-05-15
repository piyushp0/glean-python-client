# ListShortcutsPaginatedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_fields** | **List[str]** | Array of fields/data to be included in response that are not included by default | [optional] 
**page_size** | **int** |  | 
**cursor** | **str** | A token specifying the position in the overall results to start at. Received from the endpoint and iterated back. Currently being used as page no (as we implement offset pagination) | [optional] 
**filters** | [**List[FacetFilter]**](FacetFilter.md) | A list of filters for the query. An AND is assumed between different filters. We support filters on Go Link name, author, department and type. | [optional] 
**sort** | [**SortOptions**](SortOptions.md) |  | [optional] 
**query** | **str** | Search query that should be a substring in atleast one of the fields (alias , inputAlias, destinationUrl, description). Empty query does not filter shortcuts. | [optional] 

## Example

```python
from openapi_client.models.list_shortcuts_paginated_request import ListShortcutsPaginatedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListShortcutsPaginatedRequest from a JSON string
list_shortcuts_paginated_request_instance = ListShortcutsPaginatedRequest.from_json(json)
# print the JSON string representation of the object
print(ListShortcutsPaginatedRequest.to_json())

# convert the object into a dict
list_shortcuts_paginated_request_dict = list_shortcuts_paginated_request_instance.to_dict()
# create an instance of ListShortcutsPaginatedRequest from a dict
list_shortcuts_paginated_request_from_dict = ListShortcutsPaginatedRequest.from_dict(list_shortcuts_paginated_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


